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

const char rootdir[] = "C:\\CodeJam\\OversizedPancakeFlipper";
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
char S[1024];
int K;

void solve(int tt) {
  int N = strlen(S);
  int count = 0;
  for (int i = 0; i < N; i++) {
    if (S[i] == '+') continue;
    if (i + K > N) {
      count = -1;
      break;
    }
    for (int j = 0; j < K; j++) {
      S[i + j] = (S[i + j] == '+') ? '-' : '+';
    }
    count++;
  }
  if (count == -1) {
    printf("Case #%d: IMPOSSIBLE\n", tt);
  } else {
    printf("Case #%d: %d\n", tt, count);
  }
}

int main() {
  // test = true;
  // reopen("sample.in");
  // reopen("A-small-attempt0.in");
  reopen("A-large.in");

  int tt;
  scanf("%d", &tt);
  for (int qq = 1; qq <= tt; qq++) {
    scanf("%s %d", S, &K);
    solve(qq);
  }
  return 0;
}
