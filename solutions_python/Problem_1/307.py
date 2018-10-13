#!/usr/bin/env python

class SEData:
    def __init__(self, name, idx):
        self.name = name
        self.idx = idx
        
    def __str__(self):
        return '%s : %d' % (self.name, self.idx)
        
        

def mycmp(x,y):
    if x.idx < y.idx: return 1
    if x.idx > y.idx: return -1
    return 0

def choose_se( se_list, data ):
    idx = []
    
    for x in se_list:
        if x in data:
            idx.append( data.index( x ))
        else:
            idx.append( len(data ))
        
    #idx = [ data.index(x) for x in se_list if x in se_list ]
    
    se_data = [ SEData(se_list[j], idx[ j]) for j in range(len(se_list))  ]
    
    se_data.sort( mycmp )
    
    return se_data
    


def get_switch_count( se, q, bprint ):
    switch_cnt = 0

    se_data = choose_se( se, q )
    se_used = se_data[0]
    if bprint:print 'Using ', se_used.name

    for i in range(len(q)):
        x = q[i]
        
        if x != se_used.name:
            if bprint:print x
        
        
        if x == se_used.name:
            
            #if bprint:print 'se', se
            se_data = choose_se( se, q[i:] )
            if bprint:print '-->Switching to', se_data[0].name
            switch_cnt += 1
            if bprint:print x
            se_used = se_data[0]
        
    return switch_cnt



def process_input():
    l = open( 'A-large.in').readlines()
    num_inputs = eval(l[0])
    
    lc = 1

    for x in range(num_inputs):
        num_se = eval(l[lc])
        lc += 1        
        
        se_list = []
        for i in range(num_se):
            se_list.append( l[lc].strip() )
            lc += 1
        
        q = []
        num_data = eval(l[lc])
        lc += 1
        #print 'num_data', num_data
        for i in range(num_data):
            q.append( l[lc].strip() )
            lc += 1
            
            
        #print '-'*80
        #print 'list', se_list
        #print 'queries', q
        bprint = False
        
        if x == 7:
            t = 0
            bprint = False
            
        # [queries: %d, se: %d]
        print 'Case #%d: %d' % (( x+ 1), get_switch_count( se_list, q, bprint) ) #, len(q), len(se_list) )
        bprint = False


        
process_input()        
        
        

