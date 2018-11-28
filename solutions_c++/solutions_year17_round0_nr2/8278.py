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

const int MN=1e+3+35;
int n, t;
char str[50];
ll x;

ll dp[50][2][15];
bool memo[50][2][15];

ll solve(int i, int t, int l)
{
	if(i==n)
		return t==0;
	if(memo[i][t][l])
		return dp[i][t][l];
	ll &ret=dp[i][t][l]=0;
	if(t)
	{
		for(int j=l; j<=str[i]-'0'; j++)
			ret+=solve(i+1, (j==(str[i]-'0')), j);
	}
	else
	{
		for(int j=l; j<=9; j++)
			ret+=solve(i+1, 0, j);
	}
	memo[i][t][l]=true;
	return ret;
}

inline ll getValue(ll y)
{
	sprintf(str, "%lld", y+1);
	n=strlen(str);
	SET(memo, false);
	return solve(0, 1, 0);
}

inline bool f(ll mid, ll v)
{	
	return getValue(mid)==v;
}

inline bool g(ll y)
{
	int l=9;
	while(y)
	{
		if(y%10>l)
			return false;
		l=y%10;
		y/=10;
	}
	return true;
}

inline void naive()
{
	ll ans=x;
	while(!g(ans))
		ans--;
	printf("Case #%d: %lld\n", t, ans);
}

inline void solve()
{
	ll v=getValue(x);
	ll lo=0, hi=x;
	while(abs(lo-hi)>1)
	{
		ll mid=(lo+hi)>>1;
		if(f(mid, v))
			hi=mid;
		else
			lo=mid;
	}
	printf("Case #%d: %lld\n", t, lo+1);
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

inline void read()
{
	rd(x);
}

void init()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	return;
}

int main()
{
	#ifdef LOCAL_PROJECT
	init();
	#else
	#endif

	int tt;
	rd(tt);
	for(t=1; t<=tt; t++)
	{
		read();
		solve();
		//naive();
	}
	return 0;
}