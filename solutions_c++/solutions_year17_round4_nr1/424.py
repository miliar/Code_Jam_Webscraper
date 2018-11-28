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
const int maxn=105;
int f3[4][maxn][maxn],f4[4][maxn][maxn][maxn];
int a[maxn],n,P;
const int inf=1e9;
inline void solve(){
	read(n);read(P);rep(i,1,n)read(a[i]);
	rep(i,1,n)a[i]%=P;
	if(P==2){
		int res=0,cnt2=0;
		rep(i,1,n)if(a[i]==0)res++;else cnt2++;
		res+=(cnt2-1)/2;
		if(cnt2==0)res--;
		cout<<res+1<<endl;
		return;
	}
	if(P==3){
		int res=0,cnt1=0,cnt2=0;
		rep(i,1,n){
			if(a[i]==0)res++;
			if(a[i]==1)cnt1++;
			if(a[i]==2)cnt2++;
		}
		rep(i,0,2)rep(j,0,n)rep(k,0,n)f3[i][j][k]=-inf;
		f3[0][cnt1][cnt2]=0;
		per(j,n,0)per(k,n,0)rep(i,0,2)if(f3[i][j][k]!=-inf){
			if(j)f3[(i+1)%3][j-1][k]=max(f3[(i+1)%3][j-1][k],f3[i][j][k]+((i+1)%3==0));
			if(k)f3[(i+2)%3][j][k-1]=max(f3[(i+2)%3][j][k-1],f3[i][j][k]+((i+2)%3==0));
		}
		int ans=0;
		ans=max(f3[0][0][0]-1,max(f3[1][0][0],f3[2][0][0]));
		cout<<ans+res+1<<endl;
		return;
	}
	if(P==4){
		int res=0,cnt1=0,cnt2=0,cnt3=0;
		rep(i,1,n){
			if(a[i]==0)res++;
			if(a[i]==1)cnt1++;
			if(a[i]==2)cnt2++;
			if(a[i]==3)cnt3++;
		}
		rep(i,0,3)rep(j,0,n)rep(k,0,n)rep(p,0,n)f4[i][j][k][p]=-inf;
		f4[0][cnt1][cnt2][cnt3]=0;
		per(j,n,0)per(k,n,0)per(p,n,0)rep(i,0,3)if(f4[i][j][k][p]!=-inf){
			if(j)f4[(i+1)%4][j-1][k][p]=max(f4[(i+1)%4][j-1][k][p],f4[i][j][k][p]+((i+1)%4==0));
			if(k)f4[(i+2)%4][j][k-1][p]=max(f4[(i+2)%4][j][k-1][p],f4[i][j][k][p]+((i+2)%4==0));
			if(p)f4[(i+3)%4][j][k][p-1]=max(f4[(i+3)%4][j][k][p-1],f4[i][j][k][p]+((i+3)%4==0));
		}
		int ans=0;
		ans=max(f4[0][0][0][0]-1,max(f4[1][0][0][0],f4[2][0][0][0]));
		ans=max(ans,f4[3][0][0][0]);
		cout<<ans+res+1<<endl;
		return;
	}
}
int main(){
    judge();
    int T;read(T);
    rep(i,1,T){
    	printf("Case #%d: ",i);
    	solve();
    }
    return 0;
}
