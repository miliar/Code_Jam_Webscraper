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
const int maxn=1005;
pin a[maxn];
int res[maxn],n,m,c,ans;
bool flag[maxn][maxn],ins[maxn][maxn];
int cnt[maxn],tot[maxn],sum[maxn];
inline int calc(){
	int res=0;memset(flag,0,sizeof(flag));memset(ins,0,sizeof(ins));
	memset(cnt,0,sizeof(cnt));
	rep(i,1,m){
		bool fkyou=0;
		rep(j,1,ans){
			if((!flag[j][a[i].w1])&&(!ins[j][a[i].w2])){
				fkyou=1;cnt[j]++;
				flag[j][a[i].w1]=1;ins[j][a[i].w2]=1;
				break;
			}
		}
		if(fkyou)continue;
		res++;
		rep(j,1,ans){
			if(cnt[j]<a[i].w1&&(!ins[j][a[i].w2])){
				ins[j][a[i].w2]=1;cnt[j]++;
				break;
			}
			if(j==ans)assert(0);
		}
	}
	return res;
}
inline void solve(){
	read(n);read(c);read(m);memset(sum,0,sizeof(sum));
	rep(i,1,m)read(a[i].w1),read(a[i].w2),sum[a[i].w1]++;
	ans=0;
	memset(tot,0,sizeof(tot));
	int res2=0;

	rep(i,1,m)tot[a[i].w2]++;
	rep(i,1,c)ans=max(ans,tot[i]);
	sort(a+1,a+1+m);
	rep(i,1,m){
		ans=max(ans,(i-1)/(a[i].w1)+1);
	}	rep(i,1,n){
		sum[i]+=sum[i-1];
		res2+=max(0,sum[i]-sum[i-1]-ans);
	}
	printf("%d %d\n",ans,res2);
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
