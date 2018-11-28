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

const int INF=0x3f3f3f3f;
const int maxn=60;
const int maxm=60;
int n,m;
int a[maxn],_A[maxn][maxm];

struct seg{int l,r;};
vector<seg>A[maxn];
int pos[maxn];
void solve(){
	scanf("%d%d",&n,&m);
	REP(i,0,n)scanf("%d",a+i);
	REP(i,0,n)REP(j,0,m)scanf("%d",_A[i]+j);
	REP(i,0,n){
		A[i].clear();
		REP(j,0,m){
			int l=(_A[i][j]*10+11*a[i]-1)/(11*a[i]),r=(_A[i][j]*10)/(9*a[i]);
			if(l<=r)A[i].pb({l,r});
//			printf("%d %d %d\n",i,l,r);
		}
		sort(A[i].begin(),A[i].end(),[](seg a,seg b){return a.l!=b.l ? a.l<b.l : a.r<b.r;});
	}
	memset(pos,0,sizeof pos);
	int res=0;
	for(int z=1;z<=1000000;){
		bool ed=0,fg=1;
		REP(i,0,n){
			while(pos[i]<A[i].size() && A[i][pos[i]].r<z)++pos[i];
			if(pos[i]==A[i].size()){ed=1;break;}
			else if(A[i][pos[i]].l>z)fg=0;
		}
		if(ed)break;
		if(!fg){++z;continue;}
		REP(i,0,n)++pos[i];
		++res;
	}
	printf("%d\n",res);
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
