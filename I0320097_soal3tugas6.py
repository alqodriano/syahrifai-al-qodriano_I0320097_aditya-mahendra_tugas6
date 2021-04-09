#soal3
#alqodriano
for T in range (10,25) :
    for E in range(2, T):
        if (T % E) == 0:
            print(T, "bukan prima")
            break
        else:
            print(T, "adalah bilangan prima")
            break