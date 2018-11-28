#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <queue>
using namespace std;

long long n, k;

struct node
{
    long long m, l;
    friend bool operator < (const node &i, const node &j)
    {
        if(i.l == j.l) return i.m < j.m;
        return i.l < j.l;
    }
};



int main()
{
    int T;
    scanf("%d", &T);
    for(int Case = 1; Case <= T; ++Case)
    {
        priority_queue<node>  pq;
        while(!pq.empty()) pq.pop();
        scanf("%lld%lld", &n, &k);
        pq.push((node){1, n});
        while(k)
        {
            node tmp = pq.top(); pq.pop();
            while(!pq.empty() && pq.top().l == tmp.l) tmp.m += pq.top().m, pq.pop();
            //cout<<pq.top().m <<" " << pq.top().l<<" "<<k<<endl;
            if(k <= tmp.m)
            {
                long long mx, mi;
                if(tmp.l % 2) mx = mi = tmp.l / 2;
                else mx = tmp.l / 2ll, mi = mx - 1ll;
                printf("Case #%d: %lld %lld\n", Case, mx, mi);
                break;
            }
            else
            {
                k -= tmp.m;
                if(tmp.l % 2) pq.push((node){2 * tmp.m, tmp.l / 2ll});
                else
                {
                    pq.push((node){tmp.m, tmp.l / 2ll});
                    pq.push((node){tmp.m, tmp.l / 2ll - 1ll});
                }
            }
        }
    }
    
    return 0;
}
