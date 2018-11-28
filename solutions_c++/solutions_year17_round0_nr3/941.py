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

struct Section {
  long size;
  long count;

  bool operator < (const Section &s) {
    return size > s.size;
  }
};

int main() {
  int T,cs;
  long N,K;
  long total = 0;

  Section list1[100000], list2[100000];
  int l1,l2;
  Section *list,*next;
  int *len,*next_len;
  int i;

  scanf("%d", &T);

  rab(cs,1,T) {
    scanf("%ld %ld",&N,&K);

    list = list1;
    next = list2;
    len = &l1;
    next_len = &l2;
    total = 0;

    list[0].size = N;
    list[0].count = 1;
    *len = 1;
    long y, z;

    while (true) {
      *next_len = 0;

      //printf("---------------------------------------\n");

      for (i = 0; i < *len; i++) {
        long d = list[i].size - 1;

        //printf("d = %ld\n", d);

        y = (d + 1) / 2;
        z = d / 2;
        Section s1, s2;
        s1.count = s2.count = list[i].count;
        s1.size = y;
        s2.size = z;
        next[(*next_len)++] = s1;
        next[(*next_len)++] = s2;

        if (total + list[i].count >= K) {
          break;
        }
        total += list[i].count;

        //printf("total = %ld\n", total);
      }
      if (i < *len) break;

      sort(next, next + *next_len);

      int j = 0;

      for (i = 1; i < *next_len; i++) {
        if (next[j].size == next[i].size) {
          next[j].count += next[i].count;
        } else {
          next[++j] = next[i];
        }
      }
      *next_len = j + 1;

      swap(list, next);
      swap(*len, *next_len);
    }

    printf("Case #%d: %ld %ld\n", cs, y, z);
  }

  return 0;
}
