#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
#include <string.h>

using namespace std;

const double pi = acos(-1.0);
const double eps = 1E-7;

typedef long long int64;
typedef unsigned long long uint64;
#define two(X) (1<<(X))
#define twoL(X) (((int64)(1))<<(X))
#define contain(S,X) (((S)&two(X))!=0)
#define containL(S,X) (((S)&twoL(X))!=0)
#define sqr(x) ((x)*(x))
#define Abs(x) ((x) < 0 ? (-(x)) : (x))
typedef pair<int,int> ipair;
#define SIZE(A) ((int)A.size())
#define MP(A,B) make_pair(A,B)
#define PB(X) push_back(X)
#define ME(a) memset((a), 0, sizeof((a)))
#define MM(a, b) memcpy((a), (b), sizeof((a)))
#define FOR(i,n) for (int (i) = 0; (i) < (n); ++(i))
#define REP(i,a,b) for (int (i) = (a); (i) < (b); ++(i))

int n, p, a[100];
int Tests;

int main() {
  scanf("%d", &Tests); 
  for (int tts = 0; Tests--; ) {
    scanf("%d%d", &n, &p);
    for (int i = 0; i < p; ++i) a[i] = 0;
    for (int i = 0; i < n; ++i) {
      int x;
      scanf("%d", &x);
      ++a[x % p];
    }

    printf("Case #%d: ", ++tts);

    if (p == 2) {
      printf("%d\n", a[0] + ((a[1] + 1) / 2));
    } else if (p == 3) {
      int t = min(a[1], a[2]) + (max(a[1], a[2]) - min(a[1], a[2]) + 2) / 3;
      printf("%d\n", a[0] + t);
    } else if (p == 4) {
      int t = min(a[1], a[3]) + a[2] / 2;
      int tt = max(a[1], a[3]) - min(a[1], a[3]);
      if (a[2] % 2) {
        tt = (tt + 1) / 4 + 1;
      } else {
        tt = (tt + 3) / 4;
      }
      printf("%d\n", a[0] + t + tt);
    }
  }
  return 0;
}