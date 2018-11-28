// CPPFLAGS=-std=c++14 -W -Wall -g -O2
#include <algorithm>
#include <cassert>
#include <cinttypes>
#include <cmath>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <limits>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <unordered_map>
#include <vector>

using namespace std;

//#define all(c) (c).begin(),(c).end()
//#define foreach(i,c) for(auto i=(c).begin();i!=(c).end();++i)
template<class T> bool in(T e, const set<T>& s) { return s.find(e) != s.end(); }
template<class K, class V> bool in(K k, const unordered_map<K,V>& h) { return h.find(k) != h.end(); }

const int inf = 0x3fffffff;

int main() {
  int tests; if (scanf("%d",&tests)!=1) return 1;
  for (int t=1;t<=tests;++t) {
    printf("Case #%d: ",t);
    int Ac, Aj; if (scanf("%d %d\n",&Ac,&Aj)!=2) return 2;
    vector<bool> Cfree(24*60,true), Jfree(24*60,true);
    for (int i=0;i<Ac;++i) {
      int c, d; if (scanf("%d %d",&c,&d)!=2) return 3;
      for (int j=c;j<d;++j) Cfree[j] = false;
    }
    for (int i=0;i<Aj;++i) {
      int c, d; if (scanf("%d %d",&c,&d)!=2) return 4;
      for (int j=c;j<d;++j) Jfree[j] = false;
    }
    vector<vector<int>> CC(24*60+1,vector<int>(24*60+1,inf));
    vector<vector<int>> CJ(24*60+1,vector<int>(24*60+1,inf));
    vector<vector<int>> JC(24*60+1,vector<int>(24*60+1,inf));
    vector<vector<int>> JJ(24*60+1,vector<int>(24*60+1,inf));
    if (Cfree[0]) CC[1][1] = 0;
    if (Jfree[0]) JJ[1][0] = 0;
    for (int i=1;i<24*60;++i) for (int j=0;j<=i;++j) {
      if (CC[i][j] != inf) {
        if (Cfree[i]) { CC[i+1][j+1] = min(CC[i+1][j+1],CC[i][j]); }
        if (Jfree[i]) { CJ[i+1][j] = min(CJ[i+1][j],CC[i][j]+1); }
      }
      if (CJ[i][j] != inf) {
        if (Cfree[i]) CC[i+1][j+1] = min(CC[i+1][j+1],CJ[i][j]+1);
        if (Jfree[i]) CJ[i+1][j] = min(CJ[i+1][j],CJ[i][j]);
      }
      if (JC[i][j] != inf) {
        if (Cfree[i]) JC[i+1][j+1] = min(JC[i+1][j+1],JC[i][j]);
        if (Jfree[i]) JJ[i+1][j] = min(JJ[i+1][j],JC[i][j]+1);
      }
      if (JJ[i][j] != inf) {
        if (Cfree[i]) JC[i+1][j+1] = min(JC[i+1][j+1],JJ[i][j]+1);
        if (Jfree[i]) JJ[i+1][j] = min(JJ[i+1][j],JJ[i][j]);
      }
    }
    int best = inf;
    best = min(best, CC[1440][720]);
    best = min(best, JJ[1440][720]);
    best = min(best, JC[1440][720]+1);
    best = min(best, CJ[1440][720]+1);
    printf("%d\n",best);
  }
}
