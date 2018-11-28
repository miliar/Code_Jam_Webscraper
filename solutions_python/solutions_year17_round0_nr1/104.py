def flip(array,fr,to):
    for i in range(fr,to+1):
        array[i] = 1 - array[i]
    return array

def check(array):
    return sum(array) == len(array)

with open("input.txt","r") as reader, open("output.txt","w") as writer:
    cases = int(reader.readline())
    for cs in range(1,cases+1):
        cakes,K = reader.readline().split(" ")
        cakes = list(cakes)
        cakes = [ 0 if x == '-' else 1 for x in cakes]
        K = int(K)
        answer = 0
        for i in range(len(cakes)-K+1):
            if cakes[i] == 0:
                cakes = flip(cakes,i,i+K-1)
                answer += 1
        if check(cakes):
            writer.write("Case #"+str(cs)+": "+str(answer)+"\n")
        else:
            writer.write("Case #"+str(cs)+": IMPOSSIBLE\n")


