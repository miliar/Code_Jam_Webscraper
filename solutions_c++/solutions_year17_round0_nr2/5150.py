#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <limits>
#include <tuple>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <climits>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <complex>

using namespace std;

typedef long long ll;
typedef unsigned int uint;
typedef unsigned long long ull;
static const double EPS = 1e-12;
static const double PI = acos(-1.0);

#define FOR(i, a, b) for (int i = (int)(a); i < (int)(b); i++)
#define REP(i, n) for (int i = 0; i < (int)(n); i++)
#define ALL(a) (a).begin(), (a).end()
#define DEBUG(x) cout << #x << ": " << x << endl

string get_next(string N) {
  int cur = 0;
  int i;
  for (i = 0; i < (int)N.size(); i++) {
    int x = N[i] - '0';
    if (cur > x) {
      break;
    }
    cur = x;
  }
  if (i == (int)N.size()) {
    return N;
  }
  i--;
  int y = N[i] - '0';
  N[i] = (y - 1) + '0';
  i++;
  for (; i < (int)N.size(); i++) {
    N[i] = '9';
  }
  if (N[0] == '0') {
    return N.substr(1);
  }
  return N;
}

string solve() {
  string N;
  cin >> N;
  while (true) {
    string M = get_next(N);
    if (M == N) {
      return N;
    }
    N = M;
  }
  return N;
}

int main() {
  int T;
  cin >> T;
  for (int i = 0; i < T; i++) {
    printf("Case #%d: %s\n", i + 1,  solve().c_str());
  }
  return 0;
}
