#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
#include <cmath>

using namespace std;
typedef long long ll;
const double PI = 3.14159265358979323846;
double res = 0.0;
int n, k;
const int maxn = 1005;
vector<pair<int, int>> a(maxn);

double sq(int r, int h) {
  return PI * r * r + 2.0 * PI * r * h;
}

double per(int r) {
  return PI * r * r;
}

void find(double tmp, int pos, int c) {
  if (c == k) {
    res = max(res, tmp);
    return;
  }
  for (int i = pos; i < n; ++i) {
    double t = tmp - per(a[i].first) + sq(a[i].first, a[i].second);
    find(t, i + 1, c + 1);
  }
}

int main() {
  int tt; cin >> tt;
  for (int t = 1; t <= tt; ++t) {
    cin >> n >> k;
    for (int i = 0; i < n; ++i) {
      int r, h; cin >> r >> h;
      a[i] = make_pair(r, h);
    }
    sort(a.begin(), a.begin() + n);
    reverse(a.begin(), a.begin() + n);

    res = 0.0;
    double tmp = 0.0;

    for (int i = 0; i < n; ++i) {
      tmp = sq(a[i].first, a[i].second);
      find(tmp, i + 1, 1);
    }


    printf("Case #%d: %.9f\n", t, res);
  }

  return 0;
}
