#include <bits/stdc++.h>
#define _ ios_base::sync_with_stdio(false);cout.tie(0);cin.tie(0);
using namespace std;

vector<long long> t;

void f() {
   
  long long p10[18];
  p10[0] = 1;

  for (int i = 1; i <= 18; i++) {
    p10[i] = p10[i-1]*10;
  }
  for (int i = 1; i < 10; i++) {
    t.push_back(i);
  }
  for (int l = 2; l <= 18; l++) {
    int sz = t.size();

    for (int i = 0; i < sz; i++) {
      long long v = t[i];

      for (int d = 1; d <= v/p10[l-2]; d++) {
        long long u = d*p10[l-1]+v;
        t.push_back(u);
      }
    }
  }
  sort(t.begin(), t.end());
}

int tidy(long long v) {
  
  int maxi = 10;

  while (v) {
    int d = v%10LL;
    v /= 10LL;

    if (maxi < d) {
      return 0;
    }
    maxi = d;
  }
  return 1;
}

void solve() {

  long long v;
  cin >> v;

  if (tidy(v)) {
    cout << v << endl;
  } else {
    cout << *(lower_bound(t.begin(), t.end(), v)-1) << endl;
  }
}

int main() { _
  f();
  
  int T;
  cin >> T;

  for (int tt = 1; tt <= T; tt++) {
    cout << "Case #" << tt << ": ";
    solve();
  }
  return 0;
}

