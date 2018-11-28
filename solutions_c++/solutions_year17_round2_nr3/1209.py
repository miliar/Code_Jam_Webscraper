#include<bits/stdc++.h>
using namespace std;
#define pc putchar_unlocked
#define gc getchar_unlocked
typedef long long ll;
typedef unsigned long long llu;
#define mp make_pair
#define pb push_back
#define sc(x) scanf("%d",&x)
#define sc2(x,y) scanf("%d%d",&x,&y)
#define sc3(x,y,z) scanf("%d%d%d",&x,&y,&z)
#define scl(x) scanf("%lld",&x)
#define scl2(x,y) scanf("%lld%lld",&x,&y)
#define scl3(x,y,z) scanf("%lld%lld%lld",&x,&y,&z)
#define scstr(x) scanf("%s",x)
#define pd(x) printf("%d",x)
#define pstr(x) printf("%s",x)
#define newl() printf("\n")
#define fl(i,n) for (i=0;i<n;i++)
#define fle(i,n) for (i=1;i<=n;i++)
#define fla(i,a,n) for (i=a;i<n;i++)
#define mem(a,i) memset(a,i,sizeof(a))
#define fi first
#define se second
typedef pair<int,int> pii;
typedef pair<int,pair<int,int> > piii ;
typedef pair<ll,ll> pll;
typedef pair<ll,int> pli;
#define gcd __gcd
#define wl(n) while (n--)
#define debug(x) cerr<<"debug->"<<#x<<"::"<<x<<endl
#define debug2(x,y) cerr<<#x<<" :: "<<x<<"\t"<<#y<<" :: "<<y<<"\n"
#define debug3(x,y,z) cerr<<#x<<" :: "<<x<<"\t"<<#y<<" :: "<<y<<"\t"<<#z<<" :: "<<z<<"\n"
#define tr(container, it)  for(typeof(container.begin()) it = container.begin(); it != container.end(); it++) 
#define all(v) v.begin(),v.end()
#define tatt(cont) typeof(cont.begin())
const double eps=0.000000000000001 ;
#define MOD 1000000007
typedef long double LF;
typedef double lF;
#define hihihaha ((double)CLOCKS_PER_SEC)
#define nl putchar('\n')
//-------------
int n,q;
int E[100010],S[100010];
int mat[111][111];
ll D[111];
int msk[111][111];
LF dp[111][111];
LF inf=(1LL<<60);
LF doit(int c,int kis){
	if (c==n)
	{
		return 0;
	}
	if (msk[c][kis]==1)
		return dp[c][kis];
	int kk=kis;
	LF ret=inf;
	if (D[c+1]-D[kis]<=E[kis])
	{
		ret=min(ret,doit(c+1,kis)+(LF)1.0*(D[c+1]-D[c])/S[kis]);
	}

	{
		kis=c;
		if (D[c+1]-D[kis]<=E[kis])
		ret=min(ret,doit(c+1,kis)+(LF)1.0*(D[c+1]-D[c])/S[kis]);
	}
	
	msk[c][kk]=1;
	return dp[c][kk]=ret;

}
LF log1()
{
	int i,j;
	memset(msk,0,sizeof(msk));
	D[1]=0;
	//D[1]=mat[1][2];
	for (i=2;i<=n;i++)
	{
		D[i]=D[i-1]+mat[i-1][i];
		//cerr<<" i :"<<i<<" D:"<<D[i]<<endl;
	}
	
	LF got=doit(1,1);
	return got;
}
int main()
{	//ios::sync_with_stdio(0), cin.tie(0);
	int t,tst;
	sc(t);
	wl(t)
	{
		sc2(n,q);
		int i,j;
		tst++;
		for (i=1;i<=n;i++)
		{
			sc2(E[i],S[i]);//1e9 and 1000
		}	
		for (i=1;i<=n;i++)
		{
			for (j=1;j<=n;j++)
				sc(mat[i][j]);
		}	
		for (i=0;i<q;i++)
		{
			int u,v;
			sc2(u,v);
		}
		LF ans=log1();
		printf("Case #%d: %.10lf\n",tst,(double)ans);

	}

	return 0;

}


//01010110 01101100 01100001 01100100 00101110