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

ll t,k,l,ans,len,la,v[1005],r;
string s;

int main()
{
    ios_base::sync_with_stdio(false);
    ifstream cin;   
    cin.open("A-large.in");
    ofstream cout;
    cout.open("output.txt");
    cin>>t;
    for(l=1;l<=t;l++)
    {
        cin>>s>>k;
        ans=0;
        len=s.length();
        rep(i,len)
            v[i]=0;
        la=-1;
        rep(i,len)
        {
            if(i==0)
            {
                if(s[i]=='-')
                {
                    v[i]=1;
                    ans++;
                }
            }
            else
            {
                if((i-k)>=0)
                    r=v[i-1]-v[i-k];
                else
                    r=v[i-1];
                if(r<0)
                    r=0;
                if(s[i]=='-')
                {
                    if((r%2)==0)
                    {
                        if((i+k)<=len)
                        {
                            v[i]=v[i-1]+1;
                            ans++;
                        }
                        else
                            break;
                    }
                    else
                        v[i]=v[i-1];
                }
                else
                {
                    if((r%2)!=0)
                    {
                        if((i+k)<=len)
                        {
                            v[i]=v[i-1]+1;
                            ans++;
                        }
                        else
                            break;
                    }
                    else
                        v[i]=v[i-1];
                }
            }
            la=i;
        }
        if(la==(len-1))
            cout<<"Case #"<<l<<": "<<ans<<"\n";
        else
            cout<<"Case #"<<l<<": IMPOSSIBLE\n";
    }
    
    
    
    cin.close();
    cout.close();
    
    return 0;
}
