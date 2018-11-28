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

void solve() {
  int n, p; if (scanf("%d %d",&n,&p)!=2) exit(2);
  vector<int> counts(p);
  for (int i=0;i<n;++i) {
    int d; if (scanf("%d",&d)!=1) exit(3);
    ++counts[d%p];
  }
  if (p == 2) {
    printf("%d\n", counts[0] + (counts[1]+1)/2);
  } else if (p == 3) {
    int a = counts[0];
    int b = min(counts[1], counts[2]);
    counts[1] -= b;
    counts[2] -= b;
    int c = (counts[1] + 2) / 3;
    int d = (counts[2] + 2) / 3;
    printf("%d\n", a+b+c+d);
  } else if (p == 4) {
    int a = counts[0];
    int b = min(counts[1], counts[3]);
    counts[1] -= b;
    counts[3] -= b;
    int c = counts[2] / 2;
    counts[2] = counts[2] % 2;
    int d = counts[2];
    int e = (counts[1] + 3 - (d==1?2:0)) / 4;
    int f = (counts[3] + 3 - (d==1?2:0)) / 4;
    printf("%d\n", a+b+c+d+e+f);
  } else {
    assert (0);
  }
}

int main() {
  int tests; if (scanf("%d",&tests)!=1) return 1;
  for (int t=1;t<=tests;++t) {
    printf("Case #%d: ",t);
    solve();
  }
}
