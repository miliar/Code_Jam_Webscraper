#include <bits/stdc++.h>

using namespace std;

int main() {
  int t;
  cin >> t;
  for (int i = 0; i < t; i++) {
    long long n;
    cin >> n;
    long long tidy = n, j = 1, tmp = n, pre = tmp % 10;

    while (tmp != 0) {
      if (tmp % 10 <= pre) {
	pre = tmp % 10;
      }
      else {
	tidy = tmp * j - 1;
	pre = tmp % 10 - 1;
      }
      j *= 10;
      tmp /= 10;
    }

    cout << "Case #" << i+1 << ": " << tidy << endl;
  }

  return 0;
}
