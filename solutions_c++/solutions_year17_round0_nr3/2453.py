#ifdef DEBUG
//#define _GLIBCXX_DEBUG
#endif
#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <string>
#include <cstring>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <ctime>
#include <cassert>
#include <functional>
#include <complex>

using namespace std;
typedef long double LD;
typedef long long LL;

std::vector<int> primes;

void Solve() {
  long long n, k;
  cin >> n >> k;
  std::multiset<long long> s;
  s.insert(n);
  long long rv = 0, lv = 0;
  for (int i = 0; i < k; ++i) {
    auto it = s.end();
    --it;
    long long v = *it;
    s.erase(it);
    --v;
    rv = (v + 1) / 2;
    lv = v / 2;
    s.insert(rv);
    s.insert(lv);
  }
  cout << rv << " " << lv << endl;
}

void Solve2() {
  std::map<long long, long long> m;
  long long n, k;
  cin >> n >> k;
  m[n] = 1;
  long long rv = 0, lv = 0;
  while (k > 0) {
    auto it = m.end();
    --it;
    auto v = *it;
    m.erase(it);
    long long val = v.first, cnt = v.second;
    --val;
    rv = (val + 1) / 2;
    lv = val / 2;
    k -= cnt;
    m[rv] += cnt;
    m[lv] += cnt;
  }
  cout << rv << " " << lv << endl;
}

void init() {
}

int main() {
    freopen("c.in", "r", stdin);
    freopen("c.out", "w", stdout);
    init();
    int T;
    cin >> T;
    for (int i = 0; i < T; ++i) {
        printf("Case #%d: ", i + 1);
        Solve2();
    }
    return 0;
}
