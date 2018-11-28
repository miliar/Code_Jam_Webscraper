#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <map>
#include <set>
#include <stack>
#include <string>
#include <vector>
#include <queue>

using namespace std;

#define TRACE(x) cerr << #x << " " << x << endl
#define FOR(i, a, b) for (int i = (a); i < int(b); ++i)
#define REP(i, n) FOR(i, 0, n)
#define _ << " " <<

#define fst first
#define snd second

typedef long long llint;
typedef pair<int, int> pii;

const int B = 27397, MOD = 1e9 + 7;
const int B1 = 33941, MOD1 = 1e9 + 9;

char n[20];

int t, len;

void solve(int t) {
  scanf("%s", n);
  len = strlen(n);

  for (int i = 1; i < len; ++i) {
    if (n[i] < n[i - 1]) {
      int j = i - 1;
      while (j >= 0 && n[j] == n[i - 1])
        --j;
      ++j;
      --n[j++];
      while (j < len)
        n[j++] = '9';
      break;
    }
  }

  printf("Case #%d: ", t);

  if (n[0] == '0') {
    for (int i = 0; i < len - 1; ++i)
      printf("9");
    printf("\n");
  } else {
    printf("%s\n", n);
  }

}

int main(void) {
  scanf("%d", &t);
  for (int i = 0; i < t; ++i)
    solve(i + 1);
  return 0;
}
