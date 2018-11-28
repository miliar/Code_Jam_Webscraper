#include <bits/stdc++.h>
using namespace std;

typedef pair< int, int > PII;
typedef long long LL;
typedef double db;

const LL lInf = ( LL ) 1E16;
const int Inf = 0x23333333;
const int N = 100005;

#define foi( i, x ) for ( auto i=x.begin(); i!=x.end(); ++i )
#define pub( x ) push_back( x )
#define mkp( A, B ) make_pair( A, B )
#define fo( i, x, y ) for ( int i=x; i<y; ++i )
#define fi first
#define se second

double a[N];

void preprocessing()
{
}

void solve()
{

	fill( a, a+ N, 0 );
		int k,n;
		double u;
		scanf("%d%d",&k,&n);
		scanf("%lf",&u);
		for (int i=1;i<=n;i++) {
			scanf("%lf",a+i);
		}
		sort(a+1,a+1+n);
		a[n+1]=1;
		for (int i=1;i<=n;i++) {
			double tmp=(a[i+1]-a[i]);
			if (tmp*i>u) tmp=u/i;
			u-=tmp*i;
			for (int j=1;j<=i;j++) a[j]+=tmp;
		}
		double ans=1;
		for (int i=1;i<=n;i++) ans*=a[i];
		printf("%.8lf\n",ans);
}

int main()
{
	freopen( "c.in", "r", stdin );
	freopen( "c.out", "w", stdout );
	int T;
	scanf( "%d", &T );
	fo ( Case, 0, T )
	{
		preprocessing();
		printf( "Case #%d: ", Case+1 );
		solve();
	}
	return 0;
}

