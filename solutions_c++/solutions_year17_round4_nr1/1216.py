#include <bits/stdc++.h>

using namespace std;

int main() {
  int T;
  cin >> T;

  for (int tst = 0; tst < T; tst++) {
    int n, p;
    cin >> n >> p;
    vector <int> A(p);

    for (int i = 0; i < n; i++) {
      int x;
      cin >> x;
      A[x % p]++;
    }
    cout << "Case #" << tst + 1 << ": ";
    
    if (p == 2) {
      cout << A[0] + (A[1] + 1) / 2;
    } else if (p == 3) {
      cout << A[0] + min(A[1], A[2]) + (abs(A[2] - A[1]) + 2) / 3;
    } else if (p == 4) {
      int res = A[0] + A[2] / 2 + min(A[3], A[1]) + (abs(A[3] - A[1]) + 3) / 4;

      if (A[2] % 2 == 1 && (A[1] + (A[2] - 1) * 2 + A[3] * 3) % 4 == 0) {
        res++;
      }
      cout << res;
    }
    cout << '\n';
  }
}
