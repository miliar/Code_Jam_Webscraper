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

LL n,m,dick[10][10],ara[10],lol[10];

int main()
{
	//freopen("in.txt","r",stdin);
	freopen("B-small-attempt0.in","r",stdin);
	freopen("Bsmall.txt","w",stdout);
	LL t,T,i,j;
    sl(T);
    rep(t,T)
    {
		sll(n,m);
		Rep(i,n)sl(ara[i]);
		Rep(i,m)lol[i] = i;
		Rep(i,n)
		{
			Rep(j,m)sl(dick[i][j]);
		}
		LL ret = 0;
		if( n == 1 )
		{
			Rep(i,m)
			{
				LL x = dick[0][i];
				LL mnx = 10 * x / (9 * ara[0]);
				LL mxx = 10 * x / (11 * ara[0]);
				if( (10*x) % (11*ara[0]) )mxx++;
				//DD(mnx,mxx);
				if( mnx >= mxx && mxx > 0 )ret++;
			}
		}
		else
		{
			while( 1 )
			{
				LL cnt = 0;
				Rep(i,m)
				{
					LL my = lol[i];
					LL x = dick[0][i];
					LL y = dick[1][my];
					//DD(x,y);

					///x
					LL mnx = 10 * x / (9 * ara[0]);
					LL mxx = 10 * x / (11 * ara[0]);
					if( (10*x) % (11*ara[0]) )mxx++;
					//DD(mnx,mxx);
					///y
					LL mny = 10 * y / (9 * ara[1]);
					LL mxy = 10 * y / (11 * ara[1]);
					if( (10*y) % (11*ara[1]) )mxy++;
					//DD(mny,mxy);


					LL mn = min(mnx,mny);
					LL mx = max(mxx,mxy);

					if( mn >= mx && mx > 0 )cnt++;
				}
				ret = max( ret , cnt );
				bool f = next_permutation( lol, lol+m );
				if(!f)break;
			}
		}
		printf("Case #%lld: %lld\n",t,ret);
	}
	return 0;
}
