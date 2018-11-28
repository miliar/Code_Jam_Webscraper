#include <bits/stdc++.h>

using namespace std;

int dr[] = {-1, 0, 1, 0};
int dc[] = {0, 1, 0 -1};

int main() {
  int tc;
  cin >> tc;

  for (int t = 1; t <= tc; ++t) {
    int r, c;
    cin >> r >> c;

    vector<vector<char>> v(r, vector<char>(c));

    for (int i = 0; i < r; i++)
      for (int j = 0; j < c; j++)
        cin >> ws >> v[i][j];

    set<char> done;

    for (int i = 0; i < r; i++) {
      for (int j = 0; j < c; j++) {
        if (v[i][j] != '?' && !done.count(v[i][j])) {
          done.insert(v[i][j]);

          int left, right;
          for (left = j-1; left >= 0 && v[i][left] == '?'; --left) {
            v[i][left] = v[i][j];
          }

          for (right = j+1; right < c && v[i][right] == '?'; ++right) {
            v[i][right] = v[i][j];
          }

          left++;
          right--;

          int top;
          for (top = i-1; top >= 0; top--) {
            bool any = false;
            for (int k = left; k <= right; k++) {
              if (v[top][k] != '?') {
                any = true;
                break;
              }
            }

            if (!any) {
              for (int k = left; k <= right; k++)
                v[top][k] = v[i][j];
            } else {
              break;
            }
          }

          int bottom;
          for (bottom = i+1; bottom < r; bottom++) {
            bool any = false;
            for (int k = left; k <= right; k++) {
              if (v[bottom][k] != '?') {
                any = true;
                break;
              }
            }

            if (!any) {
              for (int k = left; k <= right; k++)
                v[bottom][k] = v[i][j];
            } else {
              break;
            }
          }

          // cerr << v[i][j] << " " << left << " " << top << " " << right << " " << bottom << endl;
        }
      }
    }

    cout << "Case #" << t << ":\n";

    for (int i = 0; i < r; i++) {
      for (int j = 0; j < c; j++) {
        cout << v[i][j];
      }
      cout << endl;
    }
  }

  return 0;
}
