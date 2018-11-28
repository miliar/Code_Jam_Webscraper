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
#define Max 1000005
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


LL n,k;
struct info
{
	LL val,cnt;
	info() {}
	info(LL _val, LL _cnt) { val = _val; cnt = _cnt; }
};
queue <info> q;

LL mn2,mx2;
void Find_place_small_2()
{
    while( q.empty() == 0 )q.pop();
    q.push( info(n,1) );

	LL tot = 0;
    while( q.empty() == 0 )
    {
		info my = q.front();
		q.pop();
		while( q.empty() == 0 )
		{
			info tmp = q.front();
			if( tmp.val == my.val )
			{
				my.cnt += tmp.cnt;
				q.pop();
			}
			else break;
		}
		tot += my.cnt;
		LL val = my.val - 1;
		if( val < 0 )continue;
		LL a = val / 2;
		LL b = (val + 1) / 2;
		if( tot >= k )
		{
			mn2 = a;
			mx2 = b;
			return;
		}
		if( a == b )
		{
			q.push( info(a,my.cnt*2) );
		}
		else
		{
			q.push( info(b,my.cnt) );
			q.push( info(a,my.cnt) );
		}
    }
}

int main()
{
	//freopen("in.txt","w",stdout);
	//pl(1024ll*1024*1024*1024*1024);
	//FI;
	freopen("C-large.in","r",stdin);
	freopen("Clarge.txt","w",stdout);
	//return 0;
	LL t,T,i,j;
	sl(T);
	rep(t,T)
	{
		//n = 1125899906842624 - 1000 + t;
		//k = 1125899906842624 - 100000 + t;
		sll(n,k);
		printf("Case #%lld: ",t);
		Find_place_small_2();
		printf("%lld %lld\n",mx2,mn2);
	}
	return 0;
}
