#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <cstring>
#include <cmath>
#include <cctype>
#include <sstream>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <bitset>
#include <list>
#include <cstdarg>

#ifndef DBG
#define	DBG	0
#endif

//#define	DBG(f,x)	if(_____debug & f) { x; }
using namespace std;

#define	rep(i,n)	for((i) = 0; (i) < (n); (i)++)
#define	rab(i,a,b)	for((i) = (a); (i) <= (b); (i)++)
#define all(v)		(v).begin(),(v).end()
#define	Fi(n)		rep(i,n)
#define	Fj(n)		rep(j,n)
#define	Fk(n)		rep(k,n)
#define	sz(v)		(v).size()

int main() {
  int T, cs;
  int state[100001];
  int K,N;
  char s[1000001];
  int i,j;

  scanf("%d", &T);

  rab(cs,1,T) {
    scanf("%s %d", s, &K);
    N = strlen(s);

    Fi(N) state[i] = (s[i] == '+');

    int f = 0;

    for (i = 0; i + K <= N; i++) {
      if (state[i] == 1) continue;

      for (j = 0; j < K; j++) {
        state[i + j] = 1 - state[i + j];
      }
      f++;
    }

    for (; i < N; i++) {
      if (state[i] != 1) {
        break;
      }
    }

    if (i < N) {
      printf("Case #%d: IMPOSSIBLE\n", cs);
    } else {
      printf("Case #%d: %d\n", cs, f);
    }
  }

  return 0;
}
