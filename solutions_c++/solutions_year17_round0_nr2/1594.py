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
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
}
/*******************************head*******************************/
const int maxn=25;
char s[maxn],ans[maxn];
int n;
inline bool valid(){
	rep(i,1,n-1){
		if(ans[i]>ans[i+1])return 0;
	}return 1;
}
inline void solve(){
	scanf("%s",s+1);n=strlen(s+1);i64 fk=0;
	rep(i,1,n+1){
		if(s[i]=='0')continue;
		rep(j,1,i-1){
			ans[j]=s[j];
		}
		ans[i]=s[i]-1;
		rep(j,i+1,n)ans[j]='9';
		if(valid()){
			i64 res=0;
			rep(j,1,n)res=res*10ll+ans[j]-'0';
			fk=max(res,fk);
		}
	}printf("%lld\n",fk);
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
