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

ll t,ans,n,p,a[105],c[4],m1,m2,m3,m4;

int main()
{
    ios_base::sync_with_stdio(false);
    ifstream cin;
    cin.open("A-small-attempt0.in");
    ofstream cout;
    cout.open("output1.txt");
    cin>>t;
    rep(l,t)
    {
        cin>>n>>p;
        c[0]=0;
        c[1]=0;
        c[2]=0;
        c[3]=0;
        rep(i,n)
        {
            cin>>a[i];
            a[i]%=p;
            c[a[i]]++;
        }
        if(p==2)
        {
            ans=(c[0]+(c[1]/2));
            c[1]%=2;
            if(c[1]>0)
                ans++;
        }
        else if(p==3)
        {
            m1=min(c[1],c[2]);
            c[1]-=m1;
            c[2]-=m1;
            ans=(c[0]+m1+(c[1]/3)+(c[2]/3));
            c[1]%=3;
            c[2]%=3;
            if(c[1]>0)
                ans++;
            if(c[2]>0)
                ans++;
        }
        else
        {
            m1=min(c[1],c[3]);
            c[1]-=m1;
            c[3]-=m1;
            m2=(c[2]%2);
            c[2]=m2;
            if(c[3]==0)
            {
                m3=min((c[1]/2),m2);
                c[1]-=(2*m3);
                c[2]-=m3;
                m4=(c[1]/4);
                c[1]-=(4*m4);
            }
            else
            {
                m3=min((c[3]/2),m2);
                c[3]-=(2*m3);
                c[2]-=m3;
                m4=(c[3]/4);
                c[3]-=(4*m4);
            }
            ans=(c[0]+m1+(c[2]/2)+m2+m3+m4);
            if(c[1]>0)
                ans++;
            else if(c[2]>0)
                ans++;
            else if(c[3]>0)
                ans++;
        }
        
        cout<<"Case #"<<(l+1)<<": "<<ans<<"\n";
    }
    
    
    
    
    
    cin.close();
    cout.close();
    
    return 0;
}
