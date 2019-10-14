from flask import Flask, render_template, request

from lib import rotate_qubit

app = Flask(__name__)


@app.route('/')
def index():
    circuit = request.args.get('circuit')
    if circuit:
        # Parse URL params
        elems = circuit.split(',')
        gates = [elems[i].strip() for i in range(0, len(elems) - 1, 2)]
        params = [float(elems[i].strip()) for i in range(1, len(elems) - 1, 2)]
        obs = elems[-1].strip()

        # Compute rotation
        result = rotate_qubit(gates, params, obs)

        print(f'GATES: {gates}')
        print(f'PARAMS: {params}')
        print(f'OBSERVABLE: {obs}')
        print(f'RESULT: {result}')

        # Format nice LaTeX strings
        gate_to_tex = {'RX': 'R_x', 'RY': 'R_y', 'RZ': 'R_z'}
        gates = ', '.join([
            f'\({gate_to_tex[gate]}({params[i]})\)'
            for i, gate in enumerate(gates)
        ])
        obs_to_tex = {
            'PauliX': '\\sigma_x',
            'PauliY': '\\sigma_y',
            'PauliZ': '\\sigma_z'
        }
        obs = f'\({obs_to_tex[obs]} = {result}\)'

        return render_template('index.html', circuit=circuit, gates=gates, obs=obs)
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
