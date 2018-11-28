
#include <iostream>

using namespace std;

static long long CalculateLastTidyNum(long long N) {
  int digits[32];
  int dc = 0;
  long long m = N;
  while (m > 0) {
    digits[dc++] = m % 10;
    m /= 10;
  }
  bool all_inc = true;
  for (int i = 0; i < dc - 1; ++i) {
    if (digits[i] < digits[i + 1]) {
      all_inc = false;
      break;
    }
  }
  if (all_inc) {
    return N;
  }
  for (int i = dc - 2; i >= 0; --i) {
    if (digits[i] <= digits[i + 1]) {
      digits[i + 1] -= 1;
      for (int k = i; k >= 0; --k) {
        digits[k] = 9;
      }
      break;
    }
  }
  long long res = 0;
  for (int i = dc - 1; i >= 0; --i) {
    res = res * 10 + digits[i];
  }
  return res;
}

int main() {
  int T = 0;
  long long N = 0;
  cin >> T;
  for (int i = 0; i < T; ++i) {
    cin >> N;
    cout << "Case #" << (i + 1) << ": " <<
      CalculateLastTidyNum(N) << endl;
  }
  return 0;
}