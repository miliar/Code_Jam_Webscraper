#include <cstdio>
#include <cassert>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <algorithm>
#include <vector>
#include <iostream>
#include <string>
#include <map>
#include <set>
#include <utility>
#include <sstream>
using namespace std;
typedef long long ll;

void solve() {
  ll N, K;
  scanf("%lld%lld", &N, &K);
  ll e = 0, o = 0;
  ll ne, no, Ne, No;
  e = 1;
  /*
  if (N % 2 == 0) {
    e = 1;
  } else {
    o = 1;
    }*/
  
  for (;;) {
    if (e + o >= K) {
      if (N % 2 == 1 && K <= e) {
	printf("%lld %lld\n", N/2, N/2);
      } else if ((N % 2 == 0 && K <= e) ||
		 (N % 2 == 1 && K > e)) {
	printf("%lld %lld\n", N/2, max((ll)0,N/2 - 1));
      } else {
	printf("%lld %lld\n", max((ll)0,N/2 - 1), max((ll)0,N/2 - 1));
      }
      return;
    }
    K -= e + o;
    //ne = e;
    //no = 2 * o + e;
    if (N % 2 == 0) {
      ne = e;
      no = 2 * o + e;
    } else {
      ne = 2 * e + o;
      no = o;
    }
    e = ne;
    o = no;
    //printf("%lld %lld\n", e, o);
    N /= 2;
  }
}

int main() {
  int T;
  scanf(" %d", &T);
  for (int ii = 0; ii < T; ii++) {
    printf("Case #%d: ", ii + 1);
    solve();
  }
}
