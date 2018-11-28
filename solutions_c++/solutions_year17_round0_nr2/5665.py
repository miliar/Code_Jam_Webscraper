#include <bits/stdc++.h>
#define sll(n) scanf("%lld",&(n))
#define sll2(m,n) scanf("%lld%lld",&(m),&(n))
#define sll3(m,n,o) scanf("%lld%lld%lld",&(m),&(n),&(o))
#define sll4(m,n,o,p) scanf("%lld%lld%lld%lld",&(m),&(n),&(o),&(p))
#define sdd(n) scanf("%lf",&(n))
#define sdd2(m,n) scanf("%lf%lf",&(m),&(n))
#define sdd3(m,n,o) scanf("%lf%lf%lf",&(m),&(n),&(o))
#define sdd4(m,n,o,p) scanf("%lf%lf%lf%lf",&(m),&(n),&(o),&(p))
#define pll(n) printf("%lld ",(n))
#define plln(n) printf("%lld\n",(n))
//#define ps(s) printf("%s",s)
//#define psn(s) printf("%s\n",s)
#define nln printf("\n")
#define cln cout<<"\n"
#define clr(dp,x) memset(dp,x,sizeof(dp))
#define pb push_back
#define mp make_pair
#define s(a) sort(a.begin(),a.end())
#define sa(a,n) sort(a,a+(n))
#define vecll vector<int64_t>
#define vecs vector<string>
#define vecpll vector<pair<int64_t,int64_t> >
#define pii pair <int64_t , int64_t >
#define plpl pair <int64_t , pair <int64_t , int64_t > >
#define ppll pair < pair <int64_t , int64_t > , int64_t >
#define pplpl pair < pair <int64_t , int64_t >, pair <int64_t , int64_t > >
//#define rep(i, begin, end) for (__typeof(end) i = (begin); i != (end) - ((begin) > (end)); i += 1 - 2 * ((begin) > (end)))
#define rep(i,a,n) for(int64_t i=a;i<n;++i)
#define repr(i,b,a) for(int64_t i=b;i>=a;--i)
#define rep1(it,v) for(auto &it:(v))
#define all(c) (c).begin(),(c).end()
#define fast_IO ios_base::sync_with_stdio(false);cin.tie(0);
#define while_tc int64_t testkase;sll(testkase);while(testkase-->0)
#define while_tc_ int64_t testkase;cin>>testkase;while(testkase-->0)
#define adjlw vector<vecpll >  /// ( connected to , weight ) - adjlw adj(MAXN)
#define adjl vecll ///connected to - adjl adj[MAXN]
#define ispow2(n) (n&&(!(n&(n-1))))      ///check if its perfect power of 2
#define ff first
#define ss second
#define bit(mask) __builtin_popcount(mask)
#define lsb(x) __builtin_ffl(x)-1
#define pi 3.1415926535897932384626433832795
typedef int64_t ll;
ll INF=1000000000000000;
ll MOD=1000000007;
ll MOD2 = MOD*MOD;
typedef unsigned long long int ull; /// specifier - llu
using namespace std;

inline ll fastmul(ll e, ll n){ll x=0,p=e;while(n>0){if(n&1)x=x+p;p<<=1;n>>=1;}return x;}
inline ll fastmul(ll e, ll n, ll m){e%=m,n%=m;ll x=0,p=e;while(n>0){if(n&1){x=x+p;if(x>=m)x-=m;}p=p<<1;if(p>=m)p-=m;n>>=1;}return x;}
inline ll power(ll e, ll n){ll x=1,p=e;while(n>0){if(n&1)x=fastmul(x,p);p=fastmul(p,p);n>>=1;}return x;}
inline ll power(ll e, ll n, ll m){ll x=1,p=e;while(n>0){if(n&1)x=fastmul(x,p,m);p=fastmul(p,p,m);n>>=1;}return x;}
inline ll InverseEuler(ll a, ll m){return (a==1? 1 : power(a, m-2, m));}
inline ll lcm(ll a, ll b){return (a*(b/__gcd(a,b)));}
inline ll InverseEuclid(ll a, ll m){ll m0=m,t,q,x0=0,x1=1;if(m==1)return 0;while (a>1){q=a/m;t=m;m=a%m;a=t;t=x0;x0=x1-q*x0;x1=t;}return(x1<0?x1+m0:x1);}
//inline ll CRT(){ll M=1,ans=0;rep(i,0,n)M*=num[i];rep(i,0,n)ans=(ans%M+(rem[i]%M*(M/num[i])*(InverseEuclid(M/num[i],num[i]))%M)%M)%M;return ans;}


ll movex8[]={-1,-1,-1,0,0,1,1,1};
ll movey8[]={-1,0,1,-1,1,-1,0,1};

ll movex4[]={1,-1,0,0};
ll movey4[]={0,0,1,-1};


int main()
{
    freopen("B-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	fast_IO
	ll tc = 1, k, ans;
	while_tc_
	{
	    string s;
        cin>>s;
        ll l = s.length();
        while (true)
        {
            bool ha = true;
            rep(i, 0, l - 1)
                if (s[i] > s[i+1])
                    ha = false;
            if (ha)
                break;
            rep(i, 0, l - 1)
            {
                if (s[i] > s[i+1])
                {
                    s[i] -= 1;
                    rep(j, i+1, l)
                        s[j] = '9';
                    break;
                }
            }
        }
        ll ans = 0;
        rep(i, 0, s.length())
            ans = ans * 10 + (s[i] - '0');
        cout<<"Case #"<<tc++<<": "<<ans<<endl;
	}
	return 0;
}
