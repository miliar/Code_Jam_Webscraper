#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

ll N, K;



int main()
{
    freopen("C-small-2-attempt0.in","r",stdin);
    freopen("C-small-2-attempt0.out","w",stdout);
    int t;
    cin >> t;
    for(int tc=1;tc<=t;tc++)
    {
        priority_queue<pair<ll,int> > pq;
        cin >> N >> K;
        pq.push({N,-1});
        while(--K)
        {
            auto u = pq.top();
            ll best = u.first;
            int idx = u.second;
            pq.pop();
            ll x = (best+1)>>1;
            pq.push({best-x,idx-x});
            pq.push({x-1,idx});
        }
        auto u = pq.top();
        ll best = u.first;
        pq.pop();
        ll x = (best+1)>>1;
        ll L = x-1;
        ll R = best-x;
        cout << "Case #" << tc << ": " << max(L,R) << " " << min(L,R) << '\n';
    }
    return 0;
}
