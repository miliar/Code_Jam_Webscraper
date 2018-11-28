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
ll t,r,c,l;

char a[50][50],ch;

int main()
{
    ios_base::sync_with_stdio(false);
    fstream cin;
    cin.open("A-large.in");
    ofstream cout;
    cout.open("output.txt");
    
    cin>>t;
    for(l=1;l<=t;l++)
    {
        cin>>r>>c;
        rep(i,r)
        {
            rep(j,c)
                cin>>a[i][j];
        }
        rep(i,r)
        {
            ch='?';
            rep(j,c)
            {
                if(a[i][j]=='?')
                    a[i][j]=ch;
                ch=a[i][j];
            }
        }
        rep(i,r)
        {
            ch='?';
            per(j,c)
            {
                if(a[i][j]=='?')
                    a[i][j]=ch;
                ch=a[i][j];
            }
        }
        rep(i,c)
        {
            ch='?';
            rep(j,r)
            {
                if(a[j][i]=='?')
                    a[j][i]=ch;
                ch=a[j][i];
            }
        }
        rep(i,c)
        {
            ch='?';
            per(j,r)
            {
                if(a[j][i]=='?')
                    a[j][i]=ch;
                ch=a[j][i];
            }
        }
        cout<<"Case #"<<l<<":\n";
        rep(i,r)
        {
            rep(j,c)
                cout<<a[i][j];
            cout<<"\n";
        }
    }
    
    cin.close();
    cout.close();
    return 0;
}
