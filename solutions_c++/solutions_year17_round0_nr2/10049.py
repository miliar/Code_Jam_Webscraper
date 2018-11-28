#include <iostream>

bool isTidy(unsigned long long N) {
  unsigned long long curDigit = 9;
  while (N > 0) {
    if (N % 10 > curDigit)
      return false;
    curDigit = N % 10;
    N /= 10;
  }

  return true;
}

int main() {
  using namespace std;
  int T;

  cin >> T;
  for (int caseId = 1; caseId <= T; ++caseId) {
    unsigned long long N;
    cin >> N;
    cout << "Case #" << caseId << ": ";
    while (!isTidy(N))
      --N;
    cout << N << endl;
  }
}
