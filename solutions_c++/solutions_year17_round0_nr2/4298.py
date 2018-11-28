#include <bits/stdc++.h>
using namespace std;

using LLI = long long int;

int T;
LLI N;

bool check(LLI x) {
  int prev = 10;
  while (x > 0) {
    if (prev < x%10) return false;
    prev = x%10;
    x /= 10;
  }
  return true;
}

LLI Convert(vector<int> &ds) {
  LLI ret = 0;
  for (int a : ds) {
    ret = ret*10 + a;
  }
  return ret;
}

int main() {
  scanf("%d", &T);
  for (int Case=1; Case<=T; Case++) {
    scanf("%lld", &N);
    printf("Case #%d: ", Case);
    if (check(N)) {
      printf("%lld\n", N);
      continue;
    }

    vector<int> ds;
    while (N > 0) {
      ds.emplace_back(N%10);
      N /= 10;
    }
    reverse(ds.begin(), ds.end());

    int idx = ds.size()-1;
    while (1) {
      ds[idx] = 9;
      assert(idx >= 1);
      ds[idx-1]--;
      if (ds[idx-1] == -1) {
        idx--;
        continue;
      }

      LLI t = Convert(ds);
      if (check(t)) {
        printf("%lld\n", t);
        break;
      }

      idx--;
    }
  }
}
