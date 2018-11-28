#include <iostream>
#include <vector>
#include <cassert>
#include <algorithm>

using namespace std;

typedef vector<int> rect_t;

int main() {
  int T;
  cin >> T;
  for (int t = 0; t < T; t++) {

    int size[2];
    cin >> size[0] >> size[1];

    vector<pair<int, int> > ps;
    vector<char> cs;
    for (int i = 0; i < size[0]; i++) {
      string s;
      cin >> s;
      for (int j = 0; j < size[1]; j++) {
        if (s[j] != '?') {
          ps.push_back(make_pair(i, j));
          cs.push_back(s[j]);
        }
      }
    }

    vector<int> r0;
    r0.push_back(0);
    r0.push_back(size[0]);
    r0.push_back(0);
    r0.push_back(size[1]);

    vector<rect_t> rects;
    rects.push_back(r0);

    for (int i = 1; i < ps.size(); i++) {
      auto p = ps[i];

      int rix;
      for (rix = 0; rix < rects.size(); rix += 1) {
        auto r = rects[rix];
        if (r[0] <= p.first && p.first < r[1] && r[2] <= p.second && p.second < r[3]) {
          break;
        }
      }
      /*
      for (auto s : rects) {
      cout << "rect " << "" << " " << s[0] << " " << s[1] << " " << s[2] << " " << s[3] << endl;

      }
      */
      assert(rix != rects.size());

      auto r = rects[rix];
      auto rp = ps[rix];
      rect_t s(4);

      // split with vertical line
      if (rp.first == p.first) {
        if (rp.second < p.second) {
          s[0] = r[0];
          s[1] = r[1];
          s[2] = p.second;
          s[3] = r[3];
          rects[rix][3] = p.second;
        } else {
          s[0] = r[0];
          s[1] = r[1];
          s[2] = r[2];
          s[3] = rp.second;
          rects[rix][2] = rp.second;
        }

      // split with horizontal line
      } else {
        if (rp.first < p.first) {
          s[0] = p.first;
          s[1] = r[1];
          s[2] = r[2];
          s[3] = r[3];
          rects[rix][1] = p.first;
        } else {
          s[0] = r[0];
          s[1] = rp.first;
          s[2] = r[2];
          s[3] = r[3];
          rects[rix][0] = rp.first;
        }
      }

      //cout << "add rect " << cs[i] << " " << s[0] << " " << s[1] << " " << s[2] << " " << s[3] << endl;
      //cout << "split from " << cs[rix] << " " << r[0] << " " << r[1] << " " << r[2] << " " << r[3] << endl;
      rects.push_back(s);
    }


    char zs[25][25];
    for (int rix = 0; rix < rects.size(); rix++) {
      auto r = rects[rix];
      for (int i = r[0]; i < r[1]; i++) {
        for (int j = r[2]; j < r[3]; j++) {
          zs[i][j] = cs[rix];
        }
      }
    }


    cout << "Case #" << (t + 1) << ": " << endl;
    for (int i = 0; i < size[0]; i++) {
      for (int j = 0; j < size[1]; j++) {
        cout << zs[i][j];
      }
      cout << endl;
    }
  }

  return 0;
}
