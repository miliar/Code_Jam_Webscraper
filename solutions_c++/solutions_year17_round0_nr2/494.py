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

const char rootdir[] = "C:\\CodeJam\\TidyNumbers";
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
char buf[32];

void solve(int tt) {
  char buf[32];
  __int64 m = N;
  int idx = 0;
  while (m > 0) {
    buf[idx++] = m % 10 + '0';
    m /= 10;
  }
  buf[idx] = 0;
  for (int i = 0; i < idx / 2; i++) {
    swap(buf[i], buf[idx - 1 - i]);
  }
  // find first decrease, forward change to 9
  int i = 0;
  while (i < idx - 1 && buf[i] <= buf[i + 1]) i++;
  if (i == idx - 1) {
    printf("Case #%d: %s\n", tt, buf);
    return;
  }
  buf[i]--;
  for (int j = i + 1; j < idx; j++) {
    buf[j] = '9';
  }
  while (i > 0 && buf[i] < buf[i - 1]) {
    buf[i] = '9';
    buf[i - 1]--;
    i--;
  }
  int k = 0;
  while (buf[k] == '0') k++;
  printf("Case #%d: %s\n", tt, &buf[k]);
}

int main() {
  // test = true;
  // reopen("sample.in");
  // reopen("B-small-attempt0.in");
  reopen("B-large.in");

  int tt;
  scanf("%d", &tt);
  for (int qq = 1; qq <= tt; qq++) {
    scanf("%lld", &N);
    solve(qq);
  }
  return 0;
}
