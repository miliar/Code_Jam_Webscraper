#include<iostream>
#include<cstring>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<fstream>
#include<queue>
#include<map>
using namespace std;
long long n, k, idx, ansMin, ansMax;
map<long long, long long> mp;
void solve()
{
    long long p, q, t, cnt;
    idx = 0;
    mp.clear();
    priority_queue<long long> que;
    que.push(n);
    mp[n] = 1;
    while(!que.empty())
    {
        p = que.top();
        que.pop();
        cnt = mp[p];
        idx += cnt;
        if(p % 2 == 0)
        {
            t = p/2 - 1;
            q = p/2;
        }
        else
        {
            t = p/2;
            q = p/2;
        }
        if(mp[q])
            mp[q]+=cnt;
        else
        {
            mp[q] = cnt;
            que.push(q);
        }
        if(mp[t])
            mp[t]+=cnt;
        else
        {
            mp[t] = cnt;
            que.push(t);
        }
        if(idx >= k)
        {
            ansMin = t;
            ansMax = q;
            return;
        }
    }
}
int main()
{
    freopen("G:\\C.in", "r", stdin);
    freopen("G:\\C.out", "w", stdout);
    int T;
    scanf("%d",&T);
    for(int ica=1;ica<=T;ica++)
    {
        scanf("%I64d %I64d", &n, &k);
        solve();
        printf("Case #%d: %I64d %I64d\n", ica, ansMax, ansMin);
    }
}