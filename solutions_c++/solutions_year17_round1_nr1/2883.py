#include<bits/stdc++.h>
using namespace std;

#define endl '\n'
#define D(x) cout << #x << " = " << (x) << endl;
#define IO ios_base::sync_with_stdio(false); cin.tie(NULL);

int mark[33][33];
int r, c;

struct sq {
  int x, y;
  sq () {};
  sq (int a, int b) {
    x = a;
    y = b;
  }
};

bool check (int x, int y) {
  return x >= r || x < 0 || y >= c || y < 0;
}

bool good (int x, int y, int x2, int y2, vector<string> &mat) {
//  cout << x << " " << y << " 111 " << x2 << " " << y2 << endl;
  if (check(x + x2, y + y2)) return false;

//  cout << x << " " << y << "*** " << x2 << " " << y2 << endl;
  set<char> cnt;
  for (int i = 0; i <= x2; ++i) {
    for (int j = 0; j <= y2; ++j) {
//      cout << i + x << " : " << j + y << endl;
      if (mat[i + x][j + y] != '?')
        cnt.insert(mat[i + x][j + y]);
    }
  }

  bool ok = cnt.size() == 1;

  if (ok) {
    char c = *cnt.begin();
//    cout << x << " " << y << " - " << x2 << " " << y2 << endl;
//    D(c)
    for (int i = 0; i <= x2; ++i) {
      for (int j = 0; j <= y2; ++j) {
        mark[i + x][j + y] = true;
        mat[i + x][j + y] = c;
      }
    }
  }

  return ok;
}

bool cmp (sq i, sq j) {
  int a = i.x + 1 * i.y + 1;
  int b = j.x + 1 * j.y + 1;

  if (a == b) {
    if (i.y == j.y) {
      return i.x < j.x;
    }
    return i.y > j.y;
  }

  return a > b;
}

int main() {
  int t, TC = 1;
  cin >> t;

  vector<sq> v;
  int n = 25;
  for (int i = 0; i <= n; ++i) {
    for (int j = 0; j <= n; ++j) {
      if (i == 0 && j == 0) continue;
      v.push_back(sq(i, j));
    }
  }

  sort(v.begin(), v.end(), cmp);
  v.push_back(sq(0, 0));
//  for (int i = 0; i < v.size(); ++i) cout << v[i].x << " ,"  << v[i].y << endl;
//  return 0;

  while (t --> 0) {
    cin >> r >> c;

    memset(mark, 0, sizeof mark);
    vector<string> mat(r);
    for (int i = 0; i < r; ++i) cin >> mat[i];


    bool f = true;
    for (int i = 0; i < r && f; ++i) {
      for (int j = 0; j < c; ++j) {
        if (!mark[i][j]) {
          for (int k = 0; k < v.size(); ++k) {
            int x = v[k].x;
            int y = v[k].y;
            if (good(i , j, x, y, mat)) {
              break;
            }
          }
        }

        if (i == 0 && j == 2) {
//          f = false;
//          break;
        }
      }
    }

    cout << "Case #" << TC ++ << ":" << endl;

/*    if (TC == 85) {
      cout << r << " " << c <<  " " << mat[0] << endl;
      return 0;
    }
*/
    for (int i = 0; i < r; ++i) {
      for (int j = 0; j < c; ++j) {
        cout << mat[i][j];
      }
      cout << endl;
    }
  }

  return 0;
}
