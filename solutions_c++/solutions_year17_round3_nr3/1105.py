#include <algorithm>
#include <iostream>
#include <vector>
#include <string>
#include <cstdio>
#include <map>
#include <set>
#include <queue>
#include <stack>
using namespace std;
static const int MAX = 50;

int n, k;
double unit;
vector<double> data;

double solve() {
  sort(data.begin(), data.end());
  int i = 0;
  int hoge = 1;
  data.push_back(1.0);

  while (unit > 0) {
    if (i == data.size()-1) {
      break;
    }
    auto dif = data[i+1] - data[i];
    auto app = min(dif*hoge, unit);
    for (int j =0; j < hoge; j++) {
      data[j] += app / hoge;
    }
    i++;
    hoge++;
    unit -= app;
  }
  data.pop_back();

  double ans = 1.0;
  for(auto v: data) {
    ans *= v;
  }
  return ans;
}

int main() {
  int t;
  cin >> t;
  for (int i = 0; i < t; i++) {
    data.clear();
    cin >> n >> k >> unit;

    for (int i = 0; i < n; i++) {
      double ai;
      cin >> ai;
      data.push_back(ai);
    }
    auto ans = solve();
    printf("Case #%d: %f\n", i+1, ans);
  }

}

