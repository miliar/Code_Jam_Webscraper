T = int(input())

for x in range(T):
    N, R, O, Y, G, B, V= map(int, input().split(" "))
    stable = []
    prime = {"R":R, "B":B, "Y":Y}
    secon = {"G":G, "O":O, "V":V}
    equiv = {"G":"R", "O":"B", "V":"Y"}
    seconds = ["G", "O", "V"]
    primes = ["R", "B", "Y"]
    target = N
    fix = 0
    while len(stable) < N and stable != list("IMPOSSIBLE"):
        #print(stable)
        primeKey = sorted(prime, key=prime.get)
        seconKey = sorted(secon, key=secon.get)
        if secon[list(seconKey)[-1]] != 0 and stable != []:
            cur = list(seconKey)[-1]
            part = equiv[cur]
            if prime[part] < secon[cur]:
                if prime[part] == secon[cur]-1:
                    if sum(list(prime.values())) == prime[part] and sum(list(secon.values())) == secon[cur]:
                        for z in range(secon[cur]-1):
                            stable.append(cur)
                            stable.append(part)
                            prime[part] = prime[part] - 1
                            secon[cur] = secon[cur] - 1
                        stable.append(cur)
                        secon[cur] = secon[cur] - 1
                    else:
                        stable = list("IMPOSSIBLE")
                else:
                    stable = list("IMPOSSIBLE")
            elif prime[part] == secon[cur]:
                if stable[-1] == part:
                    for z in range(secon[cur]):
                        stable.append(cur)
                        stable.append(part)
                        prime[part] = prime[part] - 1
                        secon[cur] = secon[cur] - 1
                else:
                    stable = list("IMPOSSIBLE")
            else:
                if stable[-1] != part:
                    for y in range(secon[cur]):
                        stable.append(part)
                        stable.append(cur)
                        prime[part] = prime[part] - 1
                        secon[cur] = secon[cur] - 1
                    stable.append(part)
                    prime[part] = prime[part] - 1
                else:
                    for y in range(secon[cur]):
                        stable.append(cur)
                        stable.append(part)
                        prime[part] = prime[part] - 1
                        secon[cur] = secon[cur] - 1
        else:
            if stable == []:
                if prime[list(primeKey)[-1]] != 0:
                    stable.append(list(primeKey)[-1])
                    prime[list(primeKey)[-1]] = prime[list(primeKey)[-1]] -1
                elif  prime[list(primeKey)[-2]] != 0:
                    stable.append(list(primeKey)[-2])
                    prime[list(primeKey)[-2]] = prime[list(primeKey)[-2]] -1
                elif  prime[list(primeKey)[-3]] != 0:
                    stable.append(list(primeKey)[-3])
                    prime[list(primeKey)[-3]] = prime[list(primeKey)[-3]] -1
                else:
                    stable = list("IMPOSSIBLE")
            elif prime[list(primeKey)[-1]] != 0:
                if list(primeKey)[-1] != stable[-1] and prime[list(primeKey)[-1]] != 0:
                    stable.append(list(primeKey)[-1])
                    prime[list(primeKey)[-1]] = prime[list(primeKey)[-1]] -1
                elif list(primeKey)[-2] != stable[-1] and prime[list(primeKey)[-2]] != 0:
                    stable.append(list(primeKey)[-2])
                    prime[list(primeKey)[-2]] = prime[list(primeKey)[-2]] -1
                elif list(primeKey)[-3] != stable[-1] and prime[list(primeKey)[-3]] != 0:
                    stable.append(list(primeKey)[-3])
                    prime[list(primeKey)[-3]] = prime[list(primeKey)[-3]] -1
                else:
                    stable = list("IMPOSSIBLE")
            else:
                stable = list("IMPOSSIBLE")
    if stable[-1] == stable[0]:
        #print(stable)
        correct = 0
        for z in range(2, len(stable)):
            #print(stable[-z-1])
            if correct != 1:
                #print("HERE")
                if stable[-z-1] != stable[-1] and stable[-z] != stable[-1] and stable[-z-1] in primes and stable[-z] in primes:
                    stable.insert(-z, stable[-1])
                    del stable[-1]
                    correct = 1
        if correct == 0:
            stable = list("IMPOSSIBLE")
    print("Case #" + str(x+1) + ": "+"".join(stable))
    
