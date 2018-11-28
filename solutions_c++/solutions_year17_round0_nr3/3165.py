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
	freopen("/Users/divakar.tomar/Downloads/C-large.in", "r", stdin);
	freopen("/Users/divakar.tomar/Downloads/output.out", "w", stdout);
	int T;
	int testcase=1;
	cin>>T;
	while(T--)
	{
		LL ans=0;
		LL n,k;
		cin>>n>>k;
		LL even=0,odd=0,esz=n,osz=n;
		if(n&1)
			odd++,esz++;
		else
			even++,osz--;
		while(k>0)
		{

			LL tot=even+odd;
			// printf("-------------------------before:\n");
			// Debug(even);
			// Debug(esz);
			// Debug(odd);
			// Debug(osz);
			// Debug(tot);
			if(k<=tot)
			{
				if(osz>esz&&k<=odd)
				{
					printf("Case #%d: %lld %lld\n",testcase++,osz/2,osz/2);
				}
				else if(osz>esz&&k>odd)
				{
					printf("Case #%d: %lld %lld\n",testcase++,esz/2,esz/2-1);
				}
				else if(osz<esz&&k<=even)
				{
					printf("Case #%d: %lld %lld\n",testcase++,esz/2,esz/2-1);
				}
				else
				{
					printf("Case #%d: %lld %lld\n",testcase++,osz/2,osz/2);
				}
				break;
			}
			LL newe=even,newo=even;
			LL tempo,tempe;
			LL half=osz>>1;
			if(half&1)
			{
				newo+=2*odd;
				if(esz>osz)
				{
					tempe=half+1;
					tempo=half;
				}
				else
				{
					tempo=half;
					tempe=half-1;
				}
			}
			else
			{
				newe+=2*odd;
				if(esz>osz)
				{
					tempe=half;
					tempo=half+1;
				}
				else
				{
					tempo=half-1;
					tempe=half;
				}
			}
			osz=tempo;
			esz=tempe;
			even=newe;
			odd=newo;
			k-=tot;
			// printf("*******************after:\n");
			// Debug(even);
			// Debug(esz);
			// Debug(odd);
			// Debug(osz);
			// Debug(k);
		}
	}
	return 0;
}