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

const char rootdir[] = "C:\\CodeJam\\AmpleSyrup";
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

int T;
int N;
int K;
struct PANCAKE {
  __int64 R;
  __int64 H;
};
PANCAKE cakes[1024];

int compareCake(const void* a, const void* b) {
  PANCAKE *c1 = (PANCAKE*)a;
  PANCAKE *c2 = (PANCAKE*)b;
  // decreasing lateral area, increasing radius
  __int64 v1 = c1->R * c1->H;
  __int64 v2 = c2->R * c2->H;
  if (v1 > v2) return -1;
  else if (v1 < v2) return 1;
  if (c1->R > c2->R) return 1;
  else if (c1->R < c2->R) return -1;
  return 0;
}

void solve(int tt) {
  // Identify set A --- top K pancakes lateral surface area wise.
  // To break tie, smaller radius first.
  // The top k-1 choosen pancakes must be from the set A.
  // The last one however could be from one of the remaining one.
  qsort(cakes, N, sizeof(PANCAKE), compareCake);

  __int64 pv = 0;
  for (int i = 1; i < N; i++) {
    __int64 pv = 2 * cakes[i-1].R * cakes[i-1].H;
    __int64 v = 2 * cakes[i].R * cakes[i].H;
    assert(v <= pv);
    if (v == pv) {
      assert(cakes[i].R >= cakes[i - 1].R);
    }
  }

  double output = 0;
  __int64 r0 = 0;
  __int64 h0 = 0;
  for (int i = 0; i < K; i++) {
    output += 2.0 * cakes[i].R * cakes[i].H;
    if (cakes[i].R >= r0) {
      r0 = cakes[i].R;
      h0 = cakes[i].H;
    }
  }
  output += r0 * r0;

  __int64 maxd = 0;
  for (int i = K; i < N; i++) {
    __int64 r = cakes[i].R;
    __int64 h = cakes[i].H;
    // only make sense to use if the radius is bigger
    if (r <= r0) continue;
    // if choosen, replace the one with smallest lateral suface area
    __int64 d = r * r - r0 * r0 + 2 * r * h - 2 * cakes[K-1].R * cakes[K-1].H;
    if (d > maxd) {
      maxd = d;
    }
  }

  output += maxd;
  output *= pi;
  printf("Case #%d: %0.9f\n", tt, output);
}

int main() {
  // test = true;
  // reopen("sample.in");
  // reopen("A-small-attempt0.in");
  // reopen("A-small-attempt2.in");
  reopen("A-large.in");


  scanf("%d", &T);
  for (int tt = 1; tt <= T; tt++) {
    scanf("%d %d", &N, &K);
    for (int i = 0; i < N; i++) {
      scanf("%lld %lld", &cakes[i].R, &cakes[i].H);
    }
    if (test && tt != 26) continue;
    solve(tt);
  }
  return 0;
}
