#include <bits/stdc++.h>
using namespace std;

int main(void) {
  if (fopen("probBsmall.in", "r")) {
    freopen("probBsmall.in", "r", stdin);
    freopen("probBsmall.out", "w", stdout);
  }
  if (fopen("probBlarge.in", "r")) {
    freopen("probBlarge.in", "r", stdin);
    freopen("probBlarge.out", "w", stdout);
  }
  int t;
  cin >> t;
  for (int i = 1; i <= t; i++) {
    int n;
    vector<int> ans;
    int num[3], ex;
    cin >> n;
    cin >> num[0] >> ex >> num[1] >> ex >> num[2] >> ex;
    int e1 = 0, e2 = 1, e3 = 2;
    for (int j = 0; j < 3; j++) {
      if (num[j] < num[e1]) e1 = j;
      if (num[j] > num[e3]) e3 = j;
    }
    e2 = 3 - e1 - e3;
    int a = num[e1] + num[e2] - num[e3];
    if (a < 0) {
      printf("Case #%d: IMPOSSIBLE\n", i);
      continue;
    }
    if (num[e3] < a) {
      printf("Case #%d: IMPOSSIBLE\n", i);
      continue;
    }
    for (int j = 0; j < a; j++) {
      ans.push_back(e3);
      ans.push_back(e1);
      ans.push_back(e2);
      num[0]--;
      num[1]--;
      num[2]--;
    }
    for (int j = 0; j < num[e2]; j++) {
      ans.push_back(e3);
      ans.push_back(e2);
    }
    for (int j = 0; j < num[e1]; j++) {
      ans.push_back(e3);
      ans.push_back(e1);
    }
    printf("Case #%d: ", i);
    for (int j = 0; j < n; j++) {
      if (ans[j] == 0) printf("R");
      if (ans[j] == 1) printf("Y");
      if (ans[j] == 2) printf("B");
    }
    printf("\n");
  }
  return 0;
}
