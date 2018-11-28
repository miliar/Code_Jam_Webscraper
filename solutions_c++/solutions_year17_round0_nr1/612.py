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

char str[Max];
LL ara[Max],n,k;

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("Alarge.txt","w",stdout);
	LL t,T,i,j;
	sl(T);
	rep(t,T)
	{
		ss(str);
		sl(k);
		n = strlen(str);
		Rep(i,n)
		{
			if(str[i] == '+')ara[i] = 1;
			else ara[i] = 0;
		}
		LL flag = 1,cnt = 0;
		for(i=0;i<n-k+1;i++)
		{
			if( ara[i] == 0 )
			{
				cnt++;
				for(j = i; j < i + k; j++ )ara[j] = 1 - ara[j];
			}
		}
		Rep(i,n)
		{
			if(ara[i] == 0)flag = 0;
		}
		printf("Case #%lld: ",t);
		if(flag == 0)puts("IMPOSSIBLE");
		else printf("%lld\n",cnt);
	}
	return 0;
}
