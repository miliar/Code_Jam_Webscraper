#include <iostream>

using namespace std;

long find_untidy(long n) {
  long untidy = -1;
  long factor = 10;
  int prev = n%10, cur;
  n /= 10;
  while (n > 0) {
    cur = n%10;
    if (cur > prev) {
      untidy = factor;
    }
    if (n == 0) break;

    factor *= 10;
    prev = cur;
    n /= 10;
  }
  return untidy;
}

long solve(long N) {
  // find the larget non-tidy digit
  long factor;
  factor = find_untidy(N);
  //cout << "first factor " << factor << "\n";
  while (factor != -1) {
    N = N - (N%factor) - 1;
    //cout << "factor " << factor << "\n";
    //cout << "N " << N << "\n";
    factor = find_untidy(N);
  }
  return N;
}


int main() {
  int T;
  long N;

  cin >> T;
  for (int i=0; i<T; i++) {
    cin >> N;
    cout << "Case #" << i+1 << ": " << solve(N) << "\n";
  }
  return 0;
}
