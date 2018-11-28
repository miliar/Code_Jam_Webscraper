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

struct disk {
  int r, h;
  bool operator < (const disk& o) const {
    if (r != o.r) return o.r < r;
    return o.h < h;
  }
};

int main() {
  const double pi = acos(-1);
  int tests; if (scanf("%d",&tests)!=1) return 1;
  for (int t=1;t<=tests;++t) {
    printf("Case #%d: ",t);
    int n, k; if (scanf("%d %d",&n,&k)!=2) return 2;
    vector<disk> D;
    for (int i=0;i<n;++i) {
      disk d; if (scanf("%d %d",&d.r,&d.h)!=2) return 3;
      D.push_back(d);
    }
    sort(D.begin(), D.end());
    vector<vector<double>> S(k, vector<double>(n));
    for (int j=0;j<n;++j) {
      S[0][j] += 2.0 * pi * D[j].r * D[j].h;
      S[0][j] += pi * D[j].r * D[j].r;
    }
    for (int i=1;i<k;++i) for (int j=0;j<n;++j) {
      if (0) printf("oops %d %d\n",i,j);
      for (int jj=0;jj<j;++jj) S[i][j] = max(S[i][j],S[i-1][jj]);
      S[i][j] += 2.0 * pi * D[j].r * D[j].h;
    }
    double best = 0.0;
    for (int j=0;j<n;++j) best = max(best, S[k-1][j]);
    printf("%.9g\n",best);
  }
}
