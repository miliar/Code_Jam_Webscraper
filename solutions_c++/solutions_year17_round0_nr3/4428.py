#include <iostream>
#include <map>
using namespace std;

int main() {
  int t, kase = 0;
  cin >> t;
  while (t--) {
    long long n, k;
    cin >> n >> k;
    long long steps = 0;
    map<long long, long long> p, q;
    p[n] = 1;
    while (steps <= k) {
      q.clear();
      for (auto it = p.rbegin(); it != p.rend(); ++it) {
        if (it->first % 2 == 1) {
          q[it->first / 2] += it->second * 2;
          steps += it->second;
          if (steps >= k) {
            cout << "Case #" << ++kase << ": " << it->first / 2 << " "
                 << it->first / 2 << endl;
            break;
          }
        } else {
          q[it->first / 2] += it->second;
          q[it->first / 2 - 1] += it->second;
          steps += it->second;
          if (steps >= k) {
            cout << "Case #" << ++kase << ": " << it->first / 2 << " "
                 << it->first / 2 - 1 << endl;
            break;
          }
        }
      }
      if (steps >= k) {
        break;
      }
      p = q;
    }
  }
  return 0;
}
