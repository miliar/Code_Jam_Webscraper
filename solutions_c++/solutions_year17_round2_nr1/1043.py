// CPPFLAGS=-std=c++14 -W -Wall -g -O2
#include <algorithm>
#include <cassert>
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

int main() {
  int tests; if (scanf("%d",&tests)!=1) return 1;
  for (int t=1;t<=tests;++t) {
    printf("Case #%d: ",t);
    int d, s, k, n;
    if (scanf("%d %d",&d,&n)!=2) return 2;
    double best = 1.0/0.0;
    for (int i = 0; i < n; ++i) {
      if (scanf("%d %d",&k,&s)!=2) return 3;
      double x = 1.0 * s / (d - k);
      if (x < best) best = x;
    }
    printf("%.9f\n", d*best);
  }
}
