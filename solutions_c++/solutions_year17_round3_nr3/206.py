#include<bits/stdc++.h>
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
int n,k;
typedef double ld;
ld eps=1e-8;
ld u,p[55];
inline void solve(){
	read(n);read(k);
	scanf("%lf",&u);
	rep(i,1,n)scanf("%lf",&p[i]);
	sort(p+1,p+1+n);p[n+1]=1;
	rep(i,1,n){
		int j=1;
		while(j<n&&fabs(p[j+1]-p[j])<eps)j++;
		ld v=min(p[j+1]-p[j],u/j);
		rep(k,1,j)p[k]+=v,u-=v;
	}ld res=1;
	rep(i,1,n)res*=p[i];
	printf("%.10f\n",res);
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
