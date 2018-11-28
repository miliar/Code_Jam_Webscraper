#include <bits/stdc++.h>

using namespace std;

void bfsolve()
{
    int n,k;
    cin >> n >> k;
    vector<int> v;
    v.push_back(0);
    v.push_back(n+1);
    int mx,mn;
    while(k--)
    {
        mx = 0,mn = 0;
        int res=0;
        int dex = 0;
        for(int i=1;i<=n;++i)
        {
            if(min(i-v[dex],v[dex+1]-i)>mn)
            {
                mn = min(i-v[dex],v[dex+1]-i);
                mx = max(i-v[dex],v[dex+1]-i);
                res = i;
            }
            else if (min(i-v[dex],v[dex+1]-i)==mn && max(i-v[dex],v[dex+1]-i)>mx)
            {
                mx = max(i-v[dex],v[dex+1]-i);
                res = i;
            }
            if(v[dex+1]==i) dex++;
        }
        if(!k) cout << mx-1 << " " << mn-1 << "\n";
        v.push_back(res);
        sort(v.begin(),v.end());
    }
    return;
}
struct thing
{
    int l,r;
};
struct cmp
{
    bool operator()(const thing &a,const thing&b)
    {
        return (a.r-a.l)<(b.r-b.l);
    }
};


void solve()
{
    int n,k;
    cin >> n >> k;
    priority_queue<thing,vector<thing>,cmp> pq;
    pq.push({0,n+1});
    while(k--)
    {
        thing t = pq.top();
        pq.pop();
        int ll = t.l, lr = (t.l+t.r)/2, rl = (t.l+t.r)/2, rr = t.r;
        if(!k)
        {
            cout << max(lr-ll-1,rr-rl-1) << " " << min(lr-ll-1,rr-rl-1) << "\n";
            return;
        }
        pq.push({ll,lr});
        pq.push({rl,rr});
    }

}

int main()
{
    int T;
    cin >> T;
    for(int t=1;t<=T;++t)
    {
        cout << "Case #" << t << ": ";
        solve();
    }
    return 0;
}
