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
typedef pair<string, string> pss;

const int sz = 1e5;

bool Deq(double a, double b) {
  return fabs(a - b) < numeric_limits<double>::epsilon();
}

int main() {
  ios::sync_with_stdio(false);
  int T;
  cin >> T;

  for (int t = 1; t <= T; ++t) {
    cout << "Case #" << t << ": ";
    int n, k;
    cin >> n >> k;
    double u;
    cin >> u;

    priority_queue<double, std::vector<double>, std::greater<double>> cores;

    for (int i = 0; i < n; ++i) {
      double x;
      cin >> x;
      cores.push(x); 
    }

    if (cores.size() == 1) {
      double cur = cores.top();
      cores.pop();
      cur += u;
      cur = min(cur, (double)1);
      cout << cur << endl;
      continue;
    }

    while (u > 1e-6) {
      vector<double> tmp;
      tmp.push_back(cores.top());
      cores.pop();

      while (!cores.empty()) {
        tmp.push_back(cores.top());
        cores.pop();
        if (!Deq(tmp[tmp.size() - 2], tmp[tmp.size() - 1])) {
          break;
        }
      }

      double diff = tmp.back() - tmp[0];
      if (Deq(diff, 0)) {
        for (double a : tmp) {
          a += u / tmp.size();
          a = min(a, (double)1);
          cores.push(a);
        }
        u = 0;
      } else {
        if (u < diff * (tmp.size() - 1)) {
          for (int i = 0; i < tmp.size() - 1; ++i) {
            tmp[i] += u / (tmp.size() - 1);
            tmp[i] = min(tmp[i], (double)1);
            cores.push(tmp[i]);
          }
          cores.push(tmp.back());
          u = 0;
        } else {
          for (int i = 0; i < tmp.size() - 1; ++i) {
            tmp[i] += diff; 
            tmp[i] = min(tmp[i], (double)1);
            cores.push(tmp[i]);
          }
          u -= diff * (tmp.size() - 1);
          cores.push(tmp.back());
        }
      }
    }

    double ans = 1;

    while (!cores.empty()) {
      ans *= cores.top();
      cores.pop();
    }
    cout << fixed << setprecision(12) << ans << endl;
  }
}

