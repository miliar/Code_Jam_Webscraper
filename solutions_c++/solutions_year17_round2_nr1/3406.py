// 55724827 Gerardo
#include <iostream>
#include <string.h>
#include <iomanip>

using namespace std;
long long int T, D, N;
long long int K[1010], S[1010];
int main() {
  cin >> T;
  for (int t = 0; t < T; t++) {
    cin >> D >> N;
    for (int n = 0; n < N; n++) {
      cin >> K[n] >> S[n];
    }

    long long int kms = D - K[N-1];
    long long int speed = S[N-1];
    // double max_time = -1;
    for (int n = N-2; n >= 0; n--) {
      if (kms * S[n] <= (D - K[n]) * speed) {
        kms = D - K[n];
        speed = S[n];
      }
    }

    double y = ((double) (D * speed)) / ((double) kms);
    // if (y < 0) {
    //   cout << kms << "    " << speed;
    // }
    cout << "Case #" << t+1 << ": ";
    cout << fixed;
    cout << setprecision(6);
    cout << y;
    cout << endl;
  }
  return 0;
}
