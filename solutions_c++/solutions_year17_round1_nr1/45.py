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

int main() {
  int T;
  cin >> T;
  for (int ca = 1; ca <= T; ++ca) {
    cout << "Case #" << ca << ":" << endl;
    int r, c;
    cin >> r >> c;
    vector<string> cake(r);
    for (int i = 0; i < r; ++i) {
      cin >> cake[i];
    }
    for (int i = 0; i < r; ++i) {
      char last = '?';
      for (int j = 0; j < c; ++j) {
        if (cake[i][j] != '?') {
          last = cake[i][j];
        }
        cake[i][j] = last;
      }
      last = '?';
      for (int j = c - 1; j >= 0; --j) {
        if (cake[i][j] != '?') {
          last = cake[i][j];
        }
        cake[i][j] = last;
      }
    }
    string last = string(c, '?');
    for (int i = 0; i < r; ++i) {
      if (cake[i] != string(c, '?')) {
        last = cake[i];
      }
      cake[i] = last;
    }
    last = string(c, '?');
    for (int i = r - 1; i >= 0; --i) {
      if (cake[i] != string(c, '?')) {
        last = cake[i];
      }
      cake[i] = last;
    }

    for (int i = 0; i < r; ++i) {
      cout << cake[i] << endl;
    }
  }
}
