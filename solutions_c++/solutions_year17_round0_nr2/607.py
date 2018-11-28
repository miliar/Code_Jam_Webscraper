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
#define mod 1000000007
#define FI freopen("in.txt","r",stdin)
#define FO freopen("out.txt","w",stdout)
#define D(x) cout << #x << " = " << x << endl
#define RTE __builtin_trap()

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

char str[100];
LL n,dp[30][3][15],visit[30][3][15],cs;

LL F(LL pos,LL flag,LL last)
{
	if(pos < 0)
	{
		if(flag == 0)return -1;
		else return 0;
	}

	if( visit[pos][flag][last] == cs )return dp[pos][flag][last];

	LL my = str[pos] - '0';
	LL ret = 0;
	if(flag)
	{
		for(LL i = 0; i <= min(my,last); i++)
		{
			LL my = F(pos-1,1,i);
			if(my >= 0)ret = max( ret , i + 10 * my );
		}
		for(LL i = my + 1; i <= last; i++)
		{
			LL my = F(pos-1,0,i);
			if(my >= 0)ret = max( ret , i + 10 * my );
		}
	}
	else
	{
		for(LL i = 0; i <= min(my-1,last); i++)
		{
			LL my = F(pos-1,1,i);
			if(my >= 0)ret = max( ret , i + 10 * my );
		}
		for(LL i = my; i <= last; i++)
		{
			LL my = F(pos-1,0,i);
			if(my >= 0)ret = max( ret , i + 10 * my );
		}
	}

	visit[pos][flag][last] = cs;
	return dp[pos][flag][last] = ret;
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("Blarge.txt","w",stdout);
	LL t,T;
	sl(T);
	rep(t,T)
	{
		ss(str);
		n = strlen(str);
		cs++;
		LL ret = F(n-1,1,9);
		printf("Case #%lld: ",t);
		pl(ret);NL;
	}
	return 0;
}
