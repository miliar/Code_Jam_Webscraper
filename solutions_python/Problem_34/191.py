def matches(word, pattern):
    for i in range(len(word)):
        if word[i]== pattern[0]:
            pattern = pattern[1:]
            continue

        elif pattern[0]!= "(":
            return 0

        elif pattern[0]=="(":
            t = pattern.partition(")")
            pattern = t[0]
            for j in range(len(pattern)):
                if word[i]== pattern[j]:
                    pattern = t[2]
                    break
            else:
                return 0
    return 1

def main():
    f = open("./Desktop/A-large.in")
    g = open("./Desktop/output","w")

    s = f.readline()
    tmp = s.partition(" ")
    L = int(tmp[0])
    s = tmp[2]
    tmp = s.partition(" ")
    D = int(tmp[0])
    N = int(tmp[2])
    
    words = []
    for i in range(D):
        s = f.readline()
        words.append(s)
    
    patterns = []
    for i in range(N):
        s = f.readline()
        patterns.append(s)
        
    
    
    for i in range(N):
        sum = 0
        for word in words:
           if(matches(word,patterns[i])):
               sum = sum + 1
               
        s = "Case #" + str(i+1) + ": " + str(sum) + "\n"
        g.write(s)
        
