#include <vector>
#include <list>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <stack>
#include <algorithm>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <limits>
#include <cstring>
#include <string>
#include <cassert>
using namespace std;

typedef long long llong;
typedef pair<int,int> pairii;
typedef pair<llong,llong> pairll;

#define FOR(i,s,n) for (int (i) = (s); (i) < (n); (i)++)
#define FORZ(i,n) FOR((i),0,(n))
#define memclear(ar) memset((ar), 0, sizeof(ar))
#define pb push_back

int n,c,m;
typedef vector<int> VI;
typedef vector<VI> VVI;
VVI tk;

bool bpm(int i, const VVI &w, VI &mr, VI &mc, VI &vis) {
  FORZ(j,w[i].size()) {
    if (w[i][j] && !vis[j]) {
      vis[j] = true;
      if (mc[j] < 0 || bpm(mc[j], w, mr, mc, vis)) {
        mr[i] = j;
        mc[j] = i;
        return true;
      }
    }
  }
  return false;
}

int maxBPM(const VVI &w, VI &mr, VI &mc) {
  mr = VI(w.size(), -1);
  mc = VI(w[0].size(), -1);
  int res = 0;
  for (int i = 0; i < w.size(); i++) {
    VI vis(w[0].size());
    if (bpm(i, w, mr, mc, vis)) res++;
  }
  return res;
}

void solve() {
  scanf("%d%d%d",&n,&c,&m);
  tk.clear();
  tk.resize(c);
  FORZ(i,m) {
    int x,y;
    scanf("%d%d",&x,&y);
    y--;
    tk[y].pb(x);
  }
  if (tk[0].empty()) {
    printf("%d 0\n",(int)tk[1].size());
    return;
  }
  if (tk[1].empty()) {
    printf("%d 0\n",(int)tk[0].size());
    return;
  }
  VVI w;
  w.resize(tk[0].size());
  FORZ(i,tk[0].size()) w[i].resize(tk[1].size());
  FORZ(i,w.size()) {
    FORZ(j,w[i].size()) {
      if (tk[0][i]!=tk[1][j]) w[i][j]=1;
      else w[i][j]=0;
    }
  }
  VI mr,mc;
  int res = maxBPM(w,mr,mc);
  int bad=-1, mrs=0, mcs=0;
  FORZ(i,mr.size()) {
    if (mr[i]==-1) {
      mrs++;
      if (bad==-1) {
        bad=tk[0][i];
      } else if (bad!=tk[0][i]) {
        //printf("ERROR: bad=%d, tk[0][%d]=%d\n", bad, i, tk[0][i]);
      }
    }
  }
  FORZ(j,mc.size()) {
    if (mc[j]==-1) {
      mcs++;
      if (bad==-1) {
        bad=tk[1][j];
      } else if (bad!=tk[1][j]) {
        //printf("ERROR: bad=%d, tk[1][%d]=%d\n", bad, j, tk[1][j]);
      }
    }
  }
  if (bad==1 || bad==-1) {
    res+=mrs+mcs;
    printf("%d 0\n",res);
  } else {
    res+=max(mrs, mcs);
    int pr = min(mrs, mcs);
    printf("%d %d\n",res,pr);
  }
}

int main() {
#ifdef DEBUG
  freopen("../CodeforcesB/in.txt", "r", stdin);
  freopen("../CodeforcesB/out.txt", "w", stdout);
#endif
  
  int t;
  scanf("%d", &t);
  FOR(i,1,t+1) {
    printf("Case #%d: ", i);
    solve();
  }
  
  return 0;
}
