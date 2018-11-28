#include <iostream>
#include <map>
#include <vector>
using namespace std;

map<vector<int>, int> m;
int p;

int f(vector<int>& v) {
  if (m.find(v) != m.end()) {
    return m[v];
  }

  int best = 0;
  for (int i = 0; i < p; i++) {
    if (v[i]) {
      vector<int> vv = v;
      vv[i]--;

      int tmp = 0;
      for (int j = 1; j < p; j++) {
        tmp += vv[j] * j;
      }

      best = max(best, (tmp % p == 0 ? 1 : 0) + f(vv));
    }
  }
  return m[v] = best;
}

int main() {
  int t, kase = 0;
  cin >> t;
  while (t--) {
    int n;
    cin >> n >> p;
    vector<int> v(p);
    m.clear();
    for (int i = 0; i < n; i++) {
      int tmp;
      cin >> tmp;
      v[tmp % p]++;
    }
    cout << "Case #" << ++kase << ": " << f(v) << endl;
  }
  return 0;
}
