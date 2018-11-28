#include <bits/stdc++.h>
using namespace std;

long long last_length(long long n, long long k) {
  if (k == 1) {
    return n;
  }
  if (n % 2 == 1) {
    return last_length((n-1)/2, k/2);
  } else {
    return last_length((n/2)-(k%2), k/2);
  }
}
int main() {
  int t;
  cin >> t;
  for (int tc = 1; tc <= t; tc++) {
    long long n, k;
    cin >> n >> k;
    long long r = last_length(n, k);
    // occupy this stall
    long long q = r - 1;
    cout << "Case #" << tc << ": " << ((q/2)+(q%2)) << " " << (q/2) << endl;
  }
}
