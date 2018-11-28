#include <iostream>
#include <map>

using namespace std;

typedef long long s64;

int main() {
  int t; cin >> t;
  for (int tt = 1; tt <= t; tt++) {
    s64 n, k; cin >> n >> k;
    k--;

    map<s64, s64> m[2];
    int curr = 0, next = 1;
    s64 powOf2 = 1;
    m[curr][n] = 1;
    while (k >= powOf2) {
      k -= powOf2;
      m[next].clear();
      for (map<s64, s64>::iterator it(m[curr].begin()); it != m[curr].end(); it++) {
        s64 l = (it->first-1) / 2;
        s64 h = (it->first-1) - l;
        m[next][l] += it->second;
        m[next][h] += it->second;
      }
      powOf2 <<= 1;
      curr = next;
      next = 1-curr;
    }
    for (map<s64, s64>::reverse_iterator rit(m[curr].rbegin()); rit != m[curr].rend(); rit++) {
      if (k < rit->second) {
        s64 l = (rit->first-1) / 2;
        s64 h = (rit->first-1) - l;
        cout << "Case #" << tt << ": " << h << " " << l << endl;
        break;
      }
      k -= rit->second;
    }
  }
  return 0;
}

