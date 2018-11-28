#include <iostream>

using namespace std;

typedef unsigned long long ull;

int main() {
  int T;
  cin >> T;

  for (int t = 1; t <= T; t++) {
    ull K, N;
    cin >> N >> K;  

    ull remain = K;
    ull step = 1;
    while (remain > step) {
      remain -= step;
      step *= 2;
    }

    ull range = (N - (K - remain))/(K - remain + 1);
    ull range_remain = (N - (K - remain))%(K - remain + 1);

    if (remain <= range_remain) range ++;

    cout << "Case #" << t << ": " << range/2 << " "
    << range/2 - 1 + range%2 << endl;
  }
  return 0;
}
