// I am +++++++++++[>++++++<-]>.+<+++++[>++++++<-]>.+++<++[>+++++<-]>..+++++++.
#include <bits/stdc++.h>
using namespace std;

//#define ONLINE_JUDGE
#ifndef ONLINE_JUDGE
	#define TRACE
	#define DEBUG
#endif
// CPP ALL MACROS ---------------- {{{
#ifdef TRACE
	#define trace(...) cerr  << "[" << __FUNCTION__ << " : " << __LINE__ << "] ";__f(#__VA_ARGS__,__VA_ARGS__)
	template <typename Arg1> void __f(const char* name,Arg1 && arg1){cerr<<name<<" = "<<arg1<<endl;}
	template <typename Arg1,typename... Args>
	void __f(const char* names,Arg1&& arg1,Args&&... args) {const char* comma=strchr(names+1,',');cerr.write(names,comma-names)<<" = "<<arg1<<" | ";__f(comma+1,args...);}
#else
	#define trace(...)
#endif

#ifdef DEBUG
	#define CERR cerr << "[" << __FUNCTION__ << " : " << __LINE__ << "]  "
	#define Assert(x,y) {if(x!=y) {CERR << "ERROR ----->> ( " << #x "!=" << y <<" ) " << "| GOT ----->> " << x << endl;exit(1);}};
	#define pause system("sleep 0.5s")
	#define putx(x) x
	#define msg(MSG) cerr <<__FUNCTION__<<" : msg :- "<< MSG <<endl
	#define debug(x) cerr << '>' << #x << ':' << x << endl
#else
	#define Assert(x,y)
	#define pause
	#define putx(x)
	#define msg(MSG)
	#define debug(x)
#endif

typedef long long ll;
typedef long double ld;
typedef istringstream iss;
typedef ostringstream oss;
typedef pair<int,int> pii;

// My Macros

// I/O
// special i/o
#define Nitro() ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0)
#define openup freopen("input.txt","r",stdin)
#define closeup freopen("output.txt","w",stdout);
#define pw putchar(' ')
#define pn putchar('\n')
#define dg(s,i) printf("%s %d",s,i)
#define endl '\n'

// num i/o
#define si(n) scanf("%d",&n)
#define pi(n) printf("%d",n)
#define sl(n) scanf("%lld",&n)
#define pl(n) printf("%lld",n)
#define sd(n) scanf("%Lf",&n)
#define pd(n) printf("%Lf",n)

// char i/o
#define gc(n) n=getchar()
#define pc(n) putchar(n)
#define gs(n) scanf("%s",n)
#define ps(n) printf("%s",n)
#define gcc(n) n=getchar_unlocked()
#define pcc(n) puchar_unlocked(n)

// Access
#define sz size()
#define ln length()
#define ff first
#define ss second
#define pb push_back //pop_back
#define pp pop_back
#define mp make_pair

// loops
// int
#define REP(i,n) for(int i=0;i<(n);i++)
#define FOR(i,a,b) for(int i=(a);i<=(b);i++)
#define RFOR(i,a,b) for(int i=(a);i>=(b);i--)

// STL
#define forall(it, x) for(__typeof((x).begin()) it=(x).begin();it!=(x).end();it++)
#define rep(i,z) for(int i=0;i<(z.sz);i++)
#define rforall(it, x) for(__typeof((x).rbegin()) it=(x).rbegin();it!=(x).rend();it++)
#define rrep(i,z) for(int i=((z.sz)-1);i>=0;i--)

// special
#define mset(a,val) memset(a,val,sizeof(a))
#define mcpy(a,b)   memcpy(a,b,sizeof(a))
#define mcmp(a,b)   memcmp(a,b,sizeof(a))
#define all(a)  a.begin(),a.end()
#define rall(a) a.rbegin(),a.rend()
#define ins(A, P, B) A.insert(A.begin() + P, B)
#define ers(A, P) A.erase(A.begin() + P)
#define lbnd(A, x) (lower_bound(all(A), x) - A.begin())
#define is_in(T, x) (T.find(x) != T.end())
template<class T> void unq(T &A){ sort(all(A));A.resize(unique(all(A))-A.begin());}

