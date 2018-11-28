#include <iostream>
#include <queue>

using namespace std;

bool tidy(long long n) {
  int digit = 9;
  while (n > 0) {
    if (digit < n % 10) return false;
    digit = n % 10;
    n /= 10;
  }
  return true;
}

long long tidify(long long n) {
  long long pos = 1;
  while (10 * pos <= n) {
    pos *= 10;
  }

  long long res = 0;
  int digit = 0;
  while (pos) {
    if (digit > (n / pos) % 10) {
      res--;
      res = res * pos * 10 + (pos * 10) - 1;
      return res;
    } else {
      digit = (n / pos) % 10;
      res *= 10;
      res += digit;
    }
    pos /= 10;
  }
  return res;
}

void solve() {
  long long number;
  cin >> number;
  while (!tidy(number)) {
    number = tidify(number);
  }
  cout << number << endl;
}

int main() {
  int T;
  cin >> T;
  for (int i = 0; i < T; i++) {
    cout << "Case #" << i + 1 << ": ";
    solve();
  }
  return 0;
}
