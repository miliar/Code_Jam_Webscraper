// B.cpp
// Tidy Numbers

#include <iostream>
using namespace std;

long long ans = -1, n;

void solve(int curr_idx, int max_idx, long long curr_val, string curr_str,
           long long target_val, string target_str, bool flag) {
  if (ans != -1) {
    return;
  }
  // cout << curr_idx << " " << curr_val << endl;
  if (curr_idx == max_idx) {
    // cout << curr_idx << " " << curr_val << " " << n << endl;
    if (curr_val <= n) {
      if (ans == -1 || curr_val > ans) {
        ans = curr_val;
      }
    }
    return;
  }
  if (max_idx == (int)target_str.size() && curr_val > target_val) {
    return;
  }
  int curr_digit = target_str[curr_idx] - '0';
  int target_digit = 1;
  if (curr_str != "") {
    target_digit = curr_str.back() - '0';
  }
  for (int i = flag ? curr_digit : 9; i >= target_digit; i--) {
    // cout << i << endl;
    solve(curr_idx + 1, max_idx, curr_val * 10 + i, curr_str + (char)(i + '0'),
          target_val * 10 + curr_digit, target_str, i == curr_digit);
  }
}

int main() {
  int t, kase = 0;
  cin >> t;
  while (t--) {
    cin >> n;
    int num_digits = (int)(to_string(n)).size();
    ans = -1;
    for (int i = num_digits; i >= 1; i--) {
      solve(0, i, 0, "", 0, to_string(n), i == num_digits);
      if (ans != -1) {
        cout << "Case #" << ++kase << ": " << ans << endl;
        break;
      }
    }
  }
  return 0;
}