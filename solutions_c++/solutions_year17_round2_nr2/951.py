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

map<char,char> C;


int main() {
  int tests; if (scanf("%d",&tests)!=1) return 1;
  C['R']='G'; C['Y']='V'; C['B']='O';
  for (int t=1;t<=tests;++t) {
    printf("Case #%d: ",t);
    int n, r, o, y, g, b, v;
    if (scanf("%d %d %d %d %d %d %d",&n,&r,&o,&y,&g,&b,&v)!=7) return 2;
    r -= g;
    b -= o;
    y -= v;
    map<char,int> N;
    N['R']=r; N['Y']=y; N['B']=b;
    N['G']=g; N['V']=v; N['O']=o;
    string ord = "RYB";
    bool ordered;
    do {
      ordered=true;
      if (N[ord[0]]>N[ord[1]]) { ordered=false; swap(ord[0], ord[1]); }
      if (N[ord[1]]>N[ord[2]]) { ordered=false; swap(ord[1], ord[2]); }
    } while (!ordered);
    if(0) printf("order %s\n",ord.c_str());
    if (N[ord[0]]+N[ord[1]]<N[ord[2]]) {
      printf("IMPOSSIBLE\n");
      continue;
    }
    for (int i=0;i<3;++i) {
      //printf("AAA\n");
      if (N[ord[i]]==0 && N[C[ord[i]]]>0) {
        if (n-2*N[C[ord[i]]]>0) {
          printf("IMPOSSIBLE");
        } else {
          for (int j=0;j<N[C[ord[i]]];++j) printf("%c%c",ord[i],C[ord[i]]);
        }
        printf("\n");
        goto done;
      }
    }
    while (N[ord[2]]>0) {
      //printf("XXX %d %d %d\n",N[ord[0]],N[ord[1]],N[ord[2]]);
      printf("%c",ord[2]); --N[ord[2]];
      while (N[C[ord[2]]]>0) {printf("%c%c",C[ord[2]],ord[2]); --N[C[ord[2]]];}
      if (N[ord[1]]>0) {
        printf("%c",ord[1]); --N[ord[1]];
        while (N[C[ord[1]]]>0) {printf("%c%c",C[ord[1]],ord[1]); --N[C[ord[1]]];}
      }
      if (N[ord[0]]>N[ord[2]]) {
        printf("%c",ord[0]); --N[ord[0]];
        while (N[C[ord[0]]]>0) {printf("%c%c",C[ord[0]],ord[0]); --N[C[ord[0]]];}
      }
    }
    assert(N[ord[0]]==0);
    assert(N[ord[1]]==0);
    assert(N[ord[2]]==0);
    printf("\n");
done:;
  }
}
