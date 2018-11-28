#include <iostream>
#include <stdio.h>
#include <string>
#include <algorithm>
#include <vector>
#include <set>

using namespace std;

typedef unsigned long long ull;

void solve(ull N, ull K) {
  multiset<ull> gaps;
  gaps.insert(N);

  for (ull k = 0; k < K; ++k) {
    ull max_gap = *(--gaps.end());
    gaps.erase(--gaps.end());

    ull ls = max_gap/2;
    ull rs = max_gap/2;
    if (max_gap%2==0)ls--;

    if (k == K-1) {
      cout << max(rs,ls) << " " << min(rs,ls);
    }
    else {
      if (ls > 0) gaps.insert(ls);
      if (rs > 0) gaps.insert(rs);
    }
  }
}

int main() {
  int T;
  cin >> T;
  
  for (int t = 0; t < T; ++t) {
    ull k, n;
    cin >> n >> k;

    cout << "Case #" << t+1 <<": "; 
    solve(n,k);
    cout << '\n';
  }

  return 0;
}