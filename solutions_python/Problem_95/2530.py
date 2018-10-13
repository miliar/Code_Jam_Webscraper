import sys

erese = {"a":"y", "b":"h", "c":"e", "d":"s", "e":"o", "f":"c", "g":"v", "h":"x", "i":"d", "j":"u",
         "k":"i", "l":"g", "m":"l", "n":"b", "o":"k", "p":"r", "q":"z", "r":"t", "s":"n" ,"t":"w" ,"u":"j",
         "v":"p", "w":"f", "x":"m", "y":"a", "z":"q", " ":" ", "\n":""}

if __name__ == "__main__":
    T = int(raw_input())
    i = 1
    for cad in sys.stdin:
        google = list(cad)
        for x in range(len(google)):
            google[x] = erese[google[x]]
        print "Case #" + str(i) + ": " + ''.join(google)
        i += 1

