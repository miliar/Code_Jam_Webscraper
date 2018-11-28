#include<bits/stdc++.h>
//#define DEBUG
//#ifdef DEBUG
//code to debug
//#endif
//#undef DEBUG
using namespace std;

const int mod=(int)1e9+7,maxn=2005,ln=17;
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
#define pii pair<int,char>
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
	freopen("/Users/divakar.tomar/Downloads/B-small-attempt1 (1).in", "r", stdin);
	freopen("/Users/divakar.tomar/Downloads/output.out", "w", stdout);
	int T;
	int testcase=1;
	cin>>T;
	while(T--)
	{
		char ans[maxn];
		int n;
		cin>>n;
		F(i,0,n)
		{
			ans[i]='0';
		}
		ans[n]='\0';
		int a[6],cnt[3]={0};
		bool ok=true;
		F(i,0,6)
		{
			cin>>a[i];
			if(a[i]>n/2)
				ok=false;
		}
		int pos=0;
		vector<pii> v;
		v.push_back(pii(-a[0],'R'));
		v.push_back(pii(-a[2],'Y'));
		v.push_back(pii(-a[4],'B'));
		sort(v.begin(),v.end());
		vector<char> vc;
		F(i,0,3)
		{
			F(j,0,-v[i].Fi)
			{
				vc.push_back(v[i].Se);
			}
		}
		F(i,0,vc.size())
		{
			while(ans[pos]!='0')
			{
				pos++;
				pos%=n;
			}
			ans[pos]=vc[i];
			pos+=2;
			pos%=n;
		}
		if(ok)
			printf("Case #%d: %s\n",testcase,ans);
		else
			printf("Case #%d: IMPOSSIBLE\n",testcase);
		testcase++;
	}
	return 0;
}