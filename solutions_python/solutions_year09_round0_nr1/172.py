
def main():
    with open("A-large.in", "r") as cin:
        list = []
        #List<string> dict = new List<string>();
        tokens = cin.readline().split()
        #string[] tokens = Console.ReadLine().Trim().Split();
        l = int(tokens[0])
        d = int(tokens[1])
        n = int(tokens[2])
        #int l = Convert.ToInt32(tokens[0]), d = Convert.ToInt32(tokens[1]), n = Convert.ToInt32(tokens[2]);
        for i in range(0, d):
        #for (int i = 0; i < d; ++i)
        #{
            w = cin.readline().split()[0]
            #string w = Console.ReadLine().Trim();
            #list[w] = 1
            list.append(w)
            #dict.Add(w);
        #}

        for ca in range(1, n + 1):
        #for (int ca = 1; ca <= n; ++ca) {
            w = cin.readline().split()[0]
            #string w = Console.ReadLine().Trim();
            pos = []
            #SortedList<char, object>[] pos = new SortedList<char, object>[l];
            i = 0
            for j in range(0, l):
            #for (int i = 0, j = 0; i < w.Length; ++j, ++i)
            #{
                pos.append([])
                #pos[j] = new SortedList<char, object>();
                if w[i] == '(':
                #if (w[i] == '(')
                #{
                    i += 1
                    while w[i] != ')':
                        pos[j].append(w[i])
                        i += 1
                    #for (++i; w[i] != ')'; ++i)
                    #{
                        #pos[j].Add(w[i], null);
                    #}
                #}
                else:
                #else:
                #{
                    pos[j].append(w[i])
                    #pos[j].Add(w[i], null);
                #}
                i += 1
            #}

            res = 0
	        #int res = 0;
            for i in range(0, d):
            #for (int i = 0, fl, j; i < d; ++i)
            #{
                fl = 1
                for j in range (0, l):
                #for (j = 0, fl = 1; fl > 0 && j < l; ++j)
                #{
                    if not list[i][j] in pos[j]:
                    #if (!pos[j].ContainsKey(dict[i][j]))
                    #{
                        fl = 0
                        #fl = 0;
                    #}
                #}
                res += fl
                #res += fl;
            #}

            print "Case #%d: %d" % (ca, res)
            #Console.WriteLine("Case #{0}: {1}", ca, res);
        #}

if __name__ == "__main__":
    main()
