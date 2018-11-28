#include <iostream>
#include <algorithm>
#include <cmath>
using namespace std;
double pi = 3.14159265358979323846;
struct pancacke {
  int id;
  double basearea;
  double lateral;
  friend bool operator<(pancacke a, pancacke b) {
    if(a.lateral > b.lateral) return true;
    else if(a.lateral == b.lateral) return a.basearea < b.basearea;
    return false;
  }
};
int main() {
  int t, k, n, r, h;
  cin >> t;
  for(int tc = 1; tc <= t; tc++) {
    cin >> n >> k;
    pancacke p[n];
    pancacke p1[n];
    for(int i = 0; i < n; i++) {
      cin >> r >> h;
      p[i] = {i, pi*r*r, 2*pi*r*h};
      p1[i] = p[i];
    }
    sort(p, p+n);
    sort(p1, p1+n);
    double ans = 0;
    double defans = 0;
    double base = 0;
    for(int j = 0; j < n; j++) {
      ans = p[j].lateral;
      base =  p[j].basearea;
      for(int i = 0, q = 1; q != k and i < n; i++) {
        if(p[i].id != p[j].id) {
          ans += p[i].lateral;
          base = max(base, p[i].basearea);
          q++;
        }
      }
      ans += base;
      defans = max(ans, defans);
    }
    printf("Case #%d: %.20lf\n", tc, defans);
  }
}
