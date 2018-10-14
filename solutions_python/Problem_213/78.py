
# coding: utf-8

# In[44]:

def parse(text):
    T = int(text.next())
    
    for i in range(T):
        N,C,M = [int(x) for x in text.next().split(" ")]
        
        Ts = []
        for j in range(M):
            P,B = [int(x) for x in text.next().split(" ")]
            Ts.append((P,B))
        
        soln = solve(N,C,Ts)
        
        print "Case #%d: %s" % (i+1, soln)


# In[45]:

TEXT="""5
2 2 2
2 1
2 2
2 2 2
1 1
1 2
2 2 2
1 1
2 1
1000 1000 4
3 2
2 1
3 3
3 1
3 3 5
3 1
2 2
3 3
2 2
3 1"""


# In[66]:

def solve(N,C,Ts):
    
    #print Ts
    
    afirst = sum(1 for x in Ts if x == (1,1))
    bfirst = sum(1 for x in Ts if x == (1,2))

    asecond = sum(1 for x,y in Ts if x != 1 and y == 1)
    bsecond = sum(1 for x,y in Ts if x != 1 and y == 2)
    
    atot = afirst + asecond
    btot = bfirst + bsecond
    
    #print afirst, bfirst, asecond, bsecond#, atot, btot
    rides = max(afirst + bfirst, atot, btot)
    
    upgrades = 0
    for i in range(1,N+1):
        shared = sum(1 for x,y in Ts if x == i)
        upgrades += max(0, shared - rides)
    
    return "%d %d" % (rides, upgrades)


# In[68]:

parse(x for x in TEXT.splitlines())


# In[70]:

parse(open("C:\Users\mheik\Downloads\B-small-attempt2.in"))


# In[43]:

#parse(open("C:\Users\mheik\Downloads\B-small-attempt0.in"))


# In[ ]:



