#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define vl vector<ll>

#ifndef ONLINE_JUDGE
#  define dbg(x) (cerr << #x << " = " << (x) << endl)
#define dbg2(x,y) (cerr<<#x<<" = "<<x<<" "<<#y<<" = "<<y<<endl)
#else
#define dbg(x) 0
#define dbg2(x,y) 0
#endif

#define N 1234567
#define pll pair<ll,ll>

priority_queue<ll>p;
ll n,k;
map<ll,ll>mp,mpRev;
set<ll>vis;
vector<pair<ll,ll> >v;

void go()
{
    p.push(n);
    mp[n]++;
    while(p.top()>0)
    {
        auto it=p.top();
        p.pop();
        if(it%2==1)
        {
            mp[it/2]+=2*mp[it];
            if(vis.find(it/2)==vis.end())
            {
                p.push(it/2);
                vis.insert(it/2);
            }
        }
        else
        {
            mp[it/2]+=mp[it];
            mp[(it/2)-1]+=mp[it];
            if(vis.find(it/2)==vis.end())
            {
                p.push(it/2);
                vis.insert(it/2);
            }
            if(vis.find((it/2)-1)==vis.end())
            {
                p.push((it/2)-1);
                vis.insert((it/2)-1);
            }
        }

    }
//    for(auto it:mp)
//        dbg2(it.first,it.second);
    ll cnt=0;
    for(auto it:mp)
    {
        mpRev[-it.first]=it.second;
    }
    for(auto it:mpRev)
    {
        cnt+=it.second;
        v.push_back(make_pair(cnt,-it.first));
    }
}


int main()
{
freopen("IP.txt","r",stdin);
freopen("OPG.txt","w",stdout);
    ll t;
    cin>>t;
    ll K=1;
    while(t--)
    {
        mp.clear();
        mpRev.clear();
        vis.clear();
        p.empty();
        v.clear();
        cin>>n>>k;
        go();

//        for(auto it:v)
//        {
//            dbg2(it.first,it.second);
//        }
        auto it=lower_bound(v.begin(),v.end(),make_pair(k,0LL));
        ll ans=it->second;
        cout<<"Case #"<<K++<<": ";
        if(ans%2==0)
            cout<<(ans/2)<<" "<<(ans/2)-1<<endl;
        else
            cout<<(ans/2)<<" "<<(ans/2)<<endl;
    }
}
