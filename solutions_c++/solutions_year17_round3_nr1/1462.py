/* 
	Pranshul Agarwal
	B.tech CSE Graduate
	MNNIT Allahabad
*/


#include <algorithm>
#include <cmath>
#include <climits> 
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <iostream> 
#include <limits>
#include <map> 
#include <queue>
#include <set>
#include <stack>
#include <string>  
#include <utility>   
#include <vector> 
//#include <sys/resource.h>

using namespace std;

typedef unsigned long long ull;
typedef long long ll;
typedef pair< int ,int > ii;
typedef vector < int > vi;
typedef vector < ii > vii;
typedef vector < ll > vll;

#define TRACE
 
#ifdef TRACE
#define db1(x) cerr << #x << ": " << x << endl;
#define db2(x, y) cerr << #x << ": " << x << " | " << #y << ": " << y << endl;
#define db3(x, y, z) cerr << #x << ": " << x << " | " << #y << ": " << y << " | " << #z << ": " << z << endl;
#define db4(a, b, c, d) cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << endl;
#define db5(a, b, c, d, e) cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << " | " << #e << ": " << e << endl;
#define db6(a, b, c, d, e, f) cerr << #a << ": " << a << " | " << #b << ": " << b << " | " << #c << ": " << c << " | " << #d << ": " << d << " | " << #e << ": " << e << " | " << #f << ": " << f << endl;
 
#else
 
#define db1(x)
#define db2(x, y)
#define db3(x, y, z)
#define db4(a, b, c, d)
#define db5(a, b, c, d, e)
#define db6(a, b, c, d, e, f)
 
#endif

#define tr(container , it) for(typeof(container.begin()) it=container.begin() ; it!=container.end() ; it++)

#define MS(A) memset(A, 0, sizeof(A))
#define MSV(A,a) memset(A, a, sizeof(A))

#define ESP (1e-9)
#define MOD 1000000007

#define chkbit(s, b) (s & (1<<b))
#define setbit(s, b) (s |= (1<<b))
#define clrbit(s, b) (s &= ~(1<<b))

#define found(A, x) (A.find(x) != A.end()) 
#define pb push_back
#define mp make_pair
#define X first
#define Y second
#define sz size()
#define ln length()


#define inc(i,a,n) for(int i=a;i<=n;i++)
#define dec(i,n,a) for(int i=n;i>=a;i--)
#define all(a)  a.begin(),a.end() 

#define in(n) scanf("%d",&n)
#define in2(n,m) scanf("%d%d",&n,&m)
#define inll(n) scanf("%lld",&n)
#define in2ll(n,m) scanf("%lld%lld",&n,&m)
#define ins(s) scanf("%s",s)

#define out(n) printf("%d\n",n)
#define outll(n) printf("%lld\n",n)
#define out2(n,m) printf("%d %d\n",n,m)
#define out2ll(n,m) printf("%lld %lld\n",n,m)
#define outs(s) printf("%s\n",s)

#define imax numeric_limits<int>::max()
#define imin numeric_limits<int>::min()
#define lmax numeric_limits<ll>::max()
#define lmin numeric_limits<ll>::min()
/*
int abs(int x) {if(x < 0) return -x; return x;}

long long gcd(long long a,long long b)
{
	while(b)
		b^=a^=b^=a%=b;
	return a;
}
long long int power(long long int b,long long int e)
{
	long long ans=1,temp;
	while(e>0)
	{
		if(e%2)
			ans=(ans*b)%MOD;
		b=(b*b)%MOD;
		e/=2;
	}
	return ans;
}
void increase_stack_depth()			// works on codechef
{
	rlimit R;
	getrlimit(RLIMIT_STACK, &R);
	R.rlim_cur = R.rlim_max;
	setrlimit(RLIMIT_STACK, &R);
}
*/
#define gc getchar//_unlocked

void scanint(int &x)
{
    register int c = gc();
    x = 0;
    int neg = 0;
    for(;((c<48 || c>57) && c != '-');c = gc());
    if(c=='-') {neg=1;c=gc();}
    for(;c>47 && c<58;c = gc()) {x = (x<<1) + (x<<3) + c - 48;}
    if(neg) x=-x;
}
#define pc(x) putchar//_unlocked(x);

inline void writeInt (int n)
{
	int N = n, rev, count = 0;
	rev = N;
	if (N == 0) { pc('0'); pc('\n'); return ;}
	while ((rev % 10) == 0) { count++; rev /= 10;}
	rev = 0;
	while (N != 0) { rev = (rev<<3) + (rev<<1) + N % 10; N /= 10;}
	while (rev != 0) { pc(rev % 10 + '0'); rev /= 10;}
	while (count--) pc('0');
} 
int main()
{
	int t;
	ll n,k,m,r,h,cur,c;
	ll ans;
	vector<pair<ll,pair<ll,ll> > > ar;
	in(t);
	inc(d,1,t)
	{
		ar.clear();
		in2ll(n,k);
		inc(i,0,n-1){
			in2ll(r,h);
			ar.pb(mp(2LL*r*h,mp(h,r)));
		}
		sort(ar.rbegin(),ar.rend());
		ans  = 0;
		inc(i,0,n-1){
			r = ar[i].Y.Y;
			c = 1;
			cur = r*r + ar[i].X;
			ans = max(cur,ans);
			inc(j,0,n-1){
				if(j != i && ar[j].Y.Y <= r){
					c++;
					cur += ar[j].X;
					if(c == k){
						ans = max(ans,cur);
						break;
					}
				}
			}
		}
		printf("Case #%d: %.10lf\n",d,acos(-1)*ans);
	}
	return 0;
}