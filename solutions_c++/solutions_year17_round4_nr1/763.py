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

const int MN=100+1;
int n, p;
int data[4];

int dp[MN][MN][MN][4];
bool memo[MN][MN][MN][4];
//1, 2, 3
int solve(int a, int b, int c, int r)
{
	if((a+b+c)==0)
		return 0;
	if(memo[a][b][c][r])
		return dp[a][b][c][r];
	int &ret=dp[a][b][c][r]=0;
	if(r==0)
	{
		if(a)
			ret=max(ret, 1+solve(a-1, c, b, 1));
		if(b && p>2)
			ret=max(ret, 1+solve(a, b-1, c, 2));
		if(c && p>3)
			ret=max(ret, 1+solve(a, b, c-1, 3));
	}
	else
	{
		if(a)
			ret=max(ret, solve(a-1, b, c, (r+1)%p));
		if(b && p>2)
			ret=max(ret, solve(a, b-1, c, (r+2)%p));
		if(c && p>3)
			ret=max(ret, solve(a, b, c-1, (r+3)%p));
	}
	memo[a][b][c][r]=true;
	return ret;
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
		rd(n), rd(p);
		SET(data, 0);
		for(int i=0; i<n; i++)
		{
			int x;
			rd(x);
			data[x%p]++;
		}
		SET(memo, false);
		printf("Case #%d: %d\n", t, data[0]+solve(data[1], data[2], data[3], 0));
	}
	return 0;
}