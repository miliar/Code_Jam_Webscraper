#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

struct Color {
  int cnt;
  char clr;
};
Color a[6];

bool comparator(const Color& left, const Color& right) {
  return left.cnt < right.cnt;
}

int main() {
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  int t;
  cin >> t;
  string s;
  int N, R, O, Y, G, B, V;
  for (int _case = 1; _case <= t; _case++) {
    s = "IMPOSSIBLE";
    a[0].clr = 'R';
    a[1].clr = 'O';
    a[2].clr = 'Y';
    a[3].clr = 'G';
    a[4].clr = 'B';
    a[5].clr = 'V';
    //cin >> N >> R >> O >> Y >> G >> B >> V;
    cin >> N >> a[0].cnt >> a[1].cnt >> a[2].cnt >> a[3].cnt >> a[4].cnt >> a[5].cnt;
    sort(a, a+6, comparator);
    if (N % 2 == 0) {
      if (a[3].cnt + a[4].cnt >= a[5].cnt) {
        s = "";
        int _5 = N/a[5].cnt;
        if (_5 == 1) {
          _5++;
        }
        int q = 1;
        for (int i = 0; i < N; i++) {
          if (i % _5 == 0 && a[5].cnt > 0) {
            a[5].cnt--;
            s += a[5].clr;
          } else {
            if (a[3].cnt > a[4].cnt && s[i-1] != a[3].clr) {
              s += a[3].clr;
              a[3].cnt--;
              if (a[3].cnt < 0) {
                cout << "ERROR: EVEN TOP";
                exit(1);
              }
            } else {
              s += a[4].clr;
              a[4].cnt--;
              if (a[4].cnt < 0) {
                cout << "ERROR: EVEN";
                exit(1);
              }
            }
          }
        }
      }
    } else {
      if (a[3].cnt > 0 && a[4].cnt + a[3].cnt >= a[5].cnt) {
        s = "";
        int _5 = N/a[5].cnt;
        if (_5 == 1) {
          _5++;
        }
        int q = 1;
        for (int i = 0; i < N; i++) {
          if (i % _5 == 0 && a[5].cnt > 0) {
            a[5].cnt--;
            s += a[5].clr;
          } else {
            if (a[3].cnt > a[4].cnt && s[i-1] != a[3].clr) {
              s += a[3].clr;
              a[3].cnt--;
              if (a[3].cnt < 0) {
                cout << "ERROR: ODD TOP";
                exit(1);
              }
            } else {
              s += a[4].clr;
              a[4].cnt--;
              if (a[4].cnt < 0) {
                cout << "ERROR: ODD";
                exit(1);
              }
            }
          }
        }
      }
    }

    cout << "Case #" << _case << ": "<< s << "\n";
  }
  return 0;
}
