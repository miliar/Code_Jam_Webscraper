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
const int maxn=2005;
int f[maxn][maxn][2];
bool flagA[maxn],flagB[maxn];
int n,m;
inline void solve(){
	read(n);read(m);
	memset(flagA,0,sizeof(flagA));memset(flagB,0,sizeof(flagB));
	rep(i,1,n){
		int l,r;read(l);read(r);
		rep(i,l+1,r)flagA[i]=1;
	}
	rep(i,1,m){
		int l,r;read(l);read(r);
		rep(i,l+1,r)flagB[i]=1;
	}
	rep(i,0,2000)rep(j,0,2000)f[i][j][0]=f[i][j][1]=1e9;
	f[0][0][0]=0;//f[0][0][1]=0;
	rep(i,0,1440-1)rep(j,0,720)rep(k,0,1){
		if(!flagA[i+1]){
			f[i+1][j+1][0]=min(f[i+1][j+1][0],f[i][j][k]+(k!=0));
		}
		if(!flagB[i+1]){
			f[i+1][j][1]=min(f[i+1][j][1],f[i][j][k]+(k!=1));
		}
	}
	int ans=min(f[1440][720][0],f[1440][720][1]+1);
	rep(i,0,2000)rep(j,0,2000)f[i][j][0]=f[i][j][1]=1e9;
	//f[0][0][0]=0;
	f[0][0][1]=0;
	rep(i,0,1440-1)rep(j,0,720)rep(k,0,1){
		if(!flagA[i+1]){
			f[i+1][j+1][0]=min(f[i+1][j+1][0],f[i][j][k]+(k!=0));
		}
		if(!flagB[i+1]){
			f[i+1][j][1]=min(f[i+1][j][1],f[i][j][k]+(k!=1));
		}
	}
	ans=min(ans,min(f[1440][720][1],f[1440][720][0]+1));
	cout<<ans<<endl;
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
