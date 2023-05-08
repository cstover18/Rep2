def momentum_energy(m, v):
    m = float(input("What is the mass in g?"))
    v = float(input("What is the velocity in m/s?"))
    p = m * v
    e = 0.5 * m * v**2
    return p, e


momentum_energy(m, v)
