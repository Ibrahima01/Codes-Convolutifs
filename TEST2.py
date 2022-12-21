def normalize(y):
    i = len(y)
    while (i > 0 and y[i-1] == 0):
        i -= 1
    return y[:i]

def next_state(i, b, n):
    return b*2**(n-1) + (i//2)

def ev_generator(g, state, b, n):
    i = state
    res = FF.zero()
    coeffs = g.coefficients(sparse=False)
    d = g.degree()
    if (n > d):
        coeffs += [ FF.zero() for j in range(n - d) ]
    for j in range(n):
        res += coeffs[n-j] * FF(i % 2)
        i //= 2
    res += coeffs[0] * b
    return res

def encode_with_generators(G, x):
    P = R(x)
    polys = [ P * g for g in G ]
    res = [ Y.coefficients(sparse=False) for Y in polys ]
    m = max(len(y) for y in res)
    return [ r + [0 for j in range(m-len(r))] for r in res ]

def TEST_encode_with_generators():
    G = [ FF.one() + Z + Z**2, FF.one() + Z]
    x = [0, 1, 0, 1]
    vec_c = encode_with_generators(G, x)
    print(vec_c)
