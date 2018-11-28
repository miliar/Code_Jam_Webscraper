#include <iostream>
#include <iomanip>
#include <vector>
#include <algorithm>
#include <stack>
#include <queue>
#include <map>
#include <unordered_map>
#include <set>
#include <unordered_set>
#include <tuple>
#include <string>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <numeric>
#include <functional>
using namespace std;

typedef unsigned long long int llui;
typedef long long int ll;
typedef pair<int, int> pii;
typedef pair<double, double> pdd;
typedef pair<string, string> pss;

const int sz = 1e5;
double pi = 3.1415926535897;

static bool comp(pdd a, pdd b) {
  return a.first * a.second < b.first * b.second;
}

int main() {
  ios::sync_with_stdio(false);
  int T;
  cin >> T;

  for (int t = 1; t <= T; ++t) {
    cout << "Case #" << t << ": ";
    int n, k;
    cin >> n >> k;
    vector<pdd> pans(n);

    for (int i = 0; i < n; ++i) {
      cin >> pans[i].first >> pans[i].second;
    }

    sort(pans.begin(), pans.end(), comp);

    double M = 0;

    for (int i = 0; i < n; ++i) {
      vector<pdd> sel;
      sel.push_back(pans[i]);
      int s = 1;
      for (int j = pans.size() - 1; j >= 0 && s < k; --j) {
        if (pans[j].first > pans[i].first || j == i) {
          continue;
        }
        sel.push_back(pans[j]);
        ++s;
      }

      if (s != k) {
        continue;
      }

      double sum = 0;
      for (pdd c : sel) {
        sum += c.first * c.second;
      }
      sum *= 2;
      sum += pans[i].first * pans[i].first;
      sum *= pi;

      M = max(M, sum);
    }

    cout << fixed << setprecision(12) << M << endl;
  }
}

