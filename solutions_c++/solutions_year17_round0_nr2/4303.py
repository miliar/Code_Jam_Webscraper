#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int get_digit(ll n, int idx) {
  ll d = pow(10, idx);
  ll nn = n / d;
//  cout << "digit: " << nn << endl;
  int r = nn % 10;
  return r;
}

vector<int> num_to_digits(ll n) {
  vector<int> digits;
  for (int i = 0; i < 20; i++) {
    int r = get_digit(n, i);
    digits.push_back(r);
  }
  reverse(digits.begin(), digits.end());
  return digits;
}

ll digits_to_num(vector<int> &digits) {
  long long r = 0;
  for (int i = 0; i < digits.size(); i++) {
    int idx = digits.size()-i-1;
    long long m = digits[i] * pow(10, idx);
    r += m;
//    cout << digits[i] << " " << r << " " << m << endl;
  }
  return r;
}

void solve(ll n, int t) {
  int r = 0;
  bool clear_mode;
  vector<int> digits = num_to_digits(n);
  do {
    clear_mode = false;
    for (int i = 0; i < digits.size()-1; i++) {
      if (clear_mode) {
        digits[i] = 0;
      } else if (digits[i] > digits[i+1]) {
        clear_mode = true;
      }
    }
    if (clear_mode) {
//      cout << "CLEAR MODE" << endl;
      ll num = digits_to_num(digits);
      digits = num_to_digits(num-1);
    } else {
      ll num = digits_to_num(digits);
      cout << "Case #" << t << ": " << num << endl;
    }
  } while (clear_mode);
}


int main() {
  int T; cin >> T;
  for (int t = 1; t <= T; t++) {
    ll N; cin >> N;
    solve(N, t);
  }
  return 0;
}
