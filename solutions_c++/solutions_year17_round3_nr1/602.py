/// David Mateus Batista <david.batista3010@gmail.com>
/// Computer Science - Federal University of Itajuba - Brazil

#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;

#define INF 0x3F3F3F3F
#define LINF 0x3F3F3F3F3F3F3F3FLL
#define DINF (double)1e+30
#define EPS (double)1e-9
#define PI (double)acos(-1.0)
#define RAD(x) (double)(x*PI)/180.0
#define PCT(x,y) (double)x*100.0/y

#define pb push_back
#define mp make_pair
#define pq priority_queue
#define F first
#define S second

#define D(x) x&(-x)
#define SZ(x) (int)x.size()
#define ALL(x) x.begin(),x.end()
#define SET(a,b) memset(a, b, sizeof(a))

#define gcd(x,y) __gcd(x, y)
#define lcm(x,y) (x/gcd(x,y))*y

#define bitcnt(x) __builtin_popcountll(x)
#define lbit(x) 63-__builtin_clzll(x)
#define zerosbitll(x) __builtin_ctzll(x)
#define zerosbit(x) __builtin_ctz(x)

enum {North, East, South, West};
//{0, 1, 2, 3}
//{Up, Right, Down, Left}

int mi[] = {-1, 0, 1, 0, -1, 1, 1, -1};
int mj[] = {0, 1, 0, -1, 1, 1, -1, -1};

class node
{
public:
	ll r, h;
	node(){};
	node(ll _r, ll _h)
	{
		r=_r, h=_h;
	}
	bool operator <(const node &foo) const
	{
		if(r!=foo.r)
			return r>foo.r;
		return h>foo.h;
	}
};



const int MN=1e+3+35;
int n, k;
node data[MN];

bool memo[MN][MN];
double dp[MN][MN];

double getValue(int i)
{
	return 2.0L*PI*(data[i].r*data[i].h);
}

double getValue2(int i)
{
	return PI*(data[i].r*data[i].r);
}

double solve(int i, int c)
{
	if(c>k)
		return -DINF;
	if(c==k)
		return 0;
	if(i==n)
		return c==k?0:-DINF;
	if(memo[i][c])
		return dp[i][c];
	double &ret=dp[i][c]=-DINF;
	ret=max(ret, getValue(i)+solve(i+1, c+1));
	ret=max(ret, solve(i+1, c));
	memo[i][c]=true;
	return ret;
}

inline void solve()
{
	SET(memo, false);
	sort(data, data+n);
	double ans=-DINF;
	for(int i=0; i<n; i++)
		ans=max(ans, getValue(i)+getValue2(i)+solve(i+1, 1));
	printf("%.10f\n", ans);
}

template<class num>inline void rd(num &x)
{
	char c;
	while(isspace(c = getchar()));
	bool neg = false;
	if(!isdigit(c))
		neg=(c=='-'), x=0;
	else
		x=c-'0';
	while(isdigit(c=getchar()))
		x=(x<<3)+(x<<1)+c-'0';
	if(neg)
		x=-x;
}
	
int main()
{
	#ifdef LOCAL_PROJECT
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	#else
	#endif

	int tt;
	rd(tt);
	for(int t=1; t<=tt; t++)
	{
		rd(n), rd(k);
		for(int i=0; i<n; i++)
			rd(data[i].r), rd(data[i].h);
		printf("Case #%d: ", t);
		solve();
	}
	
	return 0;
}