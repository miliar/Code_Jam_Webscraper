#include<iostream>
#include<vector>
#include<map>
#include<set>
#include<stack>
#include<queue>
#include<algorithm>
#include<cmath>
#include<utility>
#include<iomanip>

using namespace std;

int main() {
  ios_base::sync_with_stdio(false);
  cin.tie(0);
  cout << fixed << setprecision(12);

  int64_t T;
  cin >> T;


  for (int64_t t = 1; t <= T; ++t) {
    cout << "Case #" << t << ": ";
    int64_t N, R, O, Y, G, B, V;
    cin >> N >> R >> O >> Y >> G >> B >> V;
    int64_t charcnt = 0;
    if (max(R, max(B, Y)) > N/2) {
      cout << "IMPOSSIBLE\n";
      continue;
    }
    char c0, c1, c2;
    int64_t a0, a1, a2;
    if (R == max(R, max(B, Y))) {
      c0 = 'R';
      c1 = 'B';
      c2 = 'Y';
      a0 = R;
      a1 = B;
      a2 = Y;
    } else if (B == max(R, max(B, Y))) {
      c0 = 'B';
      c1 = 'R';
      c2 = 'Y';
      a0 = B;
      a1 = R;
      a2 = Y;
    } else {
      c0 = 'Y';
      c1 = 'R';
      c2 = 'B';
      a0 = Y;
      a1 = R;
      a2 = B;
    }
    int lastset = 0;
    for (int64_t i = 0; i < a0; ++i) {
      cout << c0;
      charcnt++;
      if (a1 >= a2) {
        cout << c1;
        charcnt++;
        lastset = 1;
        a1--;
      } else {
        cout << c2;
        charcnt++;
        a2--;
        lastset = 2;
      }
    }
    if (a1 == 0 && a2 == 0) {
      cout << '\n';
      continue;
    }
    if (a1 == a2) {
      for (int64_t i = 0; i < a1; ++i) {
        if (lastset == 2) {
          cout << c1 << c2;
          charcnt+=2;
        } else {
          cout << c2 << c1;
          charcnt+=2;
        }
      }
    } else if (a1 > a2) {
      cout << c1;
      charcnt++;
      a1--;
      for (int64_t i = 0; i < a1; ++i) {
        cout << c2 << c1;
        charcnt+=2;
      }
    } else if (a2 > a1) {
      cout << c2;
      charcnt++;
      a2--;
      for (int64_t i = 0; i < a2; ++i) {
        cout << c1 << c2;
        charcnt+=2;
      }
    }
    if (charcnt != N) cout << "ERRORRORO: " << charcnt << N << endl;
    cout << '\n';
  }
  return 0;
}

