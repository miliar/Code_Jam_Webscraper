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

const int maxn=1010;
int d,n;
int a[maxn];

void solve(){
	scanf("%d%d",&d,&n);
	db t=0;
	REP(i,0,n){
		int k,s;scanf("%d%d",&k,&s);
		umx(t,(db)(d-k)/s);
	}
	printf("%.6f\n",d/t);
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

