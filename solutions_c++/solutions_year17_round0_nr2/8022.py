#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

vector <long long> v;
int n;

void pre() {
  n = 1000;
  v.clear();
  for (int i = 1; i <= n; i++) {
    string o = to_string(i);
    string s = o;
    sort(s.begin(), s.end());
    if (s == o) {
      v.push_back(i);
      // cout << s << endl;
    }
  }
}

int main() {
  int t;
  pre();
  cin >> t;
  for (int _ = 1; _ <= t; _++) {
    long long ans = 0;
    long long a = 0;
    cin >> a;
    auto it = upper_bound(v.begin(), v.end(), a);
    it--;
    ans = *it;
    cout << "Case #" << _ << ": " << ans << endl;
  }
}