// Constant's
// [[360`Deg]==[2PI`Rad]]
const int Inf = 0x3f3f3f3f;
const ll Inff = 0x3f3f3f3f3f3f3f3fLL;
const int MAX = ll(1e9+7);  // const int MAX=1000000007;
const ld  EPS = ld(1e-9);
const double eps = double(1e-6);
const ld PI=ld(3.1415926535897932384626); // M_PI
const int dx[]={-1,0,1,0};
const int dy[]={0,1,0,-1};
const int d8x[]={-1,-1,-1,+0,+0,+1,+1,+1};
const int d8y[]={-1,+0,+1,-1,+1,-1,+0,+1};


#define imax numeric_limits<int>::max()
#define imin numeric_limits<int>::min()
#define lmax numeric_limits<ll>::max()
#define lmin numeric_limits<ll>::min()

double tick(){static clock_t oldt,newt=clock();double diff=1.0*(newt-oldt)/CLOCKS_PER_SEC;oldt=newt;return diff;}
ll Nmul(ll A,ll B){ll ret = (ll)((ll)(A)*(ll)(B));return ret;}ll Mmul(ll a,ll b,ll mod){ll c=Nmul(a,b);c%=mod;while(c<0){c+=mod;};return c;}
ll Nadd(ll A,ll B){ll ret = (ll)((ll)(A)+(ll)(B));return ret;}ll Madd(ll a,ll b,ll mod){ll c=Nadd(a,b);while(c>=mod){c-=mod;};while(c<0){c+=mod;};return c;}
ll Nsub(ll A,ll B){ll ret = (ll)((ll)(A)-(ll)(B));return ret;}ll Msub(ll a,ll b,ll mod){return Madd(a,mod-b,mod);}
ll Npow(ll A,ll p){ll ret=1;while(p){if(p&1){ret=(ret*A);}A=(A*A);p>>=1;}return ret;}ll Mpow(ll a,ll n,ll b){ll res=1;while(n){if(n&1) {res=Mmul(res,a,b);}a=Mmul(a,a,b);n>>=1;}return Madd(res,0,b);}
ll Ndiv(ld A,ld B,bool ud){if(B){ld ret=(ld)(A)/(ld)(B);if(ud)return ceil(ret);return floor(ret);}return Inf;}ll Mdiv(ll a,ll b,ll mod){ll ans=Mmul(a,Mpow(b,mod-2,mod),mod);return ans;}

//#define TREES
#ifdef TREES
	#define LC ((i*2)+1)
	#define RC ((i*2)+2)
	#define LV l,m,LC
	#define RV m+1,r,RC
#endif
/// }}}
/*
	Handle			- rsampaths16
	Problem			-
	Complexity		-
	Description		-
	Judge			-
*/

/*======================!!-Code-Starts-From-Here-!!======================*/
const int N = 1000006; // Default 10^6
const int M = 2*N;

int n;
double d;
vector<double> k,s;
int main(int argc,char *argv[]) {
	Nitro();//	openup;closeup;
	int T;
	cin >> T;
	for(int t=1; t<=T; t++) {
		cin >> d >> n;
		k.resize(n);
		s.resize(n);
		double ans = 0x3f3f3f3f3f3f3f3f;
		for(int i=0; i<n; i++) {
			cin >> k[i] >> s[i];
			if(k[i]<=d) ans = min(ans,(d*s[i])/(d-k[i]));
		}
		cout << "Case #" << t << ": ";
		cout << fixed <<  setprecision(10) << ans << endl;
	}
	return 0;
}

/*===========================!!-End-Of-Code-!!===========================*/

/* HINTS
	<(0-9):(A-Z):(a-z)>   <(48-57):(65-90):(97-122)>
	{ a  b  c  d  e  f  g  h  i  j  k  l  m  n  o  p  q  r  s  t  u  v  w  x  y  z }
	{ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 }
	360 DEG = 2*PI RAD => ? DEG = X RAD * (360/2*PI)
	cosine-law : C^2 = A^2 + B^2 - 2AB*cos@C
** USEFUL FUNCTIONS
	__builtin_popcount(n) count number of active bits
	__bulitin_popcountl(n) for long long
	atan2(x,y) : atan(y/x)
*/
