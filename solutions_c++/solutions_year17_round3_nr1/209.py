#include <bits/stdc++.h>
#define rep(i,a,b) for(int i=(a);i<=(b);i++)
#define per(i,a,b) for(int i=(a);i>=(b);i--)
#define forE(i,x) for(int i=head[x];i!=-1;i=ne[i])
using namespace std;
typedef long long i64;
typedef unsigned long long u64;
typedef unsigned u32;
typedef pair<int,int> pin;
#define mk(a,b) make_pair(a,b)
#define lowbit(x) ((x)&(-(x)))
#define sqr(a) ((a)*(a))
#define clr(a) (memset((a),0,sizeof(a)))
#define ls ((x)<<1)
#define rs (((x)<<1)|1)
#define mid (((l)+(r))>>1)
#define pb push_back
#define w1 first
#define w2 second
inline void read(int &x){
	x=0;int f=1;char ch=getchar();
	while(ch<'0'||ch>'9'){if(ch=='-')f=-1;ch=getchar();}
	while(ch>='0'&&ch<='9'){x=x*10+ch-'0';ch=getchar();}
	x*=f;
}
inline void judge(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
}
/*******************************head*******************************/
int n,k;const int maxn=1005;
long double r[maxn],h[maxn];
long double ans[maxn];
int tot=0;
const long double pi=acos(-1.0);
inline void solve(){
	read(n);read(k);
	rep(i,1,n)scanf("%Lf%Lf",&r[i],&h[i]);long double fin=0;
	rep(i,1,n){
		tot=0;
		rep(j,1,n)if(i!=j&&r[j]<=r[i]){
			ans[++tot]=2*pi*r[j]*h[j];
		}if(tot<k-1)continue;
		sort(ans+1,ans+1+tot);reverse(ans+1,ans+1+tot);
		long double res=0;
		rep(j,1,k-1)res+=ans[j];
		res+=pi*r[i]*r[i]+2*pi*r[i]*h[i];
		fin=max(fin,res);
	}printf("%.10f\n",(double)fin);
}
int main(){
    judge();
    int T;read(T);
    rep(Case,1,T){
    	printf("Case #%d: ",Case);
    	solve();
    }
    return 0;
}
