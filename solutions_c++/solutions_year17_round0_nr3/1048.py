#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <set>
#include <string>
#include <utility>

using namespace std;

template<typename T> T next() { T tmp; cin >> tmp; return tmp; }

using ull = unsigned long long;

void solve() {
  ull n = next<ull>();
  ull k = next<ull>();
  map<ull, ull> cur;
  cur[n] += 1;
  while (k > 0) {
    ull val = cur.rbegin()->first;
    if (k > cur[val]) {
      k -= cur[val];
      cur[val / 2] += cur[val];
      cur[(val - 1) / 2] += cur[val];
      cur.erase(val);
    } else {
      break;
    }
  }
  ull val = cur.rbegin()->first;
  cout << val / 2 << " " << (val - 1) / 2 << endl;
}

int main() {
  int n = next<int>();
  for (int i = 1; i <= n; ++i) {
    cout << "Case #" << i << ": ";
    solve();
  } 
  return 0;
}
