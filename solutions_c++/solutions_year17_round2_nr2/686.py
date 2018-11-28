#include <algorithm>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <vector>
using namespace std;
//                               1    2    3    4    5    6
const char colorname[] = {'\0', 'R', 'Y', 'O', 'B', 'V', 'G'};
int T;
int N;
int color[8];
int order[6];
vector<char> ans;
int main() {
  scanf("%d\n", &T);
  for (int TT = 1; TT <= T; TT++) {

    scanf("%d", &N);
    // N, R, O, Y, G, B, and V.
    color[0] = -1;
    scanf("%d%d%d%d%d%d", color + 1, color + 3, color + 2, color + 6, color + 4,
          color + 5);
    for (int i = 0; i < 6; i++) {
      order[i] = i + 1;
    }
    sort(order, order + 6, [=](const int &a, const int &b) -> bool {
      return color[a] > color[b];
    });
    printf("Case #%d: ", TT);
    if (color[order[0]] > color[order[1]] + color[order[2]]) {
      printf("IMPOSSIBLE\n");
      continue;
    }
    ans.resize(0);
    for (int i = 0; i < color[order[0]]; i++) {
      ans.push_back(colorname[order[0]]);
      if (i < color[order[1]]) {
        ans.push_back(colorname[order[1]]);
      }
      if (i >= color[order[1]] || i < color[order[1]] + color[order[2]] - color[order[0]]) {
        ans.push_back(colorname[order[2]]);
      }
    }
    for (int i=0; i < N; i++) {
      printf("%c", ans[i]);
    }
    printf("\n");
  }
  return 0;
}
