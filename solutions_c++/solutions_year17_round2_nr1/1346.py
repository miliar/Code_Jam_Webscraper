#include<bits/stdc++.h>
//#define DEBUG
//#ifdef DEBUG
//code to debug
//#endif
//#undef DEBUG
using namespace std;

const int mod=(int)1e9+7,maxn=205,ln=17;
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
#define pii pair<int,int>
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

int main()
{
	freopen("/Users/divakar.tomar/Downloads/A-large.in", "r", stdin);
	freopen("/Users/divakar.tomar/Downloads/output.out", "w", stdout);
	int T;
	int testcase=1;
	cin>>T;
	while(T--)
	{
		double ans=0.0;
		int n;
		int d;
		cin>>d>>n;
		int slowestp=-1,slowests=-1;
		double time_taken=0.0;
		F(i,0,n)
		{
			int p,s;
			cin>>p>>s;
			double tt=(1.0*(d-p))/s;
			if(tt-time_taken>EPSILON)
			{
				time_taken=tt;
				slowestp=d-p;
				slowests=s;
			}
		}
		ans=((1.0*d)*slowests)/slowestp;
		printf("Case #%d: %.10lf\n",testcase,ans);
		testcase++;
	}
	return 0;
}