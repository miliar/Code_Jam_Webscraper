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

const int MN=1500;
int n, m;
int data[2][MN];

bool memo[MN][MN][2][2];
int dp[MN][MN][2][2];
int solve(int i, int c, int k, int s)
{
	if(i==1440)
		return c==720?s!=k:INF;
	if(memo[i][c][k][s])
		return dp[i][c][k][s];
	int &ret=dp[i][c][k][s]=INF;
	if(k)
	{
		if(data[k][i])
		{
			if(c-1>=0)
				ret=min(ret, 1+solve(i+1, c-1, k^1, s));
		}
		else if(data[k^1][i])
		{
			if(c+1<=1440)
				ret=min(ret, solve(i+1, c+1, k, s));
		}
		else
		{
			if(c-1>=0)
				ret=min(ret, 1+solve(i+1, c-1, k^1, s));
			if(c+1<=1440)
				ret=min(ret, solve(i+1, c+1, k, s));
		}
	}
	else
	{
		if(data[k][i])
		{
			if(c+1<=1440)
				ret=min(ret, 1+solve(i+1, c+1, k^1, s));
		}
		else if(data[k^1][i])
		{
			if(c-1>=0)
				ret=min(ret, solve(i+1, c-1, k, s));
		}
		else
		{
			if(c+1<=1440)
				ret=min(ret, 1+solve(i+1, c+1, k^1, s));
			if(c-1>=0)
				ret=min(ret, solve(i+1, c-1, k, s));
		}
	}
	memo[i][c][k][s]=true;
	return ret;
}

inline void solve()
{
	SET(memo, false);
	int ans;
	if(data[0][0])
		ans=solve(0, 720, 1, 1);
	else if(data[1][0])
		ans=solve(0, 720, 0, 0);
	else
		ans=min(ans, min(solve(0, 720, 0, 0), solve(0, 720, 1, 1)));
	printf("%d\n", ans);
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
		SET(data, 0);
		rd(n), rd(m);
		for(int i=0; i<n; i++)
		{
			int l, r;
			rd(l), rd(r);
			for(int j=l; j<r; j++)
				data[0][j]=1;
		}
		for(int i=0; i<m; i++)
		{
			int l, r;
			rd(l), rd(r);
			for(int j=l; j<r; j++)
				data[1][j]=1;
		}
		printf("Case #%d: ", t);
		solve();
	}
	return 0;
}