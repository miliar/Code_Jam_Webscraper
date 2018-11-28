#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

vector<int> digitize(long long N) {
  vector<int> digits;
  if (N == 0) digits.push_back(0);
  while (N > 0) {
    digits.push_back(N % 10);
    N /= 10;
  }
  reverse(digits.begin(), digits.end());
  return digits;
}

long long findLargetTidyNumber(long long N) {
  vector<int> digits = digitize(N);
  int M = digits.size();        // unchecked digits
 tidyUpDigits:
  for (int i = 1; i < M; ++i) {
    if (digits[i - 1] > digits[i]) {    
      --digits[i - 1]; // legal since digits[i] >= 0
      fill(digits.begin() + i, digits.begin() + M, 9);
      M = i;
      goto tidyUpDigits;
    }
  }
  long long tidyNumber = 0;
  for (int d : digits) {
    tidyNumber *= 10;
    tidyNumber += d;
  }
  return tidyNumber;
}

int main(int argc, char *argv[]) {
  ios::sync_with_stdio(false); cin.tie(NULL);
  int T; cin >> T;
  for (int t = 1; t <= T; ++t) {
    long long N; cin >> N;
    cout << "Case #" << t << ": "
         << findLargetTidyNumber(N)
         << '\n';
  }
  cout << flush;
  return 0;
}
