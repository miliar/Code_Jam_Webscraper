/*
 *
 * CodeJam 2017 - Qualification Round
 * Problem 3
 *
 */

#include <cassert>
#include <iostream>
#include <math.h>
#include <queue>

using namespace std;

struct R { long long y, z; };

void print_queue(priority_queue<long long> q) {
  while (!q.empty()) {
    cout << q.top() << " ";
    q.pop();
  }
  cout << endl;
}

R stalls(long long n, long long k) {
  long long y = 0, z = 0;
  priority_queue<long long> q;
  q.push(n);
  for (long long i = 0; i < k; ++i) {
    // print_queue(q);
    y = ceil((q.top() - 1) / 2.00000000000000000000);
    z = floor((q.top() - 1) / 2.00000000000000000000);
    if (y != 0) q.push(y);
    if (z != 0) q.push(z);
    q.pop();
  }
  return {y, z};
}

int main() {
  int t;
  cin >> t;

  for (int i = 1; i <= t; ++i) {
    long long n, k;
    cin >> n >> k;
    printf("Case #%d: ", i);
    auto r = stalls(n, k);
    cout << r.y << " " << r.z << endl;
  }

  return 0;
}
