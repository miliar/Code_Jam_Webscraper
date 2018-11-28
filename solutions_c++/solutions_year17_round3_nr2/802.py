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

int DMIN = 1440;
int Ac, Aj;
int Ctime, Jtime;
int gr[3];
int time_slot[3000];

int solve(int st, int sp){
  int r[3];
  r[1] = gr[1], r[2] = gr[2];
  int nsp = sp;
  int res = 0;
  FOR(i, DMIN){
    if(time_slot[i+st] == 0){
      if(r[nsp] > 0) r[nsp] --;
      else{
        res ++;
        nsp = 3-nsp;
        //printf("c at %d, ", i+st);
        r[nsp] --;
      }
    }
    else if(time_slot[i+st] != nsp){
      res++;
      nsp = 3-nsp;
      //printf("c at %d, ", i+st);
    }
  }
  assert(r[1] == 0 && r[2] == 0);
  if(sp != nsp) res++;
  //printf("res %d\n", res);
  return res;
}

int main(){
  //openfile("A");
  int T, t=0;
  RI(T);
  while(t++<T){
    printf("Case #%d: ", t);
    RI(Ac); RI(Aj);
    Ctime = Jtime = 0;
    memset(time_slot,0,sizeof(time_slot));
    FOR(i, Ac){
      RID(c); RID(d);
      Ctime += d-c;
      for(int j=c; j<d;j++) time_slot[j+DMIN] = time_slot[j] = 1;
    }
    FOR(i, Aj){
      RID(c); RID(d);
      Jtime += d-c;
      for(int j=c; j<d;j++) time_slot[j+DMIN] = time_slot[j] = 2;
    }
    gr[1] = 720 - Ctime, gr[2] = 720 - Jtime;
    int ans = 1<<30;
    FOR(i, DMIN){
      for(int j=1;j<=2;j++){
        int res = solve(i, j);
        if(res < ans) ans = res;
      }
    }
    printf("%d\n", ans);
  }
  return 0;
}
