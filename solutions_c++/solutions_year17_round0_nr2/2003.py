#include <cstdint>
#include <iostream>
#include <vector>

using namespace std;

bool nice(int n) {
  int prev = 9;
  while (n > 0) {
    int d = n % 10;
    n = n / 10;
    if (d > prev) {
      return false;
    }
    prev = d;
  }
  return true;
}
void solve(int case_, int64_t n) {
  // auto n_keep =n;
  // int r = -1;
  // for(int i = 0; i <= n; ++i) {
  //   if (nice(i)) {
  //     r = i;
  //   }
  // }
  int64_t result = 0;
  int borrow = 0;
  int64_t mult = 1;
  while(n > 0) {
    int d = n % 10;
    n /= 10;
    int next_d = n % 10;
    if (d == 0) {
      result = mult - 1;
      d = 9;
      borrow = 1;
    } else {
      d -= borrow;
      borrow = 0;
      if (d < next_d) {
        result = mult - 1;
        borrow = 1;
        d = 9;
      }
    }
    result += mult * d;
    mult *= 10;
  }
  std::cout << "Case #" << case_ << ": " << result << endl;
  // if (r != result) {
  //   cout << "bad result : " << r << " " << result << " n " << n_keep << endl;

  // }
}

int main() {
  int t_num;
  cin >> t_num;
  for (auto t = 1; t <= t_num; ++t) {
    int64_t n;
    cin >> n;
    solve(t, n);
  }
}
