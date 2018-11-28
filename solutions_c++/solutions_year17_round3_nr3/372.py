#include<bits/stdc++.h>
using namespace std;
#define For(i,n) for(int i=1;i<=n;i++)
#define Fork(i,k,n) for(int i=k;i<=n;i++)
#define ForkD(i,k,n) for(int i=n;i>=k;i--)
#define Rep(i,n) for(int i=0;i<n;i++)
#define ForD(i,n) for(int i=n;i;i--)
#define RepD(i,n) for(int i=n;i>=0;i--)
#define Forp(x) for(int p=pre[x];p;p=next[p])
#define Forpiter(x) for(int &p=iter[x];p;p=next[p])
#define Lson (o<<1)
#define Rson ((o<<1)+1)
#define MEM(a) memset(a,0,sizeof(a));
#define MEMI(a) memset(a,0x3f,sizeof(a));
#define MEMi(a) memset(a,128,sizeof(a));
#define MEMx(a,b) memset(a,b,sizeof(a));
#define INF (0x3f3f3f3f)
#define F (1000000007)
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define vi vector<int>
#define pi pair<int,int>
#define SI(a) ((a).size())
#define Pr(kcase,ans) printf("Case #%d: %lld\n",kcase,ans);
#define PRi(a,n) For(i,n-1) cout<<a[i]<<' '; cout<<a[n]<<endl;
#define PRi2D(a,n,m) For(i,n) { \
						For(j,m-1) cout<<a[i][j]<<' ';\
						cout<<a[i][m]<<endl; \
						}
#pragma comment(linker, "/STACK:102400000,102400000")
#define ALL(x) (x).begin(),(x).end()
typedef long long ll;
typedef long double ld;
typedef unsigned long long ull;
ll mul(ll a,ll b){return (a*b)%F;}
ll add(ll a,ll b){return (a+b)%F;}
ll sub(ll a,ll b){return ((a-b)%F+F)%F;}
void upd(ll &a,ll b){a=(a%F+b%F)%F;}
inline int read()
{
	int x=0,f=1; char ch=getchar();
	while(!isdigit(ch)) {if (ch=='-') f=-1; ch=getchar();}
	while(isdigit(ch)) { x=x*10+ch-'0'; ch=getchar();}
	return x*f;
}
#define MAXN (1010)
int ka = 0;
int main()
{
//	freopen("C.in","r",stdin);
//	freopen("terris.out","w",stdout);
	int t; cin>>t;
	while(t--) {
    ka++;
		int n=read(),k=read();
		double x;cin>>x;
		vector<double> v;
		For(i,n) {
			double c;
			cin>>c;
			v.pb(c);
		}
		sort(ALL(v));

		Rep(i,k) v[i]=v[i-k+n];
//		Rep(i,k) cout<<v[i]<<endl;
		n=k;
		double t=0,Ans=0;
		Rep(i,n) {
			t+=v[i];
			double fl=x-(v[i]*(i+1)-t);
			if (fl<0) break;
			double h=v[i]+fl/(i+1);
			if (h>1) h=1;
			double ans=1;
			Rep(j,n) {
				if(j<=i) ans*=h;else ans*=v[j];
			}
			Ans=max(ans,Ans);
		}
		printf("Case #%d: %.6lf\n", ka, Ans);

	}

	return 0;
}
