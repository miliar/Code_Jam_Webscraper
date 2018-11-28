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
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
}
/*******************************head*******************************/
map<i64,i64> res;
map<i64,i64>::iterator It;
inline void solve(){
	i64 n,k;
	cin>>n>>k;
	res.clear();
	res[n+2]=1;
	for(;;){
		It=res.end();It--;
		i64 l=1,r=It->w1;
		i64 md=(l+r)>>1;
		if(k<=It->w2){
			printf("%lld %lld\n",max(md-l-1,r-md-1),min(md-l-1,r-md-1));
			return;
		}k-=It->w2;
		res[md-l+1]+=It->w2;
		res[r-md+1]+=It->w2;
		res.erase(r);
	}
}
int main(){
    judge();
    int T;read(T);
    rep(i,1,T){
    	printf("Case #%d: ",i);solve();
    }
    return 0;
}
