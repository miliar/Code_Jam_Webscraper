#include<bits/stdc++.h>
using namespace std;
#define REP(i,a,b)for(int i=(a),i##_end_=(b);i<i##_end_;++i)
#define PER(i,a,b)for(int i=(b)-1,i##_end_=(a);i>=i##_end_;--i)
#define pb push_back
#define fi first
#define se second
template<class T>inline bool umx(T& A,const T& B){return A<B?A=B,1:0;}
template<class T>inline bool umn(T& A,const T& B){return A>B?A=B,1:0;}
typedef long long LL;
typedef double db;
typedef pair<int,int> PII;
typedef pair<db,int> PDI;

const int maxn=30;

char _s[maxn],t[maxn];
int s[maxn];int n;
LL res;
void dfs(int i,int j,bool eq){
	if(i==n){
		t[n]=0;
		LL t0;sscanf(t,"%lld",&t0);
		umx(res,t0);
		return;
	}
	if(!eq){
		REP(k,i,n)t[k]='9';t[n]=0;
		LL t0;sscanf(t,"%lld",&t0);
		umx(res,t0);
		return;
	}
	if(s[i]-1>=j){
		t[i]='0'+(s[i]-1);
		dfs(i+1,s[i]-1,0);
	}
	if(s[i]>=j){
		t[i]='0'+s[i];
		dfs(i+1,s[i],1);
	}
}
void solve(){
	scanf("%s",_s);n=strlen(_s);
	REP(i,0,n)s[i]=_s[i]-'0';
	res=0;
	dfs(0,0,1);
	printf("%lld\n",res);
}
int main(){
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int _,__=0;scanf("%d",&_);
	while(_--){
		printf("Case #%d: ",++__);
		solve();
	}
	return 0;
}
