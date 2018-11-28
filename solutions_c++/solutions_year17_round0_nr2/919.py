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

long last[19];
long power[19];

long get_last(long prefix, int prev, int remain_length, long s) {
  if (remain_length == 0) return prefix <= s ? prefix : 0;
  long ret = 0,c;
  for (int i = prev; i <= 9; i++) {
    long np = (prefix * 10 + i);
    if (np * power[remain_length - 1] > s) break;
    long c = np * power[remain_length - 1] + last[remain_length - 1];
    if (c < ret) {
      ret = c;
    } else {
      c = get_last(np, i, remain_length - 1, s);
      if (c > ret) ret = c;
    }
  }
  return ret;
}

int main() {
  int i,j;
  long p;

  last[0] = 0;
  power[0] = 1;

  for (i = 1; i <= 18; i++) {
    last[i] = last[i - 1] * 10 + 9;
    power[i] = power[i - 1] * 10;
  }

  int T, cs;
  long l,s;

  scanf("%d", &T);

  rab(cs, 1, T) {
    scanf("%ld", &s);

    long largest = 0;
    int i;

    for (i = 1; i <= 18; i++) {
      if (last[i] > s) {
        break;
      }
      largest = max(largest, last[i]);
    }

    if (i <= 18) {
      long c = get_last(0, 1, i, s);
      if (c > largest) largest = c;
    }

    printf("Case #%d: %ld\n", cs, largest);
  }
  
  return 0;
}
