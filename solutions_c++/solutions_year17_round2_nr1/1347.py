#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

struct horse {
  long double k;
  long double s;
};

bool comparator(const horse& left, const horse& right) {
  return left.s > right.s;
}

horse horses[1000];
int n;
long double l,r,mid,d;

bool check(long double speed) {
  long double annie_time = d/speed;

  for (int i = 0; i < n; i++) {
    if (horses[i].k + horses[i].s*annie_time - d < 1e-7) {
      return false;
    }
  }
  return true;
}

int main() {
    // cin.tie(0);
    // ios_base::sync_with_stdio(false);
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  int t;
  cin >> t;
  for (int _case = 1; _case <= t; _case++) {
    cin >> d >> n;
    for (int i = 0; i < n; i++) {
      cin >> horses[i].k >> horses[i].s;
    }
    // sort(horses, horses + n, comparator);
    // for (int i = 0; i < n; i++) {
    //   for (int j = i+1; j < n; j++) {

    //   }
    // }
    l = 0.5;
    r = 1e14;
    int k = 0;
    while ((r - l) > 1e-6) {
      mid = (r+l) / 2.0;
      if (check(mid)) {
        l = mid;
      } else {
        r = mid;
      }
    }
    cout << "Case #" << _case << ": ";
    printf("%Lf\n", mid);
  }
  return 0;
}
