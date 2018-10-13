def bin_search(l,start,end,f):
        if start == end:
                return start
        else:
                mid = (start+end)/2
                if l[mid] <= f:
                        return bin_search(l,start,mid,f)
                else:
                        return bin_search(l,mid+1,end,f)

t = input()
for i in range(t):
        n = input()
        naomi = map(float,raw_input().split())
        ken = map(float,raw_input().split())
        naomi.sort(reverse=True)
        ken.sort(reverse=True)
        n_count = n-1
        k_count = n-1
        deceit = 0
        while (n_count >= 0):
                if naomi[n_count] > ken[k_count]:
                        deceit = deceit + 1
                        n_count = n_count - 1
                        k_count = k_count - 1
                else:
                        n_count = n_count - 1
                        
        n_count = 0
        k_count = 0
        opt_war = 0
        while (n_count < n):
                if naomi[n_count] > ken[k_count]:
                        opt_war = opt_war+1
                        n_count = n_count + 1
                else:
                        next_pos = bin_search(ken,k_count,n-1,naomi[n_count])
                        if next_pos == k_count:
                                break
                        n_count = n_count + (next_pos - k_count)
                        k_count = next_pos
        print 'Case #'+str(i+1)+': '+str(deceit)+' '+str(opt_war)

