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
ll n,k;
map<ll,ll> h;
map<ll,ll>::iterator it;
int main()
{
//	freopen("C.in","r",stdin);
//	freopen("c.out","w",stdout);
	
	int T=read();
	For(kcase,T) {
		printf("Case #%d: ",kcase); 
		cin>>n>>k;--k;
		h.clear();
		h[n]=1;
		while(k) {
			it=h.end();it--;
			ll len=it->fi;
			ll p1=len/2,p2=len-p1-1;
			ll t=it->se;
			if(t>k) break;
			else {
				h.erase(it);
				if (!h.count(p1)) h[p1]=0;
				if (!h.count(p2)) h[p2]=0;
				h[p1]+=t;h[p2]+=t;
				k-=t;
			}
		}	
		
		it=h.end();it--;
		ll len=it->fi,p1,p2;
		if (len&1) p1=p2=len/2;
		else p1=len/2,p2=p1-1;
		cout<<p1<<' '<<p2<<endl;
		
	}
	
	return 0;
}

