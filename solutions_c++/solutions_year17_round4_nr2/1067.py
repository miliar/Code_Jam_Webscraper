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
#define mod 100003
#define FI freopen("in.txt","r",stdin)
#define FO freopen("out.txt","w",stdout)
#define D(x) cout << #x << " = " << x << endl
#define DD(x,y) cout << #x << " = " << x << "  " << #y << " = " << y << endl
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

LL ara[2][1005];
LL item[3][1005];
bool visit[2][1005];
vector <LL> v[1005];
LL n,m,c;

int main()
{
	//freopen("in.txt","r",stdin);
	freopen("B-small-attempt1.in","r",stdin);
	freopen("bsmall2.txt","w",stdout);
	LL t,T,i,j,r,man;
	sl(T);
	rep(t,T)
	{
		slll(n,c,m);
		rep(i,c)v[i].clear();
		mem(item,0);
		rep(i,m)
		{
			sll(r,man);
			item[man][r]++;
		}
		LL ret = 0,pr = 0;
		if( c == 2 )
		{
			LL mx = 0, id;
			LL bad = 0;
			rep(i,n)
			{
				if( item[1][i] && item[2][i] )
				{
					LL mn = min( item[1][i] , item[2][i] );
					mx = max( mx , mn );
					if( mx == mn )id = i;
					item[1][i] -= mn;
					item[2][i] -= mn;
					bad += mn;
				}
			}
			LL rm1 = 0,rm2 = 0;
			rep(i,n)
			{
				rm1 += item[1][i];
				rm2 += item[2][i];
			}

			if( bad == 0 )
			{
				ret += max( rm1 , rm2 );
			}
			else
			{
				if( 2 * mx <= bad )
				{
					ret += bad;
					ret += max( rm1 , rm2 );
				}
				else
				{
					LL baki = bad - mx;
					ret += baki * 2;
					mx -= baki;
					item[1][id] += mx;
					item[2][id] += mx;
					rm1 += mx;
					rm2 += mx;

					LL same1 = item[1][id];
					LL same2 = item[2][id];
					LL oth1 = rm1 - same1;
					LL oth2 = rm2 - same2;


					LL my;
					my = min( same1 , oth2 );
					same1 -= my;
					oth2 -= my;
					ret += my;
					rm1 -= my;
					rm2 -= my;

					my = min( same2 , oth1 );
					same2 -= my;
					oth1 -= my;
					ret += my;
					rm1 -= my;
					rm2 -= my;

					LL l = 0;
					if( same1 )l++;
					if( same2 )l++;
					if( oth1 )l++;
					if( oth2 )l++;
					assert( l < 3 );
					if( l == 1 )
					{
						if( same1 )ret += same1;
						if( same2 )ret += same2;
						if( oth1 )ret += oth1;
						if( oth2 )ret += oth2;
					}
					else if( l == 2 )
					{
						if( same1 && same2 )
						{
							if( id == 1 )
							{
								ret += ( same1 + same2 );
							}
							else
							{
								ret += max( same1 , same2 );
								pr += min( same1 , same2 );
							}
						}
						else if( oth1 && oth2 )
						{
							ret += max( oth1 , oth2 );
						}
						else if( same1 && oth1 )ret += ( same1 + oth1 );
						else if( same2 && oth2 )ret += ( same2 + oth2 );
					}
				}
			}
		}
		printf("Case #%lld: %lld %lld\n",t,ret,pr);
	}
	return 0;
}

