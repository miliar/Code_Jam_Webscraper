// CPPFLAGS=-std=c++11 -W -Wall -g -O2
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
  char s[1024];
  int k;
  int n;
  int flips;
  for (int t=1;t<=tests;++t) {
    printf("Case #%d: ",t);
    if (scanf("%s %d",s,&k)!=2) return 2;
    n = strlen(s);
    flips = 0;
    int i, j;
    for (i = 0; i + k <= n; ++i) if (s[i] == '-') {
      ++flips;
      for (j = i; j < i + k; ++j) s[j] = (s[j] == '+')? '-' : '+';
    }
    while (i < n && s[i] == '+') ++i;
    if (i < n) printf("IMPOSSIBLE");
    else printf("%d", flips);
    printf("\n");
  }
}
