#include <iostream>
#include <cstdio>
#include <string>
#include <vector>

using namespace std;

int main() {
  int t;
  cin >> t;
  for (int _ = 1; _ <= t; _++) {
    string a;
    int k;
    cin >> a >> k;
    vector<bool> b;
    b.resize(a.size());
    for (int i = 0; i < a.size(); i++) {
      if (a[i] == '+') b[i] = true;
      else b[i] = false;
    }
    int ans = 0;
    for (int i = 0; i < b.size(); ++i) {
      if (b[i] == false) {
        if (i + k > b.size()) {
          break;
        }
        ans++;
        for (int j = i; j < i + k; j++) {
          b[j] = !b[j];
        }
      }
    }
    bool suc = true;
    /*for (int i = 0; i < b.size(); i++) {
      cout << b[i];
    } cout << endl;*/
    for (int i = 0; i < b.size(); i++) {
      if (b[i] == false) {
        suc = false;
        break;
      }
    }
    if (!suc) {
      cout << "Case #" << _ << ": IMPOSSIBLE" << endl;
    } else {
      cout << "Case #" << _ << ": " << ans << endl;
    }
  }
}
