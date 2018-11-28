#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef long double ld;
typedef pair<int,int > pii;
typedef pair<int,pii > piii;
typedef vector<int>     VI;

/*#define sc1(x) scanf("%d",&x);
#define sc2(x,y) scanf("%d%d",&x,&y);
#define sc3(x,y,z) scanf("%d%d%d",&x,&y,&z);
*/
#define sc1(x) scanf("%lld",&x);
#define sc2(x,y) scanf("%lld%lld",&x,&y);
#define sc3(x,y,z) scanf("%lld%lld%lld",&x,&y,&z);

#define pb push_back
#define mp make_pair
#define ini(x,val) memset(x,val,sizeof(x));
#define fs first
#define sc second
#define MOD 1000000007
#define inf 1000000001
#define linf 99999999999999999ll	//long long inf
#define PI 3.1415926535897932384626
const double eps=0.000000000000001 ;

#define tr(container, it)  for(typeof(container.begin()) it = container.begin(); it != container.end(); it++) 
#define PrintCont(cont) {cout<<("\n----------------\n");\
for(typeof(cont.begin()) it = cont.begin();it!=cont.end();++it) cout<<*it<<" ";cout<<("\n----------------\n");}
#define all(v) v.begin(),v.end()
string convertstring(ll n) { stringstream ss; ss << n ; return ss.str(); }

#define debug(x) cerr<<#x<<" :: "<<x<<"\n";
#define debug2(x,y) cerr<<#x<<" :: "<<x<<"\t"<<#y<<" :: "<<y<<"\n";
#define debug3(x,y,z) cerr<<#x<<" :: "<<x<<"\t"<<#y<<" :: "<<y<<"\t"<<#z<<" :: "<<z<<"\n";
#define debug4(x,y,z,a) cerr<<#x<<" :: "<<x<<"\t"<<#y<<" :: "<<y<<"\t"<<#z<<" :: "<<z<<"\t"<<#a<<" :: "<<a<<"\n";
#define debugarr(a,st,en) {cerr<<"\n"<<#a<<" :: ";for(int i=st;i<=en;++i)cerr<<a[i]<<" ";cerr<<"\n";}

#define LIM 100005
ll n,q,d[300],s[300],a[300][300];
double b[300][300];

int main()
{
	ll t,tt= 1;
	sc1(t);	
	while(t--)
	{

		ll i,j,k;
		sc2(n,q);
		for(i=0;i<=n+1;++i)
		{
			for(j=0;j<=n+1;++j)
			{
				b[i][j] = 0;
				a[i][j] = 0;
			}
		}
		for(i=1;i<=n;++i)
		{
			sc2(d[i],s[i]);
		}
		for(i=1;i<=n;++i)
		{
			for(j=1;j<=n;++j)
			{
				b[i][j] = 0;
				sc1(a[i][j]);
				if(a[i][j]==-1)
					a[i][j] = linf;
			}

		}
		for(i=1;i<=n;++i)
			a[i][i] = 0;
		
		for(k=1;k<=n;++k)
		{
			for(i=1;i<=n;++i)
			{
				for(j=1;j<=n;++j)
				{
					if(a[i][k]+a[k][j] < a[i][j])
						a[i][j] = a[i][k] + a[k][j];
				}
			}
		}
		
		for(i=1;i<=n;++i)
		{
			for(j=1;j<=n;++j)
			{
				if(d[i]>=a[i][j])
				{
					b[i][j] = (double)a[i][j]/s[i];
				}
				else b[i][j] = (double)linf;
			}
		}
		
		for(k=1;k<=n;++k)
		{
			for(i=1;i<=n;++i)
			{
				for(j=1;j<=n;++j)
				{
					if(b[i][k]+b[k][j] < b[i][j])
						b[i][j] = b[i][k] + b[k][j];
				}
			}
		}
		
		printf("Case #%lld: ",tt++);
		while(q--)
		{
			ll u,v;
			sc2(u,v);
			printf("%0.10lf ",b[u][v]);
		}
		printf("\n");



	}
	return 0;
}