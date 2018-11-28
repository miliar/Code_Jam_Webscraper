// pre-written code {{{
#include <cstdio>
#include <cmath>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <queue>
#include <numeric>
#include <iostream>
#include <cassert>
#include <set>
#include <sys/resource.h>
#define FOR(i,n) for(int _n=n,i=0;i<_n;++i)
#define FR(i,a,b) for(int _b=b,i=a;i<_b;++i)
#define CL(x) memset(x,0,sizeof(x))
#define PN printf("\n");
#define MP make_pair
#define PB push_back
#define SZ size()
#define ALL(x) x.begin(),x.end()
#define FORSZ(i,v) FOR(i,v.size())
#define FORIT(it,x) for(__typeof(x.begin()) it=x.begin();it!=x.end();it++)
using namespace std;
typedef vector<int> VI;
typedef vector<string> VS;
typedef long long LL;
void stackSizeUnlimited() { struct rlimit rl; getrlimit(RLIMIT_STACK, &rl); rl.rlim_cur = RLIM_INFINITY; setrlimit(RLIMIT_STACK, &rl); }
///////////////////////////////////////////////////////////////////////////////////
// }}}

int n,q;

int maxdist[105];
double speed[105];
int dist[105][105];
long long sdist[105][105];
double tim[105];
bool used[105];

void solve(){
  scanf("%d %d",&n,&q);
  FOR(i,n) {
    scanf("%d %lf",&maxdist[i], &speed[i]);    
  }
  FOR(i,n) {
    FOR(j,n) {
      scanf("%d",&dist[i][j]);
    }
  }
  
  FOR(i,n) FOR(j,n) sdist[i][j] = dist[i][j];
  FOR(k,n) {
    FOR(i,n) FOR(j,n) if(sdist[i][k]!=-1 && sdist[k][j]!=-1) 
      if(sdist[i][k] + sdist[k][j] < sdist[i][j] || sdist[i][j] == -1) {
        sdist[i][j] = sdist[i][k] + sdist[k][j];
      }
  }
  
  /*
  FOR(i,n) {
    FOR(j,n) printf(" %d",sdist[i][j]);
    PN;
  }
  */
  

  FOR(qq,q) {
    int start, target;
    scanf("%d %d",&start, &target); start--; target--;
    FOR(i,n) tim[i] = 1e20;
    FOR(i,n) used[i] = false;
    priority_queue<pair<double, int > > Q; 
    Q.push(MP(0.0, start) );
    while(!Q.empty()) {
      double t = -Q.top().first;
//      printf("t: %.3lf\n",t);
      int city = Q.top().second;
      Q.pop();
      if(used[city]) continue;
      used[city]= true;
      FOR(i,n) if(!used[i]) if(sdist[city][i]!=-1) if(sdist[city][i] <= maxdist[city] ) {
        double ntime = (t + sdist[city][i] / speed[city]);
        if(ntime < tim[i]) {
          Q.push(MP(-ntime, i));
          tim[i] = ntime;
        }
      }
    }
    if(qq!=0) printf(" ");
    printf("%.9lf", tim[target]);
  }
  PN;
}

int main(){
  stackSizeUnlimited();
  int pvs; scanf("%d",&pvs);
  FR(ppp,1,pvs+1){
     printf("Case #%d: ",ppp);

     solve();
  }
}


// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
