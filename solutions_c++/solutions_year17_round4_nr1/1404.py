#include <bits/stdc++.h>

#define DEBUG(x) cerr << #x << " = " << x << endl

using namespace std;

typedef long double ld;
typedef long long ll;

template <class Ta, class Tb> inline Tb cast(Ta a) {
  stringstream ss;
  ss << a;
  Tb b;
  ss >> b;
  return b;
};

int fresh(vector<int> g, int p) {
  int ret = 0;
  int extra = 0;
  for (int i = 0; i < int(g.size()); ++i) {
    if (extra == 0) {
      ++ret;
    }
    if (extra >= g[i]) {
      extra -= g[i];
    } else {
      int cg = g[i] - extra;
      extra = (p - (cg % p)) % p;
    }
  }
  return ret;
}

int main() {
  int T;
  cin >> T;
  for (int ca = 1; ca <= T; ++ca) {
    cout << "Case #" << ca << ": ";
    int n, p;
    cin >> n >> p;
    vector<int> gc(p, 0);
    for (int i = 0; i < n; ++i) {
      int g;
      cin >> g;
      ++gc[g % p];
    }

    vector<int> seq0;
    for (int i = 0; i < gc[0]; ++i) {
      seq0.push_back(0);
    }
    gc[0] = 0;
    for (int i = 1; i <= p / 2; ++i) {
      int pairs;
      if (i == p - i) {
        pairs = gc[i] / 2;
      } else {
        pairs = min(gc[i], gc[p - i]);
      }
      for (int j = 0; j < pairs; ++j) {
        seq0.push_back(i);
        seq0.push_back(p - i);
      }
      gc[i] -= pairs;
      gc[p - i] -= pairs;
    }
    vector<int> seq1;
    for (int i = 0; i < p; ++i) {
      for (int j = 0; j < gc[i]; ++j) {
        seq1.push_back(i);
      }
    }
    int ans = 0;
    do {
      vector<int> seq = seq0;
      seq.insert(seq.end(), seq1.begin(), seq1.end());
      int cur = fresh(seq, p);
      if (cur > ans) {
        ans = cur;
      }
    } while (next_permutation(seq1.begin(), seq1.end()));
    cout << ans << endl;
  }
}
