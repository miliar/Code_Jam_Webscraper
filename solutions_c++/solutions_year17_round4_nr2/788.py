#include<bits/stdc++.h>
using namespace std;
#define REP(i,a,b)for(int i=(a),i##_end_=(b);i<i##_end_;++i)
#define PER(i,a,b)for(int i=(b)-1,i##_end_=(a);i>=i##_end_;--i)
#define pb push_back
template<class T>inline bool umx(T& A,const T& B){return A<B?A=B,1:0;}
template<class T>inline bool umn(T& A,const T& B){return A>B?A=B,1:0;}
typedef pair<int,int> PII;
typedef long long LL;

const int maxn=1010;

typedef vector<int> vec;
int n,c,m;

vec a[maxn];
int numb[maxn],nump[maxn];

void solve(){
	scanf("%d%d%d",&n,&c,&m);
	memset(numb,0,sizeof numb);
	memset(nump,0,sizeof nump);
	int res=0,res2=0;
	REP(i,1,m+1){
		int p,b;scanf("%d%d",&p,&b);
		umx(res,++numb[b]);
		++nump[p];
	}
	REP(i,1,n+1)umx(res,(nump[i]+i-1)/i);
	REP(i,1,n+1)res2+=max(0,nump[i]-res);
	printf("%d %d\n",res,res2);
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

