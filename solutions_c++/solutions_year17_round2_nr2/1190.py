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
int ans[100010];
int p=0;
vector<int>v[6];
int ch[6],f=0,N;

void doit(int ind,int x)
{

	ch[x]--;
	ans[p++]=x;
	//cerr<<"ind :"<<ind<<" x:"<<x<<" "<<N<<endl;
	int i,mx=-1,yo;
	for (i=0;i<v[x].size();i++)
	{
		if (mx<ch[v[x][i]])
		{
			mx=ch[v[x][i]];
			yo=v[x][i];
		}
		
	}
	if (mx<=0&&ind<N-1)
	{	
		f=0;

	}
	if (f&&ind<N-1)
		doit(ind+1,yo);
	if (ind==N-1)
	{

	}
	ch[x]++;
	p--;
}
char X[6]={'R','O','Y','G','B','V'};
int main()
{	//ios::sync_with_stdio(0), cin.tie(0);
	int t;
	
	v[0].pb(2);v[0].pb(4);v[0].pb(3);
	v[1].pb(3);v[1].pb(4);v[1].pb(5);
	v[2].pb(0);v[2].pb(4);v[2].pb(5);
	v[3].pb(0);v[3].pb(1);v[3].pb(5);
	v[4].pb(0);v[4].pb(2);v[4].pb(1);
	v[5].pb(1);v[5].pb(2);v[5].pb(3);
	sc(t);
	int tst=0;

	wl(t)
	{		  //0 1  2  3  4   5
		int  R, O, Y, G, B,  V;
		tst++;
		sc(N);
		
		int i,j;
		set<pii>s;
		set<pii>::iterator it;
		
		printf("Case #%d: ",tst);
		for (i=0;i<6;i++)
		{
			sc(ch[i]);
			//s.insert(mp(-ch[i],i));
		}
		for(i=0;i<6;i++)
		{
			p=0;
			f=1;
			if(ch[i]<=0)
				continue;
			doit(0,i);
			if (!f)
				continue;
			for (j=0;j<v[i].size();j++)
			{
				if (ans[N-1]==v[i][j])
					break;
			}
			if (j<v[i].size())
				break;
		}
		if (i<6)
		{
			for (j=0;j<N;j++)
			{
				printf("%c",X[ans[j]]);
			}
			nl;
		}
		else
		{
			printf("IMPOSSIBLE\n");
		}

	}

	return 0;

}


//01010110 01101100 01100001 01100100 00101110