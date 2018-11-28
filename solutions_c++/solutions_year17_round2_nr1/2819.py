#include <bits/stdc++.h>
using namespace std;

typedef long double LD;

const int N = 1e5 + 1;

int d, n;

int pos[N];
int speed[N];

LD GetIntersectionPoint(int k, LD s1, LD s2) {
  return s2 * k / (s2 - s1);
}

bool Check(LD s) {
  for (int i = 0; i < n; ++i) {
    if (s > speed[i] && GetIntersectionPoint(pos[i], speed[i], s) <= d) {
      return false;
    }
  }
  return true;
}

LD Solve() {
  LD low = 0, high = 1e14, mid;
  for (int i = 0; i < 200; ++i) {
    mid = (low + high) / 2;
    if (Check(mid)) {
      low = mid;
    } else {
      high = mid;
    }
  }
  return mid;
}

int main() {
  ios_base::sync_with_stdio(0), cin.tie(0), cout.tie(0);
#ifdef Local
  freopen("test.in", "r", stdin);
  freopen("out.txt", "w", stdout);
#endif

  int t;
  cin >> t;

  for (int cs = 1; cs <= t; ++cs) {
    cin >> d >> n;
    for (int i = 0; i < n; ++i) {
      cin >> pos[i] >> speed[i];
    }
    cout << "Case #" << cs << ": ";
    cout << fixed << setprecision(7) << Solve() << '\n';
  }

  return 0;
}
