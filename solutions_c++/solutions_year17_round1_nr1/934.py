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
int n,m;
char s[maxn][maxn];
void solve(){
	scanf("%d%d",&n,&m);
	REP(i,0,n)REP(j,0,m)scanf(" %c",&s[i][j]);
	
	REP(i,0,n){
		REP(j,1,m)if(s[i][j]=='?')s[i][j]=s[i][j-1];
		PER(j,0,m-1)if(s[i][j]=='?')s[i][j]=s[i][j+1];
	}
	REP(j,0,m){
		REP(i,1,n)if(s[i][j]=='?')s[i][j]=s[i-1][j];
		PER(i,0,n-1)if(s[i][j]=='?')s[i][j]=s[i+1][j];
	}
	REP(i,0,n){REP(j,0,m)putchar(s[i][j]);putchar('\n');}
}

int main(){
//	freopen("in.txt","r",stdin);
//	freopen("out.txt","w",stdout);
	int _,__=0;scanf("%d",&_);
	while(_--){
		printf("Case #%d:\n",++__);
		solve();
	}
	return 0;
}
