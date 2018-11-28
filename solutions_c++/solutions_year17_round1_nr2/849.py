#include <bits/stdc++.h>
using namespace std;

int rc, qc;
int rs[60], qss[60][60];
int pos[60];

int solve() {
  int ret = 0;
  for(int i = 0; i < rc; i++) {
    sort(qss[i], qss[i] + qc);
    pos[i] = 0;
  }
  for(int n = 1; n <= 1e6; n++) {
    bool flag = true;
    for(int i = 0; i < rc; i++) {
      while(pos[i] < qc && 1ll * qss[i][pos[i]] * 10 < 1ll * rs[i] * n * 9) {
        pos[i]++;
      }
      if(pos[i] >= qc) {
        flag = false;
        break;
      }
    }
    if(!flag) break;
    for(int i = 0; i < rc; i++) {
      if(1ll * qss[i][pos[i]] * 10 > 1ll * rs[i] * n * 11) {
        flag = false;
        break;
      }
    }
    if(!flag) continue;
    ret++;
    for(int i = 0; i < rc; i++) {
      pos[i]++;
    }
    n--;
  }
  return ret;
}

int main() {
  int kase;
  scanf("%d", &kase);
  for(int ka = 1; ka <= kase; ka++) {
    scanf("%d%d", &rc, &qc);
    for(int i = 0; i < rc; i++) {
      scanf("%d", &rs[i]);
    }
    for(int i = 0; i < rc; i++) {
      for(int j = 0; j < qc; j++) {
        scanf("%d", &qss[i][j]);
      }
    }
    printf("Case #%d: %d\n", ka, solve());
  }
  return 0;
}
