#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

const int MAX_N = 30;

char val[MAX_N][MAX_N];
int r, c;

int populated(int bottom) {
  while (bottom < r) {
    bool has = false;
    for (int j = 0; j < c; j++) {
      if (val[bottom][j] != '?')
        has = true;
    }

    if (has)
      break;
    else
      bottom++;
  }

  return bottom;
}

vector < pair < int, char > > get_cols(int top, int next) {
  vector < pair < int, char > > cols;
  for (int j = 0; j < c; j++) {
    char c = '.';
    for (int i = top; i < next; i++) {
      if (val[i][j] != '?') {
        c = val[i][j];
        break;
      }
    }

    if (c != '.') {
      cols.push_back(make_pair(j, c));
    }
  }

  return cols;
}

int main() {
  int t; cin >> t;
  for (int test = 1; test <= t; test++) {
    cin >> r >> c;
    for (int i = 0; i < r; i++)
      for (int j = 0; j < c; j++)
        cin >> val[i][j];

    int bottom = 0;
    while (true) {
      int top = populated(bottom);
      if (top == r) break;
      int next = populated(top + 1); // exclusive

      // cout << "top " << top << " next " << next << endl;

      vector <pair<int, char> > cols = get_cols(top, next);
      cols.push_back(make_pair(c, '?'));
      cols.insert(cols.begin(), cols[0]);
      cols[0].first = 0;
      for (int i = 0; i < (int) cols.size() - 1; i++) {
        int col = cols[i].first;
        char c = cols[i].second;

        // cout << "col " << col << " c " << c << endl;

        int col2 = cols[i + 1].first;

        for (int j = col; j < col2; j++) {
          for (int k = bottom; k < next; k++)
            val[k][j] = c;
        }
      }

      bottom = next;
    }

    cout << "Case #" << test << ":" << endl;
    for (int i = 0; i < r; i++) {
      for (int j = 0; j < c; j++)
        cout << val[i][j];
      cout << endl;
    }
  }
}
