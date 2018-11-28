
# coding: utf-8

# In[34]:

def parse(text):
    T = int(text.next())
    
    for i in range(T):
        N,P = [int(x) for x in text.next().split(" ")]
        groups = [int(x) for x in text.next().split(" ")]
        
        soln = solve(N, P, groups)
        
        print "Case #%d: %s" % (i+1, soln)


# In[35]:

TEXT="""3
4 3
4 5 6 4
4 2
4 5 6 4
3 3
1 1 1"""


# In[53]:

def solve(N, P, groups):
    
    sizes = {0:0,1:0,2:0,3:0}
    
    for g in groups:
        sizes[g%P] += 1
      
    #print P, sizes[0], sizes[1], sizes[2]
    if P == 2:
        return sizes[0] + sizes[1] - sizes[1]/2
    
    if P == 3:
        pairs = min(sizes[1], sizes[2])
        remainder = N - sizes[0] - pairs - pairs
        return sizes[0] + pairs + (remainder+2)/3


# In[54]:

parse(x for x in TEXT.splitlines())


# In[55]:

parse(open("C:\Users\mheik\Downloads\A-small-attempt1.in"))


# In[42]:

#parse(open("C:\Users\mheik\Downloads\A-small-attempt0.in"))


# In[ ]:



