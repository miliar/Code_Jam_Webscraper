#include <bits/stdc++.h>

using namespace std;

using ll = long long;
void solve() {
  ll n;
  cin >> n;
  n++;
  vector <int> digits;
  while (n > 0) {
    digits.push_back(n % 10);
    n /= 10;
  }
  set <ll> answers;
  for (int i = 0; i < digits.size(); ++i) {
    for (int d = 0; d < digits[i]; ++d) {
      auto digits_ = digits;
      digits[i] = d;
      for (int j = i - 1; j >= 0; --j) {
        digits[j] = 9;
      }
      bool f = 1;
      for (int j = 1; j < digits.size(); ++j) {
        if (digits[j] > digits[j - 1]) {
          f = 0;
        }
      }
      if (!f) {
        digits = digits_;
        continue;
      }
      ll number = 0;
      for (int j = digits.size() - 1; j >= 0; --j) {
        number = 10 * number + digits[j];
      }
      answers.insert(number);
      digits = digits_;
    }
  }
  cout << *answers.rbegin() << endl;
}

int main() {
  freopen("input.txt", "r", stdin);
  int t;
  cin >> t;
  for (int i = 1; i <= t; ++i) {
    cout << "Case #" << i << ": ";
    solve();
  }
}