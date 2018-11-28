#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<vector>
#include<map>
#include<iostream>
#include<algorithm>
#include<deque>
#include<stack>
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
#define csf(a) scanf("%c",&a);
using namespace std;
LL bigmod(LL a,LL b,LL Mod)
{
    if(b==0) return 1ll;
    if(b%2) return (a*bigmod(a,b-1,Mod))%Mod;
    LL c=bigmod(a,b/2,Mod);
    return (c*c)%Mod;
}
double A[1010];
double B[1010];
double dp[1010];

double ftime(int u,int v)
{
	if(B[u]<=B[v]) return -1;
	return (A[v]-A[u])/(B[u]-B[v]);
}
pair<double,double> DD[1010];
int main()
{
    freopen("input.in","r",stdin);
 freopen("output.txt","w",stdout);
	int T,I=1;
	cin>>T;
	while(T--)
	{
		printf("Case #%d: ",I++);
		double D;
		int n;
		scanf("%lf",&D);
		scanf("%d",&n);
		double t=-1;
		double a,b;
		rep1(i,n) {
			scanf("%lf %lf",&a,&b);
			double res=(D-a)/b;
			t=max(res,t);
		}
		printf("%lf\n",D/t);
	}
	return 0;
}
