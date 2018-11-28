#include <bits/stdc++.h>
using namespace std;

string str_rep(string s, int n) {
  string ret = "";
  for(int i = 0; i < n; i++) {
    ret += s;
  }
  return ret;
}


int main() {
  int T;
  cin >> T;
  for(int t = 0; t < T; t++) {
    int N;
    cin >> N;

    int R, O, Y, G, B, V;
    cin >> R >> O >> Y >> G >> B >> V;

    int a, b, c;
    string ans = "";

    a = Y + B - R;
    b = R - B;
    c = R - Y;

    if(a >= 0 && b >= 0 && c >= 0) {
      ans = str_rep("RBY", a) + str_rep("RY", b) + str_rep("RB", c);
    }

    a = R + Y - B;
    b = B - Y;
    c = B- R;

    if(a >= 0 && b >= 0 && c >= 0) {
      ans = str_rep("BYR", a) + str_rep("BR", b) + str_rep("BY", c);
    }

    a = B + R - Y;
    b = Y - R;
    c = Y - B;

    if(a >= 0 && b >= 0 && c >= 0) {
      ans = str_rep("YRB", a) + str_rep("YB", b) + str_rep("YR", c);
    }
    if(ans.length() == 0) ans = "IMPOSSIBLE";

    cout << "Case #" << t + 1 << ": " << ans << endl;
  }
}
