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

double
find_constant_speed(long long d, long long n, long long k[], long long s[]) {
  double speed;
  double max_time = -1;

  REP(i, 0, n) {
    double time = (double) (d - k[i]) / s[i];
    if (max_time < time)
      max_time = time;
  }

  speed = d / max_time;
  return speed;
}

int
main(int argc, char *argv[]) {
  int t;
  cin >> t;
  REP(i, 0, t) {
    long long d, n;
    cin >> d >> n;

    long long k[n];
    long long s[n];

    REP(j, 0, n) {
      cin >> k[j] >> s[j];
    }
    double speed = find_constant_speed(d, n, k, s);
    cout.precision(6);
    cout << fixed << "Case #" << i + 1 << ": " << speed << endl;
  }
  return 0;
}
