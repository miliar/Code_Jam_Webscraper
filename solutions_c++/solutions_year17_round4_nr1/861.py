#include<bits/stdc++.h>
using namespace std;
#define REP(i,a,b)for(int i=(a),i##_end_=(b);i<i##_end_;++i)
#define PER(i,a,b)for(int i=(b)-1,i##_end_=(a);i>=i##_end_;--i)
#define pb push_back
template<class T>inline bool umx(T& A,const T& B){return A<B?A=B,1:0;}
template<class T>inline bool umn(T& A,const T& B){return A>B?A=B,1:0;}
typedef pair<int,int> PII;
typedef long long LL;

const int maxn=110;

typedef vector<int> vec;

vec a;
int n,p;

map<vec,int> memo;
int dfs(vec&x){
	if(memo.find(x)!=memo.end())return memo[x];
	int res=0;
	REP(i,1,p)if(x[i-1]>0){
		int t=x[p-1];
		--x[i-1];(x[p-1]+=i)%=p;
		umx(res,dfs(x)+(t==0));
		++x[i-1];x[p-1]=t;
	}
	memo[x]=res;
	return res;
}
void solve(){
	scanf("%d%d",&n,&p);
	a.assign(p,0);
	int ze=0;
	REP(i,0,n){int x;scanf("%d",&x);if(x%p)++a[x%p-1];else ++ze;}
	memo.clear();
	printf("%d\n",dfs(a)+ze);
}

int main(){
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int _,__=0;scanf("%d",&_);
	while(_--){
		printf("Case #%d: ",++__);
		solve();
	}
	return 0;
}

