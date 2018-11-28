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
int k;
char s[10000];
int a[10000],b[10000];
int p;
int main()
{
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	
	int T=read();
	For(kcase,T) {
		printf("Case #%d: ",kcase); 
		ll n;
		cin>>n;
		p=0;
		while(n) {
			a[++p]=n%10;n/=10;
		}
		bool fl=0;
		ForD(i,p) {
			bool c=0;
			ForD(j,i) {
				if (a[j]<a[i]) c=1;
				if (a[j]>a[i]) break;
			}
			if (!c) b[i]=a[i];else {
				b[i]=a[i]-1;
				ForD(k,i-1) b[k]=9;
				break;
			}
		}
		while(p>1&&!b[p]) --p;
		ForD(i,p) cout<<b[i];
		cout<<endl;
	}
	
	return 0;
}

