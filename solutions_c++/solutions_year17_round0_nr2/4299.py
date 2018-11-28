#include <iostream>
#include <iterator>
#include <functional>
#include <algorithm>
#include <vector>
#include <string>
#include <list>
#include <map>
#include <set>
#include <bitset>
#include <stack>
#include <queue>
#include <deque>
#include <cstdlib>
#include <cmath>

using namespace std;

#define REP(i, a, n) for (int i = a; i < (int) n; i++)
#define FOR_ITER(c, it) for (typeof(c.begin()) it = c.begin(); it != c.end(); it++)
#define ALL(c) (c).begin(), (c).end()

const int MOD = 1000000007;
const double EPSILON = 1e-10;

bool
is_tidy(long long n) {
  long long cur = n;
  long long next = cur / 10;

  while (next > 0) {
    if ((next % 10) > (cur % 10))
      return false;
    cur = cur / 10;
    next = cur / 10;
  }
  return true;
}

long long
find_last_tidy(long long n) {
  long long result = n;
  int idx = 1;
  while (!is_tidy(result)) {
    long long base = pow(10, idx);
    result = n - (n % base) - 1;
    idx += 1;
  }
  return result;
}

int
main(int argc, char *argv[]) {
  int t;
  cin >> t;
  REP(i, 0, t) {
    long long n;
    long long result;
    cin >> n;
    result = find_last_tidy(n);
    cout << "Case #" << i + 1 << ": " << result << endl;
  }
  return 0;
}
