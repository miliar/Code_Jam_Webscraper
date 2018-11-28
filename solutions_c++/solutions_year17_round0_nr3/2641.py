#include <algorithm>
#include <map>
#include <chrono>
#include <iostream>
#include <vector>

using namespace std;
using namespace std::chrono;

int main() {
  auto start = high_resolution_clock::now();

  ios_base::sync_with_stdio(false);
  cin.tie(nullptr);

  int tests;
  cin >> tests;
  for (int test = 1; test <= tests; ++test) {
    long long n, k;
    cin >> n >> k;
    map<long long, long long> mp;
    mp[n] = 1;
    while (k) {
      long long len = mp.rbegin()->first;
      long long cnt = mp.rbegin()->second;
      mp.erase(mp.rbegin()->first);

      long long _min = (len - 1) / 2;
      long long _max = len / 2;

      if (cnt >= k) {
        cout << "Case #" << test << ": " << _max << " " << _min << endl;
        break;
      }

      k -= cnt;
      mp[_min] += cnt;
      mp[_max] += cnt;
    }
  }

  cerr << "Total execution time : " << duration_cast<milliseconds>(high_resolution_clock::now() - start).count() << " ms" << endl;

  return 0;
}
