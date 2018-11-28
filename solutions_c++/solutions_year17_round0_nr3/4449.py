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

long long
find_last_person(long long n, long long k) {
  priority_queue<long long> q;
  long long result;
  q.push(n);

  REP(i, 0, k - 1) {
    long long cur = q.top();
    q.pop();
    q.push(cur / 2);
    q.push((cur - 1) / 2);
  }
  return q.top();
}

int
main(int argc, char *argv[]) {
  int t;
  cin >> t;
  REP(i, 0, t) {
    long long n, k, last;
    cin >> n >> k;
    last = find_last_person(n, k);
    cout << "Case #" << i + 1 << ": " << last / 2 << " " << (last - 1) / 2 << endl;
  }
  return 0;
}
