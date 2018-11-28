#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <cstdio>
#include <cassert>

using namespace std;

int main() {
  int T; cin >> T;
  for (int t = 1; t <= T; t++) {
    int N, M;
    cin >> N >> M;

    set<int> rws, cls, dr, dl;
    for (int i = 0; i < N; i++) {
      rws.insert(i);
      cls.insert(i);
    }
    for (int i = 0; i < 2 * N - 1; i++) {
      dr.insert(i);
      dl.insert(i);
    }

    vector<string> oboard(N, string(N, '_'));
    vector<vector<bool> > xtype(N, vector<bool>(N));
    vector<vector<bool> > plustype(N, vector<bool>(N));
    for (int i = 0; i < M; i++) {
      char ch;
      int r, c;
      cin >> ch >> r >> c;
      r--;
      c--;
      oboard[r][c] = ch;
      if (ch != 'x') {
        dr.erase(r + c);
        dl.erase(r + N - c - 1);
        plustype[r][c] = true;
      }
      if (ch != '+') {
        rws.erase(r);
        cls.erase(c);
        xtype[r][c] = true;
      }
    }

    vector<int> vrws(rws.begin(), rws.end());
    vector<int> vcls(cls.begin(), cls.end());

    assert(vrws.size() == vcls.size());
    for (int i = 0; i < vrws.size(); i++) {
      xtype[vrws[i]][vcls[i]] = true;
    }

    for (int p = 0; p < 2; p++) {
      vector<int> vdr;
      vector<int> vdl;
      for (auto i : dr) {
        if (i % 2 == p) {
          vdr.push_back(i);
        }
      }
      for (auto i : dl) {
        if ((i + N + 1) % 2 == p) {
          vdl.push_back(i);
        }
      }
      sort(vdr.rbegin(), vdr.rend(), [N](int x, int y) {
        int dd = min(x, 2 * N - 2 - x) - min(y, 2 * N - 2 - y);
        return dd < 0 || (dd == 0 && x < y);
      });
      sort(vdl.begin(), vdl.end(), [N](int x, int y) {
        int dd = min(x, 2 * N - 2 - x) - min(y, 2 * N - 2 - y);
        return dd < 0 || (dd == 0 && x < y);
      });

      int ji = 0;
      for (auto i : vdr) {
        while (ji < vdl.size()) {
          int j = vdl[ji++];
          int r = (i + j - N + 1) / 2;
          int c = i - r;
          if (0 <= r && r < N && 0 <= c && c < N) {
            plustype[r][c] = true;
            break;
          }
        }
      }
    }

    int result = 0;
    vector<pair<char, pair<int, int> > > changes;
    for (int i = 0; i < N; i++) {
      for (int j = 0; j < N; j++) {
        char ch = '_';
        if (xtype[i][j] && plustype[i][j]) {
          ch = 'o';
        } else if (xtype[i][j]) {
          ch = 'x';
        } else if (plustype[i][j]) {
          ch = '+';
        }
        result += xtype[i][j] ? 1 : 0;
        result += plustype[i][j] ? 1 : 0;
        if (ch != oboard[i][j]) {
          changes.push_back(make_pair(ch, make_pair(i + 1, j + 1)));
        }
      }
    }
    cout << "Case #" << t << ": " << result << ' ' << changes.size() << '\n';
    for (auto i : changes) {
      cout << i.first << ' ' <<
              i.second.first << ' ' << i.second.second << '\n';
    }
  }
  return 0;
}
