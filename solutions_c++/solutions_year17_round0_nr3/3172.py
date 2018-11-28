#include <iostream>
#include <cstring>
#include <cstdio>

using namespace std;

long long getLen(long long N, long long K) {
  if (N % 2 == 1) {
    if (N > 1 && K > 1) {
      return getLen(N / 2, K / 2);
    } else {
      return N;
    }
  } else {
    long long x = 0;
    while ((1LL << (x + 1)) <= K) {
      ++x;
    }
    long long num = 1LL << x;
    long long M = (N - (num - 1)) / num;
    long long Y = N - num + 1 - num * M;
    long long X = num - Y;
    // cout << num << ' ' << M << ' ' << X << ' ' << Y << endl;
    if (K - num < Y) {
      return M + 1;
    } else {
      return M;
    }
  }
}

int main() {
  int T;
  cin >> T;
  for (int cases = 0; cases < T; ++cases) {
    long long N, K;
    cin >> N >> K;
    // cout << getLen(N, K) << endl;
    long long len = getLen(N, K);
    printf("Case #%d: ", cases + 1);
    if (len % 2 == 0) {
      printf("%lld %lld\n", len / 2, len / 2 - 1);
    } else {
      printf("%lld %lld\n", len / 2, len / 2);
    }
  }
}