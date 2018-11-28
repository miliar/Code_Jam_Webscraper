#include <iostream>

using namespace std;

main() {
  int T;
  cin >> T;
  for (int c=1; c<=T; c++) {
    unsigned long long N, answer, p = 100000000000000000;
    cin >> N;
    while (p>0 && (N/p/10)%10 <= (N/p)%10) p /= 10;
    if (p == 0) answer = N;
    else {
      long long q = p * 10;
      while ((N/q/10)%10 == (N/q)%10) q *= 10;
      answer = N - (N % (q*10)) + (((N / q) % 10)-1) * q + q - 1;
    }
    cout << "Case #" << c << ": " << answer << endl; 
  };
};
