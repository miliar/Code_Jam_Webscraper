#-*- coding: utf-8 -*-


import sys

def build_table(engines, queries):
    d = {}
    for engine in engines:
        try:
            d[engine] = queries.index(engine)
        except:
            d[engine] = len(queries)

    return d
    
    
if __name__ == '__main__':
    file_name = sys.argv[1]

    input_file = open(file_name).readlines()
    output_file = open('output.ou', 'w')


    
    N = int(input_file[0])
    input_file = input_file[1:]
    for case in range(1, N+1):
        switches = 0
        
        S = int(input_file[0])
        input_file = input_file[1:]
        search_engines = input_file[0:S]
        input_file = input_file[S:]

        Q = int(input_file[0])
        input_file = input_file[1:]
        queries = input_file[0:Q]
        input_file = input_file[Q:]

        while queries:
            prox = build_table(search_engines, queries)
            #El de mayor valor en proximidad será el primer engine que usaré
            max_prox = max(prox.values())
            #Saco el engine más cercano
            for engine in prox.keys():
                if prox[engine] == max_prox:
                    current = engine
                    break

            #Enviar queries al buscador
            while max_prox > 0:
                queries.pop(0)
                max_prox -= 1
            else:
                if queries:
                    switches += 1
        output_file.write("Case #%d: %d\n"%(case, switches))
