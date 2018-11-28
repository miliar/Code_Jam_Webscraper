#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>

using namespace std;

int main() {
  ios_base::sync_with_stdio(0);
  cin.tie(0);

  int T; cin >> T;
  for (int tc = 1; tc <= T; tc++) {
    cout << "Case #" << tc << ":" << endl;
    int r, c;
    cin >> r >> c;
    vector<string> grid(r);
    for (int i = 0; i < r; i++)
      cin >> grid[i];
    set<char> chars;
    map<char, int> firstrow;
    map<char, int> firstcol;
    map<char, int> lastrow;
    map<char, int> lastcol;
    for (int i = 0; i < r; i++) {
      for (int j = 0; j < c; j++) {
        char ch = grid[i][j];
        if (ch == '?') continue;
        if (chars.find(ch) == chars.end()) {
          chars.insert(ch);
          firstrow[ch] = r+1;
          lastrow[ch] = -1;
          firstcol[ch] = c+1;
          lastcol[ch] = -1;
        }
        firstrow[ch] = min(firstrow[ch], i);
        firstcol[ch] = min(firstcol[ch], j);
        lastrow[ch] = max(lastrow[ch], i);
        lastcol[ch] = max(lastcol[ch], j);
      }
    }
    for (char ch : chars) {
      for (int i = firstrow[ch]; i <= lastrow[ch]; i++) {
        for (int j = firstcol[ch]; j <= lastcol[ch]; j++) {
          grid[i][j] = ch;
        }
      }
    }
    char fil;
    for (int i = 0; i < r; i++) {
      fil = '?';
      for (int k = 0; k < c; k++) {
        if (grid[i][k] != '?') {
          fil = grid[i][k];
          break;
        }
      }
      for (int j = 0; j < c; j++) {
        char ch = grid[i][j];
        if (ch != '?') fil = ch;
        grid[i][j] = fil;
      }
    }
    for (int i = 0; i < c; i++) {
      fil = '?';
      for (int k = 0; k < r; k++) {
        if (grid[k][i] != '?') {
          fil = grid[k][i];
          break;
        }
      }
      for (int j = 0; j < r; j++) {
        char ch = grid[j][i];
        if (ch != '?') fil = ch;
        grid[j][i] = fil;
      }
    }

    for (int i = 0; i < r; i++) {
      for (int j = 0; j < c; j++) {
        cout << grid[i][j];
      }
      cout << endl;
    }
  }
}
