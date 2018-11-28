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
ll t,n,p,l,ans,q[60];
ll g[60],h[60][60],low[60][60],high[60][60];
bool o;

bool recurse(ll pos,ll lval,ll hval)
{
    if((pos==n)&&(hval>=lval))
    {
        ans++;
        return true;
    }
    bool f;
    if(pos==0)
    {
        rep(i,p)
            f=recurse(pos+1,low[pos][i],high[pos][i]);
        return f;
    }
    else
    {
        reu(i,q[pos],p)
        {
            if((low[pos][i]>hval)||(high[pos][i]<lval))
            {
                if(low[pos][i]>hval)
                    return false;
            }
            else
            {
                if(recurse(pos+1,max(lval,low[pos][i]),min(hval,high[pos][i])))
                {
                    q[pos]=i+1;
                    return true;
                }
            }
        }
        return false;
    }
}


int main()
{
    ios_base::sync_with_stdio(false);
    fstream cin;
    cin.open("B-large.in");
    ofstream cout;
    cout.open("output1.txt");
    
    cin>>t;
    for(l=1;l<=t;l++)
    {
        cin>>n>>p;
        ans=0;
        rep(i,n)
            cin>>g[i];
        rep(i,n)
            q[i]=0;
        rep(i,n)
        {
            rep(j,p)
                cin>>h[i][j];
            sort(h[i],h[i]+p);
            rep(j,p)
            {
                low[i][j]=(10*h[i][j]);
                if((low[i][j]%(11*g[i]))==0)
                    low[i][j]/=(11*g[i]);
                else
                    low[i][j]=(low[i][j]/(11*g[i]))+1;
                high[i][j]=((10*h[i][j])/(9*g[i]));
                //cout<<low[i][j]<<" "<<high[i][j]<<"\n";
            }
            //cout<<"\n";
        }
        //cout<<"\n";
        o=recurse(0,0,0);
        cout<<"Case #"<<l<<": "<<ans<<"\n";
    }
    
    cin.close();
    cout.close();
    return 0;
}
