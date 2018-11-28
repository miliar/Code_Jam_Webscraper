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
	int l, r;
	node(){};
	node(int _l, int _r)
	{
		l=_l, r=_r;
	}
	bool operator <(const node &foo) const
	{
		return (r-l)<(foo.r-foo.l);
	}
};

int t, n, k;

inline void solve()
{
	pq<node>heap;
	int ansL=0;
	int ansR=INF;
	heap.push(node(0, n+1));
	for(int i=0; i<k; i++)
	{
		int l=heap.top().l;
		int r=heap.top().r;
		heap.pop();
		if(l==r)
		{
			k++;
			continue;
		}
		int m=(r+l)/2;
		ansL=max(abs(m-r)-1, abs(m-l)-1);
		ansR=min(abs(m-r)-1, abs(m-l)-1);

		heap.push(node(l, m));
		heap.push(node(m, r));
	}

	printf("Case #%d: %d %d\n", t, ansL, ansR);
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
	rd(n), rd(k);
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
	}
	
	return 0;
}