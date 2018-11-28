#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <functional>
#include <iostream>
#include <limits>
#include <numeric>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

#define MP make_pair
#define all(v) (v).begin(), (v).end()
#define PROBLEM_ID "bathroom_stalls"

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<vvi> vvvi;
typedef vector<bool> vb;
typedef vector<vb> vvb;
typedef vector<vvb> vvvb;
typedef long double ld;
typedef pair<int, int> pii;
typedef long long ll;
typedef vector<ll> vl;
typedef vector<vl> vvl;
typedef vector<vvl> vvvl;
typedef pair<ll, ll> pll;
typedef vector<double> vd;
typedef vector<vd> vvd;
typedef vector<vvd> vvvd;

typedef map<ll, ll, greater<ll> > LenMap;

LenMap ComputeLenCounts(ll n, map<ll, LenMap>& len_counts) {
  if (len_counts.count(n)) {
    return len_counts[n];
  }
  LenMap& res = len_counts[n];
  if (n == 0) {
    return res;
  }
  if (n == 1) {
    res[1] = 1;
    return res;
  }
  res = ComputeLenCounts((n - 1) / 2, len_counts);
  LenMap second_half = ComputeLenCounts(n / 2, len_counts);
  for (auto entry : second_half) {
    res[entry.first] += entry.second;
  }
  res[n] += 1;
  return res;
}

int main() {
  freopen(PROBLEM_ID".in", "r", stdin);
  freopen(PROBLEM_ID".out", "w", stdout);
  int tests;
  cin >> tests;
  for (int test_index = 0; test_index < tests; ++test_index) {
    ll n, k;
    cin >> n >> k;
    map<ll, LenMap> len_counts;
    ComputeLenCounts(n, len_counts);
    ll sum = 0;
    ll y, z;
    for (auto entry : len_counts[n]) {
      if (sum + entry.second >= k) {
        y = entry.first / 2;
        z = (entry.first - 1) / 2;
        break;
      }
      sum += entry.second;
    }
    cout << "Case #" << (test_index + 1) << ": " << y << ' ' << z << endl;
    cerr << "Case #" << (test_index + 1) << ": " << y << ' ' << z << endl;
  }
  return 0;
}
