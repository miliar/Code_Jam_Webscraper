#include <bits/stdc++.h>
#include <fstream>

using namespace std;
 
typedef long long ll;
typedef vector<ll> vll;
typedef pair<ll,ll> pll;
typedef vector<pll > vpll;
typedef vector<string> vs;
typedef long double ld;

#define rep(i,n) for(ll (i)=0;(i)<(ll)(n);++(i))
#define per(i,n) for(ll (i)=(ll)(n-1);(i)>=0;--(i))
#define reu(i,l,u) for(ll (i)=(ll)(l);(i)<(ll)(u);++(i))
#define uer(i,l,u) for(ll (i)=(ll)(u-1);(i)>=(ll)(l);--(i))
#define each(it,o) for(auto it= (o).begin(); it != (o).end(); ++ it)
#define all(o) (o).begin(), (o).end()
#define mp(x,y) make_pair((x),(y))
#define mset(m,v) memset(m,v,sizeof(m))
#define INF 0x3f3f3f3f3f3f3f3fLL
#define MOD 1000000007
#define m5 100005
#define m6 1000005
#define pb push_back

ll fast_pow(ll base, ll n,ll M)
{
    if(n==0) return 1;
    if(n==1) return (base)%M;
    ll halfn=fast_pow(base,n/2,M);
    if(n%2==0) return ( halfn * halfn ) % M;
    else return ( ( ( halfn * halfn ) % M ) * base ) % M;
}

ll gcd(ll a,ll b)
{
    return b == 0 ? a : gcd(b, a % b);
}

ll t,n,c,m,y,z,p,b,v1=0,v2=0,visit[1005][2];

vll a[1005];

int main()
{
    ios_base::sync_with_stdio(false);
    ifstream cin;
    cin.open("B-small-attempt0.in");
    ofstream cout;
    cout.open("output2.txt");
    cin>>t;
    rep(l,t)
    {
        cin>>n>>c>>m;
        rep(i,1005)
        {
            visit[i][0]=0;
            visit[i][1]=0;
            a[i].clear();
        }
        rep(i,m)
        {
            cin>>p>>b;
            a[b].pb(p);
        }
        y=(max(a[1].size(),a[2].size()));
        rep(i,a[1].size())
            visit[a[1][i]][0]++;
        rep(i,a[2].size())
            visit[a[2][i]][1]++;
        z=0;
        rep(i,1005)
        {
            if(i==1)
                y=max(y,(visit[i][0]+visit[i][1]));
            else
            {
                if((visit[i][0]+visit[i][1])>y)
                    z+=((visit[i][0]+visit[i][1])-y);
            }
        }
        
        
        cout<<"Case #"<<(l+1)<<": "<<y<<" "<<z<<"\n";
    }
    
    
    
    
    
    cin.close();
    cout.close();
    
    return 0;
}
