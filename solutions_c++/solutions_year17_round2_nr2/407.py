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

	//freopen("","r",stdin);
	//freopen("","w",stdout);

int setb(int n,int pos){return n=n | (1 << pos);}
int resb(int n,int pos){return n=n & ~(1 << pos);}
bool checkb(int n,int pos){return (bool)(n & (1 << pos)); }

LL ara[1000005];
LL r,o,y,g,b,v,n;
LL meaning[3],flag;

LL F()
{
	LL cur = 1;
	while( r-- )
	{
		if( ara[cur] != -1 )
		{
			flag = 0;
			break;
		}
		ara[cur] = 0;
		cur += 2;
		if( cur > n )cur -= n;
	}

	cur--;
	if(cur == 0)cur = n;
	if( ara[cur] != -1 )flag = 0;

	if( b >= y )
	{
		while( b-- )
		{
			if( ara[cur] != -1 )
			{
				flag = 0;
				break;
			}
			ara[cur] = 1;
			cur++;
			if(cur > n)cur = 1;
			if( ara[cur] != -1 )break;
			else if( y )
			{
				y--;
				ara[cur] = 2;
			}
			cur++;
			if(cur > n)cur = 1;
			if( ara[cur] != -1 )break;
		}
		LL i;
		rep(i,n)
		{
			if( ara[i] == -1 )
			{
				if( b )
				{
					b--;
					ara[i] = 1;
				}
				else if( y )
				{
					y--;
					ara[i] = 2;
				}
			}
		}
	}
	else
	{
		while( y-- )
		{
			if( ara[cur] != -1 )
			{
				flag = 0;
				break;
			}
			ara[cur] = 2;
			cur++;
			if(cur > n)cur = 1;
			if( ara[cur] != -1 )break;
			else if( b )
			{
				b--;
				ara[cur] = 1;
			}
			cur++;
			if(cur > n)cur = 1;
			if( ara[cur] != -1 )break;
		}
		LL i;
		rep(i,n)
		{
			if( ara[i] == -1 )
			{
				if( b )
				{
					b--;
					ara[i] = 1;
				}
				else if( y )
				{
					y--;
					ara[i] = 2;
				}
			}
		}
	}
}

bool oka()
{
	LL j;
	//rep(j,n)printf("%lld ",ara[j]);
	//NL;
	rep(j,n)if(ara[j] == -1)return 0;
	rep(j,n)
	{
		LL i = j - 1;
		if(i == 0)i = n;
		LL k = j + 1;
		if(k > n)k = 1;
		if( ara[i] == ara[j] || ara[j] == ara[k] )return 0;
	}
	return 1;
}

int main()
{
	//freopen("in.txt","r",stdin);
	freopen("B-small-attempt0.in","r",stdin);
	freopen("bsmallout.txt","w",stdout);

	LL t,T,i,j;
	sl(T);
	rep(t,T)
	{
		sl(n);
		slll(r,o,y);
		slll(g,b,v);
		rep(i,n)ara[i] = -1;
		flag = 1;
		meaning[0] = 0;
		meaning[1] = 1;
		meaning[2] = 2;
		if( r == max( r , max(y,b) ) )
		{
			F();
		}
		else if( b == max( b , max(r,y) ) )
		{
			swap(b,r);
			swap(meaning[0],meaning[1]);
			F();
		}
		else
		{
			swap(y,r);
			swap(meaning[0],meaning[2]);
			F();
		}
		if( oka() == 0 )flag = 0;
		printf("Case #%lld: ",t);
		if( flag )
		{
			rep(i,n)
			{
				LL val = meaning[ ara[i] ];
				if(val == 0)printf("R");
				if(val == 1)printf("B");
				if(val == 2)printf("Y");
			}
			NL;
		}
		else puts("IMPOSSIBLE");
	}
	return 0;
}
