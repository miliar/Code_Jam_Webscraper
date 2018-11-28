#define _CRT_SECURE_NO_DEPRECATE
#include <algorithm>
#include <bitset>
#include <cstdio>
#include <cassert>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <functional>
#include <unordered_map>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <list>
#include <deque>
#include <queue>
#include <math.h>
#include <map>
#include <numeric>
#include <set>
#include <stack>
#include <stdio.h>
#include <string>
#include <sstream>
#include <utility>
#include <vector>

using namespace std;
bool test = false;
const double pi = acos(-1.0);
const double eps = 1e-11;
int breakpoint = 0;

const char rootdir[] = "C:\\CodeJam\\BathroomStalls";
void reopen(char* a) {
  char input[256], output[256];
  sprintf(input, "%s\\%s", rootdir, a);
  sprintf(output, "%s\\%s", rootdir, a);
  char *p = strstr(output, ".in");
  if (p) sprintf(p, ".out");
  else sprintf(&p[strlen(output)], ".out");
  freopen(input, "r", stdin);
  if (!test) freopen(output, "w", stdout);
}

int tt;
__int64 N;
__int64 K;


__int64 inline left(__int64 v) {
  return (v % 2 == 0) ? (v >> 1) - 1 : v >> 1;
}

__int64 inline right(__int64 v) {
  return v >> 1;
}

void solve(int tt) {
  if (test) printf("N=%lld K=%lld\n", N, K);
  // level L has 2^L parts and (2^L-1) occupants
  // L=0: * + + + + + + + + * for k = 1
  // L=1: * + + + * + + + + * for k = 2, 3
  // L=2: * + * + * + * + + * for k = 4, 5, 6, 7
  // L=3: * * * * * * * * + * for k = 8
  __int64 v = K;
  int L = 0;
  while (v > 1) {
    v >>= 1;
    L++;
  }
  // remaining n elements has been split into P=2^L parts
  __int64 ONE = 1;
  __int64 P = (ONE << L);
  __int64 n = N - (P-1);
  // floor of the size of each part is
  __int64 S = n >> L;
  // some of the parts are 1 larer than the floor size
  __int64 r = n % P;
  if (test) printf("%lld\n%lld\n", ((S << L) + r), n);
  assert(((S << L) + r) == n);
  if (test) printf("L:%lld(%lld) S:%lld(%lld)\n", S+1, r, S, P - r);
  __int64 m = K - (P - 1);
  if (m <= r) {
    printf("Case #%d: %lld %lld\n", tt, right(S+1), left(S+1));
  } else {
    printf("Case #%d: %lld %lld\n", tt, right(S), left(S));
  }
}

void incub() {
  vector<__int64> nums;
  nums.push_back(1000);
  for (int i = 0; i < 5; i++) {
    vector<__int64> n2;
    printf("* ");
    for (int k = 0; k < nums.size(); k++) {
      __int64 l = left(nums[k]);
      __int64 r = right(nums[k]);
      n2.push_back(l);
      n2.push_back(r);
      printf("%lld * %lld * ", l, r);
    }
    printf("\n");
    nums.clear();
    nums.insert(nums.begin(), n2.begin(), n2.end());
  }
}

int main() {
  // test = true;
  // reopen("sample.in");
  // reopen("C-small-1-attempt0.in");
  // reopen("C-small-2-attempt0.in");
  reopen("C-large.in");
  int tt;
  N = 12345678987654321L;
  K = 10000000L;
  // solve(0);
  scanf("%d", &tt);
  for (int qq = 1; qq <= tt; qq++) {
    scanf("%lld %lld", &N, &K);
    solve(qq);
  }
  return 0;
}
