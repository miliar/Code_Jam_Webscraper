#include <algorithm>
#include <bitset>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <tuple>
#include <utility>
#include <vector>

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

string solve() {
  string S;
  cin >> S;
  int K;
  cin >> K;
  int c = 0;
  REP(i, S.size() - K + 1) {
    if (S[i] == '-') {
      FOR(j, i, i + K) {
        if (S[j] == '-') {
          S[j] = '+';
        } else {
          S[j] = '-';
        }
      }
      c++;
    }
  }
  if (count(ALL(S), '+') == S.size()) {
    return to_string(c);
  } else {
    return "IMPOSSIBLE";
  }
}

int main() {
  int T;
  cin >> T;
  for (int i = 0; i < T; i++) {
    printf("Case #%d: %s\n", i + 1, solve().c_str());
  }
  return 0;
}
