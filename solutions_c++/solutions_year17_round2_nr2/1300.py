/*
ID: kfoozminus
TASK:
LANG: C++
*/

#include <bits/stdc++.h>
using namespace std;
//typedefs
/*
typedef long long ll;
typedef unsigned long long ull;
typedef pair <int, int> pii;
typedef pair <int, pii> piii;
typedef vector <int> vi;
typedef vector <ll> vl;
typedef pair <ll, ll> pll;
const double PI = acos(-1);
*/
//typedefs
#define ll long long
#define ull unsigned long long
#define pii pair <int, int>
#define piii pair <int, pii>
#define vi vector <int>
#define vl vector <ll>
#define pll pair <ll, ll> 
#define PI acos(-1)
//defines
#define MP make_pair
#define PB push_back
#define F first
#define S second
#define mem(a, b) memset(a, b, sizeof(a))
#define gcd(a,b) __gcd(a,b)
#define lcm(a,b) (a*(b/gcd(a,b)))
#define sqr(a) ((a)*(a))
#define inf 100000000
#define mod 1000000007
#define mod1 1000000007
#define mod2 1000000009
#define b1 43
#define b2 41
#define EPS 1e-9
//define harmonic(n) 0.57721566490153286l+log(n)
#define nl puts("")
#define odd(n) ((n)&1)
#define even(n) (!((n)&1))
#define vsort(v) sort(v.begin(), v.end())
#define lc (node<<1)
#define rc ((node<<1)|1)
//loop
#define rep(i, n) for(int i = 0; i < n; ++i)
#define REP(i, n) for(int i = 1; i <= n; ++i)
//input
#define si(a) scanf("%d", &a)
#define sii(a, b) scanf("%d%d", &a, &b)
#define siii(a, b, c) scanf("%d%d%d", &a, &b, &c)
#define sl(a) scanf("%lld", &a)
#define sll(a, b) scanf("%lld%lld", &a, &b)
#define slll(a, b, c) scanf("%lld%lld%lld", &a, &b, &c)
#define sd(a) scanf("%lf", &a)
#define sc(a) scanf("%c", &a)
#define sst(a) scanf("%s", a)
inline bool EQ(double a, double b) { return fabs(a-b) < 1e-9; }
//debug
#ifdef kfoozminus

template < typename F, typename S >
ostream& operator << ( ostream& os, const pair< F, S > & p ) {
	return os << "(" << p.first << ", " << p.second << ")";
}

template < typename T >
ostream &operator << ( ostream & os, const vector< T > &v ) {
	os << "{";
	for(auto it = v.begin(); it != v.end(); ++it) {
		if( it != v.begin() ) os << ", ";
		os << *it;
	}
    return os << "}";
}

template < typename T >
ostream &operator << ( ostream & os, const set< T > &v ) {
	os << "[";
	for(auto it = v.begin(); it != v.end(); ++it) {
		if( it != v.begin()) os << ", ";
		os << *it;
	}
    return os << "]";
}

template < typename F, typename S >
ostream &operator << ( ostream & os, const map< F, S > &v ) {
	os << "[";
	for(auto it = v.begin(); it != v.end(); ++it) {
		if( it != v.begin() ) os << ", ";
		os << it -> first << " = " << it -> second ;
	}
    return os << "]";
}

#define dbg(args...) do {cerr << #args << " : "; faltu(args); } while(0)

clock_t tStart = clock();
#define timeStamp dbg("Execution Time: ", (double)(clock() - tStart)/CLOCKS_PER_SEC)

void faltu () { cerr << endl; }

template <typename T>
void faltu( T a[], int n ) {
	for(int i = 0; i < n; ++i) cerr << a[i] << ' ';
	cerr << endl;
}

template <typename T, typename ... hello>
void faltu( T arg, const hello &... rest) { cerr << arg << ' '; faltu(rest...); }

#else
#define dbg(args...)
#endif
/*
ll add(ll a, ll b) {
	ll ret = a+b;
	if(ret >= mod) ret -= mod;
	return ret;
}

ll subtract(ll a, ll b) {
	ll ret = a-b;
	if(ret < 0) ret += mod;
	return ret;
}

ll mult(ll a, ll b) {
	ll ret = a*b;
	if(ret >= mod) ret %= mod;
	return ret;
}

ll bigmod(ll a, ll b) {
	ll ret = 1;
	while(b) {
		if(b&1) ret = mult(ret, a);
		b >>= 1; a = mult(a, a);
	}
	return ret;
}
*/

//ll inverse(ll n) { return bigmod(n, mod-2); }

/*
#define PMX 1000000

int marked[PMX/64 + 2];
vi primes;

#define mark(x) marked[x >> 6] |= (1 << ((x & 63) >> 1))
#define check(x) (marked[x >> 6] & (1 << ((x & 63) >> 1)))

bool isPrime(int x)
{
	return (x > 1) && ((x == 2) || ((x & 1) && (!(check(x)))));
}

void seive(int n)
{
	int i, j;
	for(i = 3; i * i <= n; i += 2) if(!check(i)) for(j = i * i; j <= n; j += i << 1) mark(j);
	primes.PB(2);
	for(i = 3; i <= n; i += 2) if(isPrime(i)) primes.PB(i);
}
*/

//Direction Array 
//int fx[]={1, -1, 0, 0}; int fy[]={0, 0, 1, -1};
//int fx[]={0, 0, 1, -1, -1, 1, -1, 1}; int fy[]={-1, 1, 0, 0, 1, 1, -1, -1};

//bit manipulation
/*
bool checkBit(int n, int i) { return (n&(1<<i)); }
int setBit(int n, int i) { return (n|(1<<i)); }
int resetBit(int n, int i) { return (n&(~(1<<i))); }
*/
//end of template

#define MX 100007

pair<int, char> c[10];

int main () {
#ifdef kfoozminus
//	freopen("in", "r", stdin);
//	freopen("out", "w", stdout);
#endif
	int tc, cs, i, sum, d, n;

	scanf("%d", &tc);
	for(cs = 1; cs <= tc; cs ++) {
		scanf("%d", &n);
		for(i =  0; i < 6; i ++) {
			scanf("%d", &c[i].F);
		}
		printf("Case #%d: ", cs);
		c[0].S = 'R';
		c[1].S = 'O';
		c[2].S = 'Y';
		c[3].S = 'G';
		c[4].S = 'B';
		c[5].S = 'V';
		sort(c, c + 6);
		sum = c[3].F + c[4].F;
		if(c[5].F > c[3].F + c[4].F) printf("IMPOSSIBLE\n");
		else {
			d = sum - c[5].F;
			c[4].F -= d;
			for(i = 1; i <= c[5].F; i ++) {
				printf("%c", c[5].S);
				if(d == 0 && c[3].F == 0) {
					if(c[4].F > 0) {
						printf("%c", c[4].S);
						c[4].F --;
					}
				}
				if(c[3].F > 0) {
					printf("%c", c[3].S);
					c[3].F --;
				}
				if(d > 0) {
					printf("%c", c[4].S);
					d --;
				}
				
			}
			nl;
		}
	}

//	timeStamp;
	return 0;
}

