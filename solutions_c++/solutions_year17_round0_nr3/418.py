#include <iostream>
#include <cstdlib>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cassert>

using namespace std;

long long K;
long long N;

void init() {
  cin >> N >> K;
}

void solve_case(int t) {
  init();

  long long m = 1LL; // number of regions
  while (2 * m <= K)
    m *= 2;
  long long k = K - (m - 1);
  long long n = N - (m - 1);
  long long block_size = n / m;

  if (k <= (n % m)) {
    block_size++;
  }
  cout << "Case #" << t << ": "
       << (block_size / 2) << " "
       << ((block_size - 1) / 2) << "\n";
}

int main() {
  int T;
  cin >> T;

  for (int i = 0; i < T; i++) {
    solve_case(i + 1);
  }

  return 0;
}
