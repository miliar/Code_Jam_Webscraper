#!/usr/bin/env python
#coding=utf-8

def do_case(infile, outfile, case):
    engine_count = int(infile.readline().strip())
    engine_list = {}
    for i in range(engine_count): # read engine list
        engine = infile.readline().strip()
        print engine
        engine_list[engine] = 0
    print engine_list

    query_count = infile.readline().strip()
    query_dict = {}
    switch = 0
    for i in range(int(query_count)):
        query = infile.readline().strip()
        print query
        
        if not query_dict.has_key(query):
            query_dict[query] = 1
            
        if len(query_dict) == engine_count:
            switch = switch + 1 
            query_dict = {}
            query_dict[query] = 1
            print "switch engine"
    
    print switch
    str = "Case #%d: %s" % (case+1, switch)
    print str
    outfile.write(str)
    outfile.write('\n')
    

def QR_A(infile, outfile, total_case):
    for i in range(total_case):
        do_case(infile, outfile, i)
    
    
def main():
    infilepath = "A-large.in"
    outfilepath = infilepath.replace(".in", ".out")
    
    ifobj = file(infilepath)
    ofobj = file(outfilepath, "w")
        
    num_of_case = int(ifobj.readline().strip())
    print int(num_of_case)
    
    QR_A(ifobj, ofobj, num_of_case)
    
    ifobj.close()
    ofobj.close()
    


if __name__ == "__main__":
    main()