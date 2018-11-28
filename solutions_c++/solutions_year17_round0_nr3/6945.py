#include <iostream>
#include <math.h>

using namespace std;

int main() {

  int t;
  cin >> t;

  unsigned long long  n, k, y, z;
  for (unsigned long long   i = 0; i < t; i++) {
    cin >> n >> k;
    for (unsigned long long j = 0; pow(2, j) <= k; j++) {
      y = ceil((n - 1) / 2.0);
      z = floor((n - 1) / 2.0);

      unsigned long long tmp = floor(1.0*k / pow(2, j));
      n = tmp % 2 == 0 ? y : z;
    }

    cout << "Case #" << i + 1 << ": " << y << " " << z << endl;
  }

  return 0;
}