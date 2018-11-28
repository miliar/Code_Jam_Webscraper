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
#define PROBLEM_ID "core_training"

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

double ComputeProbOK(const vector<double>& p, int k) {
  vector< vector<double> > dp(p.size() + 1, vector<double>(p.size() + 1, 0));
  dp[0][0] = 1;
  for (int i = 0; i < p.size(); ++i) {
    for (int j = 0; j <= i; ++j) {
      dp[i + 1][j + 1] += p[i] * dp[i][j];
      dp[i + 1][j] += (1 - p[i]) * dp[i][j];
    }
  }
  double res = 0;
  for (int j = k; j <= p.size(); ++j) {
    res += dp[p.size()][j];
  }
  return res;
}

double MaxProb(vector<double> p, int k, double U) {
  while (U > 1e-10) {
    sort(p.begin(), p.end());
    vector<pair<double, int> > derivs;
    for (int i = 0; i < p.size(); ++i) {
      if (i + 1 == p.size() || p[i + 1] > p[i] + 1e-10) {
        vector<double> q;
        for (int j = 0; j < p.size(); ++j) {
          if (j != i) {
            q.push_back(p[j]);
          }
        }
        double deriv = ComputeProbOK(q, k - 1);
        derivs.push_back(MP(deriv, i));
      }
    }
    sort(derivs.rbegin(), derivs.rend());
    int index = derivs[0].second;
    int index_copy = index;
    while (index > 0 && p[index - 1] > p[index] - 1e-10) {
      --index;
    }
    int cnt = index_copy - index + 1;
    double next_value = 1;
    if (index_copy + 1 < p.size()) {
      next_value = p[index_copy + 1];
    }
    if (cnt * (next_value - p[index_copy]) <= U) {
      U -= cnt * (next_value - p[index_copy]);
      for (int i = index; i <= index_copy; ++i) {
        p[i] = next_value;
      }      
    }
    else {
      double delta = U / cnt;
      for (int i = index; i <= index_copy; ++i) {
        p[i] += delta;
      }
      U = 0;
      break;
    }
  }
  return ComputeProbOK(p, k);
}

int main() {
  freopen(PROBLEM_ID".in", "r", stdin);
  freopen(PROBLEM_ID".out", "w", stdout);
  int tests;
  cin >> tests;
  for (int ti = 0; ti < tests; ++ti) {
    int n, k;
    cin >> n >> k;
    double U;
    cin >> U;
    vector<double> p(n);
    for (int i = 0; i < n; ++i) {
      cin >> p[i];
    }
    double result = MaxProb(p, k, U);
    cout << "Case #" << ti + 1 << ": ";
    cerr << "Case #" << ti + 1 << ": ";
    printf("%.10lf\n", result);
    fprintf(stderr, "%.10lf\n", result);
  }
  return 0;
}
