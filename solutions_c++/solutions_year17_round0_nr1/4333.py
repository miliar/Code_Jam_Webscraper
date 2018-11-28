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

void
print_pancake(bool arr[], int n) {
  REP(i, 0, n) {
    cout << (arr[i] ? '+' : '-');
  }
  cout << endl;
}

int
find_flipper_num(string s, int k) {
  int len = s.length();
  bool arr[len];
  REP(i, 0, len) {
    arr[i] = s[i] == '-' ? false : true;
  }

  int count = 0;
  REP(i, 0, len - k + 1) {
    if (!arr[i]) {
      count += 1;
      for (int j = i; j < i + k; j++) {
        arr[j] = !arr[j];
      }
    }
  }
  REP(i, len - k + 1, len) {
    if (!arr[i])
      return -1;
  }
  return count;
}

int
main(int argc, char *argv[]) {
  int t;
  cin >> t;
  REP(i, 0, t) {
    string s;
    int k;
    int result;
    cin >> s >> k;
    result = find_flipper_num(s, k);
    cout << "Case #" << i + 1 << ": " << (result < 0 ? "IMPOSSIBLE" : to_string(result)) << endl;
  }
  return 0;
}
