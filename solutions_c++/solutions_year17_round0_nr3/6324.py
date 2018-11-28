#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

int main() {
  int t;
  cin >> t;
  for (int _ = 1; _ <= t; _++) {
    long long n = 0;
    long long k = 0;
    long long l = 0;
    long long r = 0;
    cin >> n >> k;
    priority_queue<long long, std::vector<long long>> q;
    q.push(n);
    for (long long i = 0; i < k; ++i) {
      long long top = q.top();
      q.pop();
      r = top / 2;
      l = top - r;
      if (l < r) {
        r--;
      } else {
        l--;
      }
      q.push(l);
      q.push(r);
      //cout << top << ' ' << q.size() << endl;
    }
    cout << "Case #" << _ << ": " << max(r, l) << ' ' << min(l, r) << endl;
  }
}
