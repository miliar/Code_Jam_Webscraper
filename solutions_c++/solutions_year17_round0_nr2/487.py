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
  char n[32];
  int sz;
  for (int t=1;t<=tests;++t) {
    printf("Case #%d: ",t);
    if (scanf("%s",n)!=1) return 2;
    sz = strlen(n);
    int i;
    for (i = 1; i < sz && n[i-1] <= n[i]; ++i);
    if (i < sz) {
      --i;
      while (i > 0 && n[i-1] == n[i]) --i;
      --n[i++];
      while (i < sz) n[i++] = '9';
    }
    printf("%s\n", n+(n[0]=='0'));
  }
}
