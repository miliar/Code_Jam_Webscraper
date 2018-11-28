
def get_parents( elem, vals ):
    #print elem, vals
    parents = set( vals[ elem - 1 ] )
    result = set( parents )
    for i in parents:
        result.update( get_parents( i, vals ) )
    return result 

def check( depends ):
    vals = []
    for v in depends:
        l = [ int(x) for x in v.split() ][1:]
        vals.append( l )
    for i, v in enumerate( vals ):
        i = i + 1
        if len( v ) > 1:
            all_parents = list()
            for j in v:
                r = get_parents(j, vals) 
                r.update( [j,] )
                all_parents.append( set(r) )
                alllist = []
                for l in all_parents:
                    alllist.extend( set(l) )
                if len(alllist) > len( set( alllist ) ):
                    return 'Yes'



            
    return 'No'

def main():
    data = open( 'in', 'r' ).readlines()
    count = int( data[0] )
    fv = 1
    num = 0
    for i in range( count ):
        count_vals = int( data[ fv ] )
        depends = data[fv + 1: fv + 1 + count_vals]
        fv += count_vals + 1
        num += 1
        print "Case #%s: %s" % ( num, check( depends ) )

if __name__ == '__main__':
    main()
