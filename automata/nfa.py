class NFA:
    def __init__(self, states, alphabet, transition, start_state, accepted_states):
        self.states = states
        self.alphabet = alphabet
        self.transition = transition
        self.start_state = start_state
        self.accepted_states = accepted_states


