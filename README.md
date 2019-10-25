# qubit-rotation

This Flask app simply applies a user-supplied circuit of rotation [gates](https://pennylane.readthedocs.io/en/latest/introduction/operations.html#qubit-gates) (`RX`, `RY`, `RZ`) to a single qubit, and measures one of the Pauli [observables](https://pennylane.readthedocs.io/en/latest/introduction/operations.html#qubit-observables) (`PauliX`, `PauliY`, `Pauliz`), using the [PennyLane](https://github.com/XanaduAI/pennylane) library.

It may be deployed directly to Heroku: here's a [demo](https://qubit-rotation.herokuapp.com).

## To-do

- [ ] Migrate to a more interactive JS/Wasm-based frontend
    - [ ] Refactor Flask to expose a JSON API
