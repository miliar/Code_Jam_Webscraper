#include<bits/stdc++.h>
using namespace std;

int check(int n){
  if (n/10 == 0) return 1;

  vector<int> v;
  while (n > 0) {
    v.push_back(n%10);
    n /= 10;
  }
  reverse(v.begin(), v.end());
  for (int i = 1; i < v.size(); i++) {
    if (v[i] < v[i-1]) return 0;
  }

  return 1;
}

int main(){

  int t;
  scanf("%d", &t);
  for (int tt = 1; tt <= t; tt++) {
    int n;
    scanf("%d", &n);
    int ans = 0;
    for (int i = n; i >= 0; i--) {
      if (check(i)) {
        ans = i;
        break;
      }
    }
    printf("Case #%d: %d\n", tt, ans);
    fprintf(stderr, "test %d solved\n", tt);
  }

  return 0;
}