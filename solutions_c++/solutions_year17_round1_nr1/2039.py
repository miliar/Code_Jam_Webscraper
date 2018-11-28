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

using namespace std::chrono;
class timecheck
{
public:
	high_resolution_clock::time_point t1, t2;
	void start()
	{
		t1 = high_resolution_clock::now();
	}
	void end()
	{
		t2= high_resolution_clock::now();
		duration<double> time_span = duration_cast<duration<double>>(t2 - t1);
		cout << "Time: " << time_span.count() << "s" << endl;
	}
};

const int MN=30;
int t;
int n, m;
char ans[MN][MN];

inline void propagate(int si, int sj)
{
	char x=ans[si][sj];
	for(int j=sj+1; j<m && ans[si][j]=='?'; j++)
		ans[si][j]=x;
	for(int j=sj-1; j>=0 && ans[si][j]=='?'; j--)
		ans[si][j]=x;
}

inline void propagate2(int si, int bi)
{
	for(int j=0; j<m; j++)
		ans[si][j]=ans[bi][j];
}

inline bool valid()
{
	for(int i=0; i<n; i++)
		for(int j=0; j<m; j++)
			if(ans[i][j]=='?')
				return false;
	return true;
}

inline void solve()
{
	for(int i=0; i<n; i++)
	{
		for(int j=0; j<m; j++)
		{
			if(ans[i][j]!='?')
			{
				propagate(i, j);
			}
		}
	}

	queue<pii>bfs;
	for(int i=0; i<n; i++)
	{
		for(int j=0; j<m; j++)
		{
			if(ans[i][j]!='?')
				bfs.push({i, j});
		}
	}
	while(!bfs.empty())
	{
		int i=bfs.front().F;
		int j=bfs.front().S;
		bfs.pop();

		if(i+1<n && ans[i+1][j]=='?')
		{
			propagate2(i+1, i);
			for(int j=0; j<m; j++)
				bfs.push(mp(i+1, j));
		}
		if(i-1>=0 && ans[i-1][j]=='?')
		{
			propagate2(i-1, i);
			for(int j=0; j<m; j++)
				bfs.push(mp(i-1, j));
		}
	}

	printf("Case #%d:\n", t);
	for(int i=0; i<n; i++)
	{
		for(int j=0; j<m; j++)
			printf("%c", ans[i][j]);
		printf("\n");
	}
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
	rd(n), rd(m);
	for(int i=0; i<n; i++)
		for(int j=0; j<m; j++)
			scanf(" %c", &ans[i][j]);
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
	for(t=1; t<=tt; t++)
	{
		read();
		solve();
	}
	
	return 0;
}