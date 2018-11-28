#include<bits/stdc++.h>
#define vi vector<int>
#define vll vector<LL>
#define pii pair<int,int>
#define pli pair<LL,int>
#define pll pair<LL,LL>
#define fr first
#define sc second
#define MAX 50010
#define LL   long long int
#define ll   long long int
//#define LLL long long int
#define inf (1ll<<62)
#define INF 10000000
#define mod 1000000007
#define PI acos(-1)
//#define N 65
#define mMax 30010
#define nMax 2010
#define SZ(a) a.size()
#define pb push_back
#define eb emplace_back
#define mp make_pair
#define rep1(i,b) for(int i=1;i<=b;i++)
#define rep2(i,b) for(int i=0;i<b;i++)
#define rep(i,a,b) for(int i=a;i<=b;i++)
#define all(A) A.begin(),A.end()
#define isf(a) scanf("%d",&a);
#define Lsf(a) scanf("%I64d",&a);
#define lsf(a) scanf("%lld",&a);
#define csf(a) scanf("%c",&a);
#define vedge vector<Edge>
using namespace std;
LL bigmod(LL a,LL b,LL Mod)
{
    if(b==0) return 1ll;
    if(b%2) return (a*bigmod(a,b-1,Mod))%Mod;
    LL c=bigmod(a,b/2,Mod);
    return (c*c)%Mod;
}
struct cyl{
	double r,h;
	double area;
	 cyl(){}
	cyl(double a,double b){
		r=a;
		h=b;
		area=r*h*2.0;
	}
};
bool cmp(cyl a,cyl b)
{
	if(a.r==b.r)
	{
		return a.h>b.h;
	}
	return a.r>b.r;
}
vector<cyl> A;
double dp[1010][1010];
int main()
{
	freopen("input.in","r",stdin);
	freopen("output.txt","w",stdout);
	int T,I=1;
	cin>>T;
	while(T--)
	{
		A.clear();
		printf("Case #%d: ",I++);
		int n,k;
		scanf("%d %d",&n,&k);
		rep1(i,n)
		{
			double a,b;
			scanf("%lf %lf",&a,&b);
			A.pb(cyl(a,b));
		}
		sort(all(A),cmp);
		rep2(i,n) 
		if(i>0)
		dp[1][i]=max(dp[1][i-1],A[i].r*A[i].r  + A[i].area);
		else dp[1][i]=max(0.0,A[i].r*A[i].r  + A[i].area);
		rep(j,2,k)
		{
			dp[j][j-2]=0;
			rep(i,j-1,n-1){
				dp[j][i]=max(dp[j][i-1],dp[j-1][i-1]+A[i].area);
				//cout<<dp[i][j]<<" ";
			}

		}
		/*rep1(i,k)
		rep2(j,n)
		cout<<dp[j][i]*/
		printf("%f\n",dp[k][n-1]*PI);
	}
	return 0;
}