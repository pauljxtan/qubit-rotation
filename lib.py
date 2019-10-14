import pennylane as qml

GATE_MAP = {
    'RX': qml.RX,
    'RY': qml.RY,
    'RZ': qml.RZ,
}

OBS_MAP = {
    'PauliX': qml.PauliX,
    'PauliY': qml.PauliY,
    'PauliZ': qml.PauliZ,
}

def rotate_qubit(gates, params, observable):
    # Map to pennylane functions
    gates = [GATE_MAP[gate] for gate in gates]
    observable = OBS_MAP[observable]

    # Create device
    device = qml.device('default.qubit', wires=1)

    # Define quantum function
    # Decorator converts it into `QNode` running on device `device`
    @qml.qnode(device)
    def circuit():
        for gate, param in zip(gates, params):
            gate(param, wires=0)
        return qml.expval(observable(0))

    return circuit()
