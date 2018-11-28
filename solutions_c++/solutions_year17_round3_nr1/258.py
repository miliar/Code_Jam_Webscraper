#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
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
#define PROBLEM_ID "ample_syrup"

#pragma comment(linker,"/STACK:32000000")

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

const double PI = 3.1415926535897932384626433832795;

int main() {
  freopen(PROBLEM_ID".in", "r", stdin);
  freopen(PROBLEM_ID".out", "w", stdout);
  int tests;
  cin >> tests;
  for (int ti = 0; ti < tests; ++ti) {
    int n, k;
    cin >> n >> k;
    vector<pii> pancakes(n);
    for (int i = 0; i < n; ++i) {
      cin >> pancakes[i].first >> pancakes[i].second;
    }
    sort(pancakes.begin(), pancakes.end());
    ll max_sum = 0;
    for (int last = k - 1; last < n; ++last) {
      vector<pii> other_pancakes(pancakes.begin(), pancakes.begin() + last);
      vector<ll> sort_by_rh;
      for (int i = 0; i < other_pancakes.size(); ++i) {
        sort_by_rh.push_back(ll(other_pancakes[i].first) * other_pancakes[i].second);
      }
      sort(sort_by_rh.rbegin(), sort_by_rh.rend());
      ll sum = ll(pancakes[last].first) * (pancakes[last].first + 2 * pancakes[last].second);
      for (int i = 0; i < k - 1; ++i) {
        sum += 2 * sort_by_rh[i];
      }
      if (sum > max_sum) {
        max_sum = sum;
      }
    }
    double result = max_sum * PI;
    cout << "Case #" << ti + 1 << ": ";
    cerr << "Case #" << ti + 1 << ": ";
    printf("%.10lf\n", result);
    fprintf(stderr, "%.10lf\n", result);
  }
  return 0;
}
