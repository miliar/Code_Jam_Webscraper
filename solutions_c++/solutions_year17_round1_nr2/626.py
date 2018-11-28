#include<bits/stdc++.h>
using namespace std;
#define For(i,n) for(int i=1;i<=n;i++)
#define Fork(i,k,n) for(int i=k;i<=n;i++)
#define Rep(i,n) for(int i=0;i<n;i++)
#define ForD(i,n) for(int i=n;i;i--)
#define ForkD(i,k,n) for(int i=n;i>=k;i--)
#define RepD(i,n) for(int i=n;i>=0;i--)
#define Forp(x) for(int p=Pre[x];p;p=Next[p])
#define Forpiter(x) for(int &p=iter[x];p;p=Next[p])  
#define Lson (o<<1)
#define Rson ((o<<1)+1)
#define MEM(a) memset(a,0,sizeof(a));
#define MEMI(a) memset(a,127,sizeof(a));
#define MEMi(a) memset(a,128,sizeof(a));
#define INF (2139062143)
#define F (100000007)
#define pb push_back
#define mp make_pair 
#define fi first
#define se second
#define vi vector<int> 
#define pi pair<int,int>
#define SI(a) ((a).size())
typedef long long ll;
typedef unsigned long long ull;
ll mul(ll a,ll b){return (a*b)%F;}
ll add(ll a,ll b){return (a+b)%F;}
ll sub(ll a,ll b){return (a-b+llabs(a-b)/F*F+F)%F;}
void upd(ll &a,ll b){a=(a%F+b%F)%F;}
int read()
{
	int x=0,f=1; char ch=getchar();
	while(!isdigit(ch)) {if (ch=='-') f=-1; ch=getchar();}
	while(isdigit(ch)) { x=x*10+ch-'0'; ch=getchar();}
	return x*f;
} 
#define MAXN (1010)
int p[MAXN],a[MAXN][MAXN];
int l[MAXN][MAXN],r[MAXN][MAXN];
int c[MAXN];
bool b[MAXN][MAXN];
int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	
	int T=read();
	For(kcase,T) {
		printf("Case #%d: ",kcase); 
		int n,m,ans=0;
		cin>>n>>m;
		For(i,n) cin>>p[i];
		For(i,n) For(j,m) {
			cin>>a[i][j];
		}
		For(i,n) sort(a[i]+1,a[i]+1+m);
		MEM(b)
		int k=1;while(1) {
			int fl=0,cnt=0;
			memset(c,-1,sizeof(c));
			For(i,n) {
				double mi=(double)p[i]*k*0.9,mx=(double)p[i]*k*1.1;
				For(j,m) if (!b[i][j]) {
					if (mi<=a[i][j]&&a[i][j]<=mx) {
						c[i]=j;
						++cnt;break;
					}
				}
				if (mi>a[i][m]) fl=1;
				
			}
			if (cnt==n) {
				For(i,n) b[i][c[i]]=1;
				++ans;
			} else ++k;
			if (fl) break;
			
		}
		
		cout<<ans<<endl;
	}
	
	return 0;
}

