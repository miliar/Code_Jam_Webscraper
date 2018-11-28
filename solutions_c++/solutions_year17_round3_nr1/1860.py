#include<bits/stdc++.h>
//#define DEBUG
//#ifdef DEBUG
//code to debug
//#endif
//#undef DEBUG
using namespace std;

const int mod=(int)1e9+7,maxn=1005,ln=17;
#define F(i,p,n) for(int i=p;i<n;i++)
#define I(i,p,q) for(int i=p;i>=q;i--)
#define forall(itr,x)	for( __typeof((x).begin()) itr=(x).begin(); itr!=(x).end(); itr++)
#define Ss(x) scanf("%s",x)
//#define S(x) scanf("%d",&x)
#define Sl(x) scanf("%lld",&x)
//#define getcx getchar_unlocked
#define getcx getchar
inline void S(int& n)
{
    n=0; int ch = getcx(); int sign = 1;
    while(ch < '0' || ch > '9') { if(ch == '-') sign=-1; ch = getcx(); }
    while(ch >= '0' && ch <= '9') { n = (n << 3) + (n << 1) + ch - '0', ch = getcx(); }
    n = n * sign;
}
#define Ps(x) printf("%d  ",x)
#define P(x) printf("%d\n",x)
typedef long long int LL;
#define modulo(x,y,z) (x+y)<0?x+y+z:((x+y>=z)?x+y-z:x+y)
#define Debug(x) cout << #x << "=" << x << endl
#define Debugarr(x,n) cout<<"array "<<#x<<":"<<endl; F(ij,0,n) cout<<ij<<". "<<x[ij]<<endl; cout<<endl
#define Debugarr2(x,m,n) cout<<"array "<<#x<<":"<<endl; F(ij,0,m) {F(jk,0,n) cout<<x[ij][jk]<<" "; cout<<endl;} cout<<endl
#define Debugset(x) cout<<"Set "<<#x<<":"<<endl; forall(iittrr,x) cout<<(*iittrr)<<endl; cout<<endl
#define Debugmap(x) cout<<"Map "<<#x<<":"<<endl; forall(iittrr,x) cout<<"( "<<(iittrr->Fi)<<" , "<<(iittrr->Se)<<" )"<<endl; cout<<endl
#define pii pair<LL,LL>
#define Fi first
#define Se second
#define chk(x,n) (x[n>>5]&(1<<(n&31))) //unsigned int
//#define set(x,n) (x[n>>5]|=(1<<(n&31)))//32 bit
const int shift=30,etf=mod-1,LIM=(int)1e9;
#define WHITE 0
#define GREY 1
#define BLACK 2

const LL inf=(LL)1e18+1;

const double PI=(double)3.141592653589793238,EPSILON=1e-10;

LL dp[maxn][maxn];

bool comp(pii a,pii b)
{
	if(a.Fi==b.Fi)
		return a.Se>b.Se;
	return a.Fi>b.Fi;
}

int main()
{
	freopen("/Users/divakar.tomar/Downloads/A-large (1).in", "r", stdin);
	freopen("/Users/divakar.tomar/Downloads/output.out", "w", stdout);
	int T;
	int testcase=1;
	cin>>T;
	while(T--)
	{
		memset(dp,0,sizeof dp);
		double ans=0.0;
		int n;
		int k;
		cin>>n>>k;
		vector<pii> dims(n+1);
		F(i,1,n+1)
		{
			LL r,h;
			cin>>r>>h;
			dims[i].Fi=r;
			dims[i].Se=h;
		}

		// F(i,1,n+1)
		// {
		// 	Debug(i);
		// 	printf("r=%lf h=%lf\n",dims[i].Fi,dims[i].Se);
		// }

		sort(dims.begin()+1,dims.end(),comp);
		// F(i,1,n+1)
		// {
		// 	Debug(i);
		// 	printf("r=%lf h=%lf\n",dims[i].Fi,dims[i].Se);
		// }

		F(i,1,n+1)
		{
			//Debug(i);
			LL r=dims[i].Fi,h=dims[i].Se;
			dp[i][1]=max(2*r*h+r*r,dp[i-1][1]);
		}

		//Debugarr2(dp,n+1,n+1);

		F(i,2,n+1)
		{
			F(j,2,i+1)
			{
				LL r=dims[i].Fi,h=dims[i].Se;
				dp[i][j]=max(dp[i-1][j],dp[i-1][j-1]+2*r*h);
			}
		}

		//Debugarr2(dp,n+1,n+1);


		ans=M_PI*dp[n][k];

		printf("Case #%d: %.10lf\n",testcase,ans);
		testcase++;
	}
	return 0;
}