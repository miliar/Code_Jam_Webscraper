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
#include <cinttypes>

using namespace std;

//#define all(c) (c).begin(),(c).end()
//#define foreach(i,c) for(auto i=(c).begin();i!=(c).end();++i)
template<class T> bool in(T e, const set<T>& s) { return s.find(e) != s.end(); }
template<class K, class V> bool in(K k, const unordered_map<K,V>& h) { return h.find(k) != h.end(); }

int main() {
  int tests; if (scanf("%d",&tests)!=1) return 1;
  map<int64_t,int64_t> M;
  for (int t=1;t<=tests;++t) {
    printf("Case #%d: ",t);
    int64_t n, k;
    if (scanf("%ld %ld",&n,&k)!=2) return 2;
    M.clear();
    M[n] = 1;
    --k;
    while (k > 0) {
      n = M.rbegin()->first;
      assert (M[n] > 0);
      int64_t r = min(k, M[n]);
      k -= r; M[n] -= r;
      M[n/2] += r; M[(n-1)/2] += r;
      if (M[n] == 0) M.erase(n);
    }
    n = M.rbegin()->first;
    printf("%" PRIi64 " %" PRIi64 "\n", n/2, (n-1)/2);
  }
}
