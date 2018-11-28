    
def main(filename):
    s1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv"
    s2 = "our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up"
    m = {}
    for i in range(len(s1)):
        m[s1[i]] = s2[i]
    m["q"] = "z"
    m["z"] = "q"

    f = open(filename)
    ouf = open("output.txt", "w")
    num_of_tests = int(f.readline())
    for test_i in range(num_of_tests):
        line = f.readline()
        ans = ""
        for ch in line:
            if ch in m:
                ans += m[ch]
            else:
                ans += ch
        ouf.write("Case #%d: %s" % (test_i + 1, ans))


if __name__ == "__main__":
    main("1.txt")
        
                
        
    