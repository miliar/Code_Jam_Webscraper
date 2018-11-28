#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

typedef long long lol;
typedef vector<int> VI;
typedef vector<VI> VVI;

#define Loop(i, a, b) for (int i = (a); i < (b); ++i)
#define Loopb(i, a, b) for (int i = (a - 1); i >= (b); --i)

void remake(string &ans, VI &vec) {
  string st;
  if (vec[1]) {
    string str;
    st = "BO";
    Loop(i, 0, vec[1]) str += st;
    int c = ans.find('B');
    ans = ans.substr(0, c) + str + ans.substr(c);
  }
  if (vec[3]) {
    string str;
    st = "RG";
    Loop(i, 0, vec[3]) str += st;
    int c = ans.find('R');
    ans = ans.substr(0, c) + str + ans.substr(c);
  }
  if (vec[5]) {
    string str;
    st = "YV";
    Loop(i, 0, vec[5]) str += st;
    int c = ans.find('Y');
    ans = ans.substr(0, c) + str + ans.substr(c);
  }
  //  cout << "ok\n";
}

int main() {

#ifdef LocalHost
  //freopen("input", "rt", stdin);
  freopen("B-small-attempt0.in", "rt", stdin);
  //freopen("B-large.in", "rt", stdin);
  freopen("output.txt", "w", stdout);
#endif

  int line_num;
  cin >> line_num;

  for (int line = 0; line < line_num; ++line) {
    int n; VI vec(6), red(3);
    cin >> n;
    Loop(i, 0, 6) cin >> vec[i];
    bool b = true, bl = false; int bb = 0;
    Loop (i, 0, 3) {
      //cout << vec[2 * i] << " " << vec[2 * i + 3] << " " << b << "\n";
      int w = (2 * i + 3) % 6;
      b = b && (vec[2 * i] > vec[w] ||
                ( (vec[2 * i] == vec[w]) && ( (vec[w] == 0) || (vec[2 * i] + vec[w] == n))));
      if (vec[2 * i] == vec[w] && vec[2 * i] + vec[w] == n) bb = i + 1;
    }
    //cout << b << "\n";
    string ans = "";
    if (bb) {
      string str;
      if (bb == 1) str = "RG";
      if (bb == 2) str = "OB";
      if (bb == 3) str = "YV";
      Loop (i, 0, n / 2) ans = ans + str;
    } else {
    if (b) {
      Loop(i, 0, 3) {int w = (2 * i + 3) % 6; red[i] = vec[2 * i] - vec[w];}
      Loop(i, 0, 3) if (red[i] > (red[(i + 1) % 3] + red[(i + 2) % 3])) b = false;
    }
    if (b && !bb) {
      while (red[0] > 1)
        if (red[1] > red[2]) {
          ans = ans + "RY";
          --red[1];
          --red[0];
          bl = false;
        } else  {
          ans = ans + "RB";
          --red[2];
          --red[0];
          bl = true;
        }
      if (red[0]) {ans = ans + "R"; bl = true;}
      while (red[1] + red[2] > 0)
        if (red[1] > red[2] || (red[1] == red[2] && bl)) {ans = ans + "Y"; --red[1]; bl = false;}
        else {ans = ans + "B"; --red[2]; bl = true;}
      remake(ans, vec);

    } else ans = "IMPOSSIBLE";
    }
    printf("Case #%d: %s\n", line+1, ans.c_str());
  }
  return 0;
}
