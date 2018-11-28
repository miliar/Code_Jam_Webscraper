#include<bits/stdc++.h>
using namespace std;
#define REP(i,a,b)for(int i=(a),i##_end_=(b);i<i##_end_;++i)
#define PER(i,a,b)for(int i=(b)-1,i##_end_=(a);i>=i##_end_;--i)
#define pb push_back
#define lock lok
#define fi first
#define se second
template<class T>inline bool umx(T& A,const T& B){return A<B?A=B,1:0;}
template<class T>inline bool umn(T& A,const T& B){return A>B?A=B,1:0;}
typedef long long LL;
typedef long double db;
typedef pair<int,int> PII;
typedef pair<db,int> PDI;

const int maxn=24*60+10;

int n,m;

int lock[maxn];
int f[maxn][maxn][2][2];

void solve(){
	scanf("%d%d",&n,&m);
	memset(lock,0,sizeof lock);
	REP(i,1,n+1){
		int x,y;scanf("%d%d",&x,&y);
		REP(j,x+1,y+1)lock[j]=1;
	}
	REP(i,1,m+1){
		int x,y;scanf("%d%d",&x,&y);
		REP(j,x+1,y+1)lock[j]=2;
	}
	memset(f,0x3f,sizeof f);
	f[0][0][0][0]=f[0][0][1][1]=0;
	int N=12*60;
	for(int i=0;i<=N;++i)
		for(int j=0;j<=N;++j)if(i+j>=1){
			if(i>0&&lock[i+j]!=1){
				umn(f[i][j][0][0],min(f[i-1][j][0][0],f[i-1][j][0][1]+1));
				umn(f[i][j][1][0],min(f[i-1][j][1][0],f[i-1][j][1][1]+1));
			}
			if(j>0&&lock[i+j]!=2){
				umn(f[i][j][0][1],min(f[i][j-1][0][1],f[i][j-1][0][0]+1));
				umn(f[i][j][1][1],min(f[i][j-1][1][1],f[i][j-1][1][0]+1));
			}
		}
	printf("%d\n",min(min(f[N][N][0][0],f[N][N][1][1]),min(f[N][N][0][1],f[N][N][1][0])+1));
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

