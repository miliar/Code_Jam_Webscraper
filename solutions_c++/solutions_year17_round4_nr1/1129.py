#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef long double ld;
typedef pair<int,int > pii;
typedef pair<int,pii > piii;
typedef vector<int>     VI;

#define sc1(x) scanf("%d",&x);
#define sc2(x,y) scanf("%d%d",&x,&y);
#define sc3(x,y,z) scanf("%d%d%d",&x,&y,&z);
/*
#define sc1(x) scanf("%lld",&x);
#define sc2(x,y) scanf("%lld%lld",&x,&y);
#define sc3(x,y,z) scanf("%lld%lld%lld",&x,&y,&z);
*/
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
int n,p,a[1000];
int dp[105][105][105][5];

int solve(int r1,int r2,int r3,int last)
{
	int x = (last == 0);
	int &ans = dp[r1][r2][r3][last];
	if(ans != -1 )return ans;
	ans = 0;
	if(r1 > 0)
	{
		ans = max(ans , x + solve(r1-1,r2,r3,(last + 1) % p));
	}
	if(r2 > 0)
	{
		ans = max(ans , x + solve(r1 , r2 - 1, r3 , (last+2)%p));
	}
	if(r3 > 0)
	{
		ans = max(ans , x + solve(r1 , r2 , r3-1 , (last+3)%p));
	}
	return ans ;
}
int main()
{
	int t,tt=1;
	sc1(t);
	while(t--)
	{
		ini(dp,-1);
		int i,j,ans = 0;
		sc2(n,p);
		ini(a,0);
		for(i=1;i<=n;++i)
		{
			int x;
			sc1(x);
			x%=p;
			a[x]++;
		}
		ans = a[0] + solve(a[1],a[2],a[3],0);
		printf("Case #%d: %d\n",tt++,ans);
	}	
	return 0;
}