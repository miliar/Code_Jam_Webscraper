if __name__ == '__main__':
    n=int(raw_input())
    for x in range(n):
        s=int(raw_input())
        engines = set(str(raw_input()) for y in range(s))
        q=int(raw_input())
        queries = [str(raw_input()) for y in range(q)]
        used_queries = set()
        ans=0
        for query in queries:
            used_queries.add(query)
            if len(used_queries) == len(engines):
                ans+=1
                used_queries.clear()
                used_queries.add(query)
        print 'Case #'+str(x+1)+': '+str(ans)
        