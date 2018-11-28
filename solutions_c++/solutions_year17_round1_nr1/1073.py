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
const int N=100100, INF=1e9;
const LD EPS=1e-7;

int R,C;
char board[30][30];

bool fill_one(char *row, int r)
{
	int sp=0;
	char nc;
	for(sp=0;row[sp]=='?';sp++);
	if(sp == r) return false;
	nc = row[sp];
	for(int i=0;i<r;i++){
		if(row[i] == '?') row[i] = nc;
		else nc = row[i];
	}
	//puts(row);
	return true;
}

int main(){
  openfile("As");
	//fill_one("?2?4?",5);
	int T;
	scanf("%d",&T);
	int t = 0;
	while(t<T) {
		t++; printf("Case #%d:\n",t);
		scanf("%d %d",&R,&C);
		for(int i=0;i<R;i++) scanf("%s",board[i]);
		int sr = 0; bool w=false;
		for(int i=0;i<R;i++){
			if(fill_one(board[i], C)){
				if(!w){
					sr = i;
					w=true;
				}
			} else{
				if(w) memcpy(board[i],board[i-1], sizeof(char)*(C+1));
			}
		}
		for(int i=0;i<sr;i++)
			memcpy(board[i],board[sr], sizeof(char)*(C+1));
		for(int i=0;i<R;i++) puts(board[i]);
	}
  return 0;
}
