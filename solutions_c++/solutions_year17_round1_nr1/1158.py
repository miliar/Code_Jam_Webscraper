#include <bits/stdc++.h>

#define rep(i,n) for(i=1;i<=n;i++)
#define Rep(i,n) for(i=0;i<n;i++)
#define For(i,a,b) for(i=a;i<=b;i++)

#define pb(x) push_back(x)
#define sz(x) x.size()

#define mem(ara,val) memset(ara,val,sizeof(ara))
#define eps 1e-9

#define si(x) scanf("%d",&x)
#define sii(x,y) scanf("%d %d",&x,&y)
#define siii(x,y,z) scanf("%d %d %d",&x,&y,&z)
#define sl(x) scanf("%lld",&x)
#define sll(x,y) scanf("%lld %lld",&x,&y)
#define slll(x,y,z) scanf("%lld %lld %lld",&x,&y,&z)
#define ss(ch) scanf("%s",ch)
#define pi(x) printf("%d",x)
#define pii(x,y) printf("%d %d",x,y)
#define piii(x,y,z) printf("%d %d %d",x,y,z)
#define pl(x) printf("%lld",x)
#define pll(x,y) printf("%lld %lld",x,y)
#define plll(x,y,z) printf("%lld %lld %lld",x,y,z)
#define ps(ch) printf("%s",ch)
#define Afridi 0
#define NL printf("\n")
#define debug(x) printf("wow  %d !!\n",x)
#define Max 100005
#define INF (LL)1e15
#define mod 100003
#define FI freopen("in.txt","r",stdin)
#define FO freopen("out.txt","w",stdout)
#define D(x) cout << #x << " = " << x << endl
#define DD(x,y) cout << #x << " = " << x << "   " << #y << " = " << y << endl
#define RTE __builtin_trap()
#define FI(str) freopen(str,"r",stdin)
#define FO(str) freopen(str,"w",stdout)

const double PI = acos( -1.0 );

typedef long long LL;
typedef unsigned long long ULL;

using namespace std;

LL bigmod(LL b,LL p)
{
    if(p == 0)return 1;
    LL my = bigmod(b,p/2);
    my*=my;
    my%=mod;
    if(p & 1)my*=b,my%=mod;
    return my;
}
int setb(int n,int pos){return n=n | (1 << pos);}
int resb(int n,int pos){return n=n & ~(1 << pos);}
bool checkb(int n,int pos){return (bool)(n & (1 << pos)); }

int n,m;
char str[30][30];
bool fnd[30],shit[30];
int border[30][4];

void prework()
{
	mem(fnd,0);
	mem(shit,0);
	for(int k = 0; k < 26; k++)
	{
		bool flag = 0;
		for(int i = 0; i < n; i++)
		{
			for(int j = 0; j < m; j++)
			{
				if( str[i][j] == ('A' + k) )flag = 1;
			}
		}
		fnd[k] = flag;
		shit[k] = flag;
		if( flag )
		{
			int u = 100,d = -100,l = 100,r = -100;
			for(int i = 0; i < n; i++)
			{
				for(int j = 0; j < m; j++)
				{
					if( str[i][j] == ('A' + k) )
					{
						u = min(u,i);
						d = max(d,i);
						l = min(l,j);
						r = max(r,j);
					}
				}
			}
			border[k][0] = u;
			border[k][1] = d;
			border[k][2] = l;
			border[k][3] = r;
			//DD(u,d);
			//DD(l,r);
			for(int i = u; i <= d; i++)
			{
				for(int j = l; j <= r; j++)str[i][j] = 'A' + k;
			}
		}
	}
}

bool oka(int x,int y)
{
	if( x < 0 || x >= n )return 0;
	if( y < 0 || y >= m )return 0;
	if( str[x][y] != '?' )return 0;
	return 1;
}

