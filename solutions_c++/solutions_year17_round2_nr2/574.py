#include<stdio.h>
#include<stdlib.h>
#include<vector>
#include<algorithm>
#include<cassert>

using namespace std;

bool cmp(const pair<char, int> &a, const pair<char, int> &b) {
  return a.second > b.second;
}

int main() {
  int t;

  scanf("%d", &t);
  for (int k = 0; k < t; k++) {
    int n, r, o, y, g, b, v;

    scanf("%d %d %d %d %d %d %d", &n, &r, &o, &y ,&g ,&b ,&v);

    printf("Case #%d: ", k + 1);

    if (o >= b && o != 0) {
      if (o == b && n == o + b) {
        for (int i = 0; i < n / 2; i++) {
          printf("BO");
        }
      } else {
        printf("IMPOSSIBLE");
      }
      printf("\n");
      continue;
    }
    if (g >= r && g != 0) {
      if (g == r && n == g + r) {
        for (int i = 0; i < n / 2; i++) {
          printf("RG");
        }
      } else {
        printf("IMPOSSIBLE");
      }
      printf("\n");
      continue;
    }
    if (v >= y && v != 0) {
      if (v == y && n == v + y) {
        for (int i = 0; i < n / 2; i++) {
          printf("YV");
        }
      } else {
        printf("IMPOSSIBLE");
      }
      printf("\n");
      continue;
    }

    b = b - o;
    r = r - g;
    y = y - v;

    if (b == 0 && r == 0 && y == 0) {
      if (o != 0 || g != 0 || v != 0) {
        printf("IMPOSSIBLE");
      }
      printf("\n");
      continue;
    }

    vector<char> ol;
    vector<pair<char, int>> dl;

    dl.emplace_back('B', b);
    dl.emplace_back('R', r);
    dl.emplace_back('Y', y);
    sort(dl.begin(), dl.end(), cmp);

    for (int i = 0; i < dl[2].second; i++) {
      ol.push_back(dl[0].first);
      ol.push_back(dl[1].first);
      ol.push_back(dl[2].first);
      dl[0].second -= 1;
      dl[1].second -= 1;
    }
    for (int i = 0; i < dl[1].second; i++) {
      ol.push_back(dl[0].first);
      ol.push_back(dl[1].first);
      dl[0].second -= 1;
    }
    if (ol.size() == 0) {
      ol.push_back(dl[0].first);
      dl[0].second -= 1;
    }

    vector<char> ul;
    vector<char> vl;

    for (int i = 0; i < ol.size(); i++) {
      ul.push_back(ol[i]);
    }

    if (o > 0) {
      int i;
      for (i = 0; i < ul.size(); i++) {
        vl.push_back(ul[i]);
        if (ul[i] == 'B') {
          break;
        }
      }
      assert(i != ul.size());
      for (int j = 0; j < o; j++) {
        vl.push_back('O');
        vl.push_back('B');
      }
      for (i = i + 1; i < ul.size(); i++) {
        vl.push_back(ul[i]);
      }
      ul.clear();
      for (int i = 0; i < vl.size(); i++) {
        ul.push_back(vl[i]);
      }
      vl.clear();
    }

    if (g > 0) {
      int i;
      for (i = 0; i < ul.size(); i++) {
        vl.push_back(ul[i]);
        if (ul[i] == 'R') {
          break;
        }
      }
      assert(i != ul.size());
      for (int j = 0; j < g; j++) {
        vl.push_back('G');
        vl.push_back('R');
      }
      for (i = i + 1; i < ul.size(); i++) {
        vl.push_back(ul[i]);
      }
      ul.clear();
      for (int i = 0; i < vl.size(); i++) {
        ul.push_back(vl[i]);
      }
      vl.clear();
    }

    if (v > 0) {
      int i;
      for (i = 0; i < ul.size(); i++) {
        vl.push_back(ul[i]);
        if (ul[i] == 'Y') {
          break;
        }
      }
      assert(i != ul.size());
      for (int j = 0; j < v; j++) {
        vl.push_back('V');
        vl.push_back('Y');
      }
      for (i = i + 1; i < ul.size(); i++) {
        vl.push_back(ul[i]);
      }
      ul.clear();
      for (int i = 0; i < vl.size(); i++) {
        ul.push_back(vl[i]);
      }
      vl.clear();
    }

    int i;
    for (i = 0; i < ul.size(); i++) {
      vl.push_back(ul[i]);
      if (dl[0].second > 0) {
        if (i + 1 < ul.size()) {
          char pre = ul[i];
          char nxt = ul[i + 1];
          if (pre != 'O' && pre != 'G' && pre != 'V'
              && nxt != 'O' && nxt != 'G' && nxt != 'V'
              && pre != dl[0].first && nxt != dl[0].first) {
            vl.push_back(dl[0].first);
            dl[0].second -= 1;
          }
        }
      }
    }

    if (dl[0].second > 0) {
      printf("IMPOSSIBLE\n");
    } else {
      for (int i = 0; i < vl.size(); i++) {
        printf("%c", vl[i]);
      }
      printf("\n");
    }
  }

  return 0;
}
