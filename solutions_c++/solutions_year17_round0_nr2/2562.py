#include <algorithm>
#include <chrono>
#include <iostream>
#include <vector>

using namespace std;
using namespace std::chrono;

const int LIM = 20;

long long solve(long long x) {
  vector<int> num(LIM, 0);
  for (int i = 0; i < LIM; ++i) {
    num[i] = x % 10;
    x /= 10;
  }

  for (int i = LIM - 2; i >= 0; --i) {
    if (num[i] < num[i + 1]) {
      while (num[i] < num[i + 1]) {
        ++i;
        --num[i];
      }
      for (int j = 0; j < i; ++j)
        num[j] = 9;
      break;
    }
  }

  x = 0;
  for (int i = LIM - 1; i >= 0; --i)
    x = x * 10 + num[i];

  return x;
}

int main() {
  auto start = high_resolution_clock::now();

  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int tests;
  cin >> tests;
  for (int test = 1; test <= tests; ++test) {
    long long n;
    cin >> n;

    cout << "Case #" << test << ": " << solve(n) << endl;
  }

  cerr << "Total execution time : " << duration_cast<milliseconds>(high_resolution_clock::now() - start).count() << " ms" << endl;

  return 0;
}
