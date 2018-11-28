#include <bits/stdc++.h>
#define openfile(s) freopen(s".in","r",stdin);freopen(s".out","w",stdout)
#define mpr std::make_pair
#define lg(x) (31-__builtin_clz(x))
#define lgll(x) (63-__builtin_clzll(x))
#define __count __builtin_popcount
#define __countll __builtin_popcountll
#define X first
#define Y second
#define mst(x) memset(x,0,sizeof(x))
#define mst1(x) memset(x,-1,sizeof(x))
#define ALL(c) (c).begin(),(c).end()
#define FOR(i,n) for(int i=0;i<n;i++)
#define FOR1(i,n) for(int i=1;i<=n;i++)
#define FORit(it,c) for(__typeof(c.begin()) it=c.begin();it!=c.end();++it)
#define pb push_back
#define mp make_pair
#define RI(x) scanf("%d",&x)
#define RID(x) int x;RI(x)
using namespace std;
typedef long long LL;
typedef double LD;
typedef vector<int> VI;
typedef std::pair<int,int> PII;
template<class T>inline void maz(T &a,T b){if(a<b)a=b;}
template<class T>inline void miz(T &a,T b){if(a>b)a=b;}
template<class T>inline T abs(T a){return a>0?a:-a;}
const int N=100, INF=1e9;
const LD EPS=1e-7;

int ori[N];
PII ud[N][N];
int idx[N];

int calc(PII x, PII y){
	int up = min(x.X, y.X);
	int dn = max(x.Y, y.Y);
	if(up<dn) return 0;
	else return 1;
}

int n,p;
int main(){
  openfile("Bs");
	int T, t=0;
	scanf("%d",&T);
	while(t<T){
		t++;printf("Case #%d: ",t);
		scanf("%d %d",&n, &p);
		for(int i=0;i<n;i++) scanf("%d",&ori[i]);
		for(int i=0;i<n;i++){
			for(int j=0;j<p;j++){
				int tmp;
				scanf("%d",&tmp);
				ud[i][j] = mp(tmp*10/(9*ori[i]),(tmp*10+(11*ori[i]-1))/(11*ori[i])); 
			}
		}
		//printf("n,p %d %d\n",n,p);
		int ans = 0;
		for(int i=0;i<p;i++) idx[i] = i;
		do{
			int res = 0;
			for(int j=0;j<p;j++){
				if(n == 1) res += (ud[0][j].X>=ud[0][j].Y);
				else res += calc(ud[0][j],ud[1][idx[j]]);
			}
			//printf("%d ",res);
			ans = max(ans, res);
		}while(next_permutation(idx, idx+p));
		printf("%d\n", ans);

	}
  return 0;
}
