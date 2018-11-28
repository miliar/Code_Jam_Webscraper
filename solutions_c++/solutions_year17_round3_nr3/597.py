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
#define EPS (double)1e-6
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

const int MN=55;
int n, k;
double x;
double data[MN];

inline bool f()
{
	for(int i=0; i<n; i++)
		for(int j=0; j<n; j++)
			if(fabs(data[i]-data[j])>EPS)
				return true;
	return false;
}

inline bool g()
{
	for(int i=0; i<n; i++)
		if(fabs(1.0L-data[i])>EPS)
			return true;
	return false;
}

inline void solve()
{
	if(n==1)
	{
		if(data[0]+x>=1.000000L)
			data[0]=1.0L;
		else
			data[0]+=x;
		printf("%.10f\n", data[0]);
		return;
	}

	while(x>EPS && f() && g())
	{
		sort(data, data+n);
		int cnt=0;
		for(int i=0; i<n; i++)
			if(fabs(data[0]-data[i])<EPS)
				cnt++;
		double y=0.0;
		for(int i=1; i<n; i++)
			if(fabs(data[0]-data[i])>EPS)
			{
				y=fabs(data[0]-data[i]);
				break;
			}
		if(cnt*y<=x)
		{
			for(int i=0; i<cnt; i++)
				data[i]+=y;
			x-=(cnt*y);
		}
		else
		{
			y=x/(1.0L*cnt);
			for(int i=0; i<cnt; i++)
				data[i]+=y;
			x=0;
			break;
		}
	}
	double ans=1.0L;
	double y=0;
	if(!f())
		y=(x/(1.0L*n));
	for(int i=0; i<n; i++)
	{
		if(data[i]+y>=1.000000L)
			data[i]=1.0L;
		else
			data[i]+=y;
		//printf("%g\n", data[i]);
		ans*=(data[i]);
	}
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
		scanf("%lf", &x);
		for(int i=0; i<n; i++)
			scanf("%lf", &data[i]);
		printf("Case #%d: ", t);
		solve();
	}
	
	return 0;
}