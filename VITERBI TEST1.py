def viterbi(A, k, n, y):
    N = len(y[0])
    INFTY = k*n + 2
    nb_states = 2**n
    old_weights = [ INFTY for i in range(nb_states) ]
    old_weights[0] = 0
    new_weights = [ INFTY for i in range(nb_states) ]
    prec = [ [] for i in range(N) ]
    for j in range(N):
        for i in range(nb_states):
            rem = i % 2**(n-1)
            prev_state_1 = 2 * rem
            prev_state_2 = 2 * rem + 1
            path_1 = old_weights[prev_state_1] + sum([abs(int(y[m][j]) - int(A[prev_state_1][i // 2**(n-1)][m])) for m in range(k)])
            path_2 = old_weights[prev_state_2] + sum([abs(int(y[m][j]) - int(A[prev_state_2][i // 2**(n-1)][m])) for m in range(k)])
            if path_1 <= path_2:
                new_weights[i] = path_1
                prec[j].append(prev_state_1)
            else:
                new_weights[i] = path_2
                prec[j].append(prev_state_2)
        old_weights = [ new_weights[i] for i in range(nb_states) ]
    min_weight = min(old_weights)
    m = old_weights.index(min_weight)
    best_path = [ m ]
    for j in range(N-1, -1, -1):
        aux = prec[j][m]
        best_path = [ aux ] + best_path
        m = aux
    return [ best_path[i] // 2**(n-1) for i in range(1, N) ]