void F()
{
	for(int k = 0; k < 26; k++)
	{
		if( fnd[k] )
		{
			while( 1 )
			{
				int u = border[k][0];
				int d = border[k][1];
				int l = border[k][2];
				int r = border[k][3];
				int f;
				///up
				f = 1;
				for(int j = l; j <= r; j++)
				{
					if( oka(u-1,j) == 0 )
					{
						f = 0;
						break;
					}
				}
				if( f )
				{
					for(int j = l; j <= r; j++)
					{
						str[u-1][j] = 'A' + k;
					}
					border[k][0] = u - 1;
					continue;
				}

				///down
				f = 1;
				for(int j = l; j <= r; j++)
				{
					if( oka(d+1,j) == 0 )
					{
						f = 0;
						break;
					}
				}
				if( f )
				{
					for(int j = l; j <= r; j++)
					{
						str[d+1][j] = 'A' + k;
					}
					border[k][1] = d + 1;
					continue;
				}

				///left
				f = 1;
				for(int i = u; i <= d; i++)
				{
					if( oka(i,l-1) == 0 )
					{
						f = 0;
						break;
					}
				}
				if( f )
				{
					for(int i = u; i <= d; i++)
					{
						str[i][l-1] = 'A' + k;
					}
					border[k][2] = l - 1;
					continue;
				}

				///right
				f = 1;
				for(int i = u; i <= d; i++)
				{
					if( oka(i,r+1) == 0 )
					{
						f = 0;
						break;
					}
				}
				if( f )
				{
					for(int i = u; i <= d; i++)
					{
						str[i][r+1] = 'A' + k;
					}
					border[k][3] = r + 1;
					continue;
				}
				break;
			}
		}
	}
}

bool check()
{
	mem(fnd,0);
	for(int k = 0; k < 26; k++)
	{
		int flag = 0;
		for(int i = 0; i < n; i++)
		{
			for(int j = 0; j < m; j++)
			{
				if( str[i][j] == ('A' + k) )flag = 1;
			}
		}
		if( flag )
		{
			int u = 100,d = -100,l = 100,r = -100;
			for(int i = 0; i < n; i++)
			{
				for(int j = 0; j < m; j++)
				{
					if( str[i][j] == ('A' + k) )
					{
						u = min(u,i);
						d = max(d,i);
						l = min(l,j);
						r = max(r,j);
					}
				}
			}
			for(int i = u; i <= d; i++)
			{
				for(int j = l; j <= r; j++)
				{
					if( str[i][j] != ('A'+k) )return 0;
					//assert(str[i][j] == ('A'+k));
				}
			}
		}
	}
	for(int i = 0; i < n; i++)
	{
		for(int j = 0; j < m; j++)
		{
			if( str[i][j] == '?' )return 0;
			//assert( str[i][j] != '?' );
		}
	}

	return 1;
}

void Fuck()
{
	char tmp[30][30];

	for(int i = 0; i < n; i++)
	{
		for(int j = 0; j < m; j++)
		{
			tmp[i][j] = str[i][j];
		}
	}
	for(int i = 0; i < n; i++)
	{
		int lst = -1;
		for(int j = 0; j < m; j++)
		{
			if( str[i][j] != '?' )
			{
				char c = str[i][j];
				for(int k = lst + 1; k <= j; k++)
				{
					str[i][k] = c;
				}
				lst = j;
			}
		}
	}

	for(int i = 0; i < n; i++)
	{
		int lst = m;
		for(int j = m-1; j >= 0; j--)
		{
			if( str[i][j] != '?' )
			{
				char c = str[i][j];
				for(int k = lst - 1; k >= j; k--)
				{
					str[i][k] = c;
				}
				lst = j;
			}
		}
	}

	for(int i = 1; i < n; i++)
	{
		int f = 0;
		for(int j = 0; j < m; j++)if( str[i][j] == '?' )f = 1;
		if(f)for(int j = 0; j < m; j++)str[i][j] = str[i-1][j];
	}
	for(int i = n-2; i >= 0; i--)
	{
		int f = 0;
		for(int j = 0; j < m; j++)if( str[i][j] == '?' )f = 1;
		if(f)for(int j = 0; j < m; j++)str[i][j] = str[i+1][j];
	}
}

int main()
{
	//freopen("in.txt","r",stdin);
	freopen("A-large.in","r",stdin);
	freopen("Alarge.txt","w",stdout);
	int t,T,i,j;
    si(T);
    rep(t,T)
    {
		sii(n,m);
		Rep(i,n)ss(str[i]);
		//Rep(i,n)puts(str[i]);
		//prework();
		//F();
		Fuck();
		printf("Case #%d:\n",t);
		Rep(i,n)puts(str[i]);
		bool f = check();
		//printf("check %d\n",f);
		assert(f);
		//puts("--------");
	}
	return 0;
}
