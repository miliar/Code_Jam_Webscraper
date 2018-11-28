#include <iostream>

using namespace std;

int main() {
  int T;
  cin >> T;

  for (int tst = 0; tst < T; tst++) {
    long long n, k;
    cin >> n >> k;

    long long power = 1;
    long long one = n, numone = 1, two = n + 1, numtwo = 0;

    while (power * 2 <= k) {
      long long newone, newtwo, newnumone, newnumtwo;

      if (one % 2 == 0) {
        newone = one / 2 - 1;
        newtwo = one / 2;
        newnumone = numone;
        newnumtwo = numone + numtwo * 2;
      } else {
        newone = one / 2;
        newtwo = one / 2 + 1;
        newnumone = numone * 2 + numtwo;
        newnumtwo = numtwo;
      }
      power *= 2;
      one = newone;
      two = newtwo;
      numone = newnumone;
      numtwo = newnumtwo;
    }
    k -= power - 1;
    long long res = (k <= numtwo ? two : one);
    cout << "Case #" << tst + 1 << ": " << res / 2 << ' ' << (res - 1) / 2 << '\n';
  }
}
