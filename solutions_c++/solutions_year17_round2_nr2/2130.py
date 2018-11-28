#include <algorithm>
#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <vector>
#include <utility>

using namespace std;

bool solve(int r, int o, int y, int g, int b, int v, string& res) {
  bool solution = true;

  if (y == 0 && v == 0 && b == 0 && o == 0) {
    if (r != g)
      return false;
    for (int i = 0; i < r; ++i)
      res += "rg";
    return true;
  }

  if ( r == 0 && g == 0 &&  b == 0 && o == 0) {
    if (y != v)
      return false;
    for (int i = 0; i < v; ++i)
      res += "yv";
    return true;
  }

  if ( r == 0 && g == 0 && y == 0 && v == 0) {
    if (b != o)
      return false;
    for (int i = 0; i < b; ++i)
      res += "bo";
    return true;
  }

  if (g > r + 1) {
    return false;
  }

  if (g != 0) {
    r -= g + 1;
    if (r == 0)
      r = 1;
  }

  if (v > y + 1) {
    return false;
  }

  if (v != 0) {
    y -= v + 1;

    if (y == 0)
      y = 1;
  }

  if (o > b + 1) {
    return false;
  }
  if (o != 0) {
    b -= o + 1;

    if (b == 0)
      b = 1;
  }

  vector<int> a = {r, b, y};
  vector<char> ch = {'r', 'b', 'y'};

  int m1 = 0;
  for (int i = 1; i < 3; ++i)
    if (a[i] > a[m1])
      m1 = i;

  res += ch[m1];
  a[m1]--;

  while (a[0] > 0 || a[1] > 0 || a[2] > 0) {
    int m2 = 0;
    if (m1 == 0)
      m2 = 1;
    for (int i = 0; i < 3; ++i)
      if (i != m1 && a[i] > a[m2])
        m2 = i;

    if (a[m2] == 0)
      return false;

    res += ch[m2];
    a[m2]--;
    m1 = m2;
  }

  if (res.size() > 1 && res.front() == res.back()) {
    if (res.front() == 'r') {
      int p1 = res.find("yby");
      int p2 = res.find("byb");

      if (p1 != string::npos) {
        swap(res[p1 + 1], res.front());
      } else if (p2 != string::npos) {
        swap(res[p2 + 1], res.front());
      } else {
        if (res.size() > 3) {
          int i = res.size()-2;
          if (res[i-1] != 'r' && res[i] != res[i - 2]) {
            swap(res[i], res.back());
            return true;
          }
        }

        return false;
      }
    } else if (res.front() == 'b') {
      int p1 = res.find("yry");
      int p2 = res.find("ryr");

      if (p1 != string::npos) {
        swap(res[p1 + 1], res.front());
      } else if (p2 != string::npos) {
        swap(res[p2 + 1], res.front());
      } else {
        if (res.size() > 3) {
          int i = res.size()-2;
          if (res[i-1] != 'b' && res[i] != res[i - 2]) {
            swap(res[i], res.back());
            return true;
          }
        }

        return false;
      }
    } else if (res.front() == 'y') {
      int p1 = res.find("brb");
      int p2 = res.find("rbr");

      if (p1 != string::npos) {
        swap(res[p1 + 1], res.front());
      } else if (p2 != string::npos) {
        swap(res[p2 + 1], res.front());
      } else {
        if (res.size() > 3) {
          int i = res.size()-2;
          if (res[i-1] != 'y' && res[i] != res[i - 2]) {
            swap(res[i], res.back());
            return true;
          }
        }
        return false;
      }
    }
  }

  if (g > 0) {
    int p = res.find('r');
    string tm;
    int i = 0;
    for (int i = 0; i < p; ++i)
      tm += res[i];
    for (int i = 0; i < g; ++i)
      tm += "rg";
    tm += 'r';
    for (int i = p + 1; i < res.size(); ++i)
      tm += res[i];
    res = tm;
  }
  if (v > 0) {
    int p = res.find('y');
    string tm;
    int i = 0;
    for (int i = 0; i < p; ++i)
      tm += res[i];
    for (int i = 0; i < g; ++i)
      tm += "yv";
    tm += 'y';
    for (int i = p + 1; i < res.size(); ++i)
      tm += res[i];
    res = tm;
  }
  if (o > 0) {
    int p = res.find('b');
    string tm;
    int i = 0;
    for (int i = 0; i < p; ++i)
      tm += res[i];
    for (int i = 0; i < g; ++i)
      tm += "bo";
    tm += 'b';
    for (int i = p + 1; i < res.size(); ++i)
      tm += res[i];
    res = tm;
  }

  return true;
}

int main() {
  int T = 0;
  cin >> T;

  for (int test = 1; test <= T; ++test) {
    int n;
    cin >> n;
    int r, o, y, g, b, v;
    cin >> r >> o >> y >> g >> b >> v;

    string res;
    bool sol = solve(r, o, y, g, b, v, res);

    if (sol) {
      cout << "Case #" << test << ": " << res << endl;
    } else {
      cout << "Case #" << test << ": IMPOSSIBLE" << endl;
    }
  }
}
