#include <stdio.h>
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

void solve() {
    int N, Cl, P;
    scanf("%d %d %d", &N, &Cl, &P);
    std::vector<int> C(Cl + 1, 0);
    std::vector<int> S(N + 1, 0);
    int ans1 = 1;
    for (int m = 0; m < P; m++) {
        int c, s;
        scanf("%d %d", &s, &c);
        S[s]++;
        C[c]++;
        if (ans1 < C[c]) ans1 = C[c];
    }
    int sum = 0;
    for (int s = 1; s <= N; s++) {
        sum += S[s];
        if (ans1 * s < sum) ans1 = (sum + s - 1) / s; 
    }
    int ans2 = 0;
    for (int s = 1; s <= N; s++) {
        if (S[s] > ans1) ans2 += S[s] - ans1; 
    }
    printf("%d %d", ans1, ans2);
}

int main() {
  int T;
  scanf("%d\n", &T);
  for (int t = 1; t <= T; t++) {
    printf("Case #%d: ", t);
    solve();
    printf("\n");
  }
  return 0;
}
