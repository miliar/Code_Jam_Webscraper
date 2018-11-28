#include <iostream>
#include <string>

using namespace std;

typedef unsigned long long ull;

int main() {
  int T;
  cin >> T;
  for (int t = 1; t <= T; t++) {
    ull N;
    cin >> N;

    ull ans = N;
    ull idx = 1;
    ull m = 0;
    while (N > 0) {
      ull cur = N%10;
      ull next = N/10%10;
      N /= 10;

      idx *= 10;
      if (next > cur) {
        m = idx;
        N -= 1;
      }
    }

    if (m > 0) ans = ans/m*m-1;

    cout << "Case #" << t << ": " << ans << endl;
  }
  return 0;
}
