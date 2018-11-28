#include <bits/stdc++.h>
using namespace std;

#define rep(i,a,b) for (int i = a; i < b; i ++)
#define per(i,a,b) for (int i = b-1; i >= a; i --)

int main() {
  freopen("C.in", "r", stdin);
  freopen("C.out", "w", stdout);
  long long T, n, m, res;
  long long x, y, xn, yn;
  long long x1, y1, xn1, yn1;
  cin >> T;
  rep(t, 1, T + 1) {
//    cout << "====================" << endl;
    cin >> m >> n;
    x = m; xn = 1;
    y = m + 1; yn = 0;
    while (n > 0) {
//      cout << x << " " << xn << " " << y << " " << yn << endl;
//      cout << n << endl;
      if (x % 2 == 0) {
        x1 = x / 2 - 1;
        y1 = x / 2;
        xn1 = xn;
        yn1 = xn + yn + yn;
      } else {
        x1 = x / 2;
        y1 = x / 2 + 1;
        xn1 = xn + xn + yn; 
        yn1 = yn;
      }
      if (n <= yn) {
        res = y;
        break;
      }
      n -= yn;
      if (n <= xn) {
        res = x;
        break;
      }
      n -= xn;
      x = x1;
      y = y1;
      xn = xn1;
      yn = yn1;
    }
    cout << "Case #" << t << ": ";
    res --;
    x = (res / 2);
    y = (res / 2) + (res % 2);
    cout << y << " " << x << endl; 
  }
  return 0;
}
