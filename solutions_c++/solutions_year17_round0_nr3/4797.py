#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

#define trace(x)    cerr << #x << ": " << x << endl;
#define bitcount    __builtin_popcountll
#define MOD 1000000007
#define pb push_back
#define pi pair<long long, long long>
#define pii pair<pi,int>
#define mp make_pair

pi stalls(ll n, ll k)
{
    if(k==1)
        return mp(n/2, (n-1)/2);
    if((k-1)%2==1)
        return stalls(n/2, k/2);
    return stalls((n-1)/2, (k-1)/2);
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    freopen("stalls_small1.in", "r", stdin);
    freopen("a78.txt", "w", stdout);
    ll n, k, i, l, t=1, a[65];
    a[0]=1;
    for(i=1; i<=60; i++)
        a[i]=2*a[i-1];
    for(i=1; i<=60; i++)
        a[i]+=a[i-1];
    cin>>t;
    for(l=1; l<=t; l++)
    {
        cin>>n>>k;
        pi x=stalls(n, k);
        cout<<"Case #"<<l<<": "<<x.first<<" "<<x.second<<endl;
    }
    return 0;
}
