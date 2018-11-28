#include <algorithm>
#include <cmath>
#include <iostream>
#include <string>

using namespace std;

int T = 0;

// K = 2^h - 1 + m
void solve(long long N, long long K, long long* L, long long* R) {
  //cout << "N=" << N << " K=" << K << endl;
  long long h_ld = log2l(K);
  const long long b = pow((long double)2.0, h_ld);
  const int m = int(K + 1 - b);
  const long long i = (N - b + 1) / b;
  const long long j = (N - b + 1) % b;
  //cout << "h_ld=" << h_ld << " b=" << b << " m=" << m << " i=" << i << " j=" << j << endl;
  long long step = i;
  if (m <= j) {
    step++;
  }

  if (step % 2 == 0) {
    *L = step / 2 - 1;
    *R = step / 2;
  } else {
    *L = *R = step / 2;
  }
}

int main() {

  long long N, K, L, R;
  cin >> T;
  for (int i = 1; i <= T; i++) {
    //cout << "Case #" << i << endl;
    cin >> N >> K;
    solve(N, K, &L, &R);
    cout << "Case #" << i << ": " << max(L, R) << " " << min(L, R) << endl;
  }

  return 0;
}
