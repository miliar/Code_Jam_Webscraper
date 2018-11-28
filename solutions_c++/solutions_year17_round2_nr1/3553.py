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

const char rootdir[] = "C:\\CodeJam\\CruiseControl_2017R1B";
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
int D;
struct Horse {
  int k;
  int s;
};
Horse h[1024];

void solve(int tt) {
  double DD = D;
  double tmax = (DD - h[1].k) / h[1].s;
  for (int i = 2; i <= N; i++) {
    double t = (DD - h[i].k) / h[i].s;
    tmax = std::max(tmax, t);
  }
  double v = DD / tmax;
  printf("Case #%d: %0.6f\n", tt, v);
}


int main() {
  // test = true;
  // reopen("sample.in");
  // reopen("A-small-attempt0.in");
  reopen("A-large.in");

  scanf("%d", &T);
  for (int tt = 1; tt <= T; tt++) {
    scanf("%d %d", &D, &N);
    for (int i = 1; i <= N; i++) {
      scanf("%d %d", &h[i].k, &h[i].s);
    }
    solve(tt);
  }
  return 0;
}
