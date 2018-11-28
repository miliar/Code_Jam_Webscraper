#include <bits/stdc++.h>
#include <stdint.h>

using namespace std;


struct Pancake {
  int r, h;
  
  static bool compareS(Pancake const &a, Pancake const &b) {
    return a.h * int64_t(a.r) < b.h * int64_t(b.r);
  }
};



void test(bool verbose) {
  int n, k;
  cin >> n >> k;
  
  vector<Pancake> P(n);
  for(int i = 0; i < n; i++) cin >> P[i].r >> P[i].h;
  
  if(not verbose) return;
  
  sort(P.begin(), P.end(), Pancake::compareS);
  reverse(P.begin(), P.end());
  
  double ans = 0.0;
  
  for(int i0 = 0; i0 < n; i0++) {
    int maxR = P[i0].r;
    double sumH = P[i0].h;
    double top  = M_PI * maxR * maxR;
    double side = (2.0 * M_PI * P[i0].r) * P[i0].h;
    
    int picked = 1;
    for(int i = 0; i < n; i++) {
      if(P[i].r > maxR) continue;
      if(i == i0) continue;
      if(picked >= k) break;
      sumH += P[i].h;
      side += (2.0 * M_PI * P[i].r) * P[i].h;
      picked++;
    }
    
    if(picked < k) continue;
    
    ans = max(ans, top + side);
  }
  
  cout << setprecision(9) << fixed << ans << '\n';
}



int main(int argc, char const **argv) {
  ios_base::sync_with_stdio(false);
#ifndef FORCE_TIE
  cin.tie(NULL);
#endif
  
  int z = (argc > 1 ? atoi(argv[1]) : -1);
  
  int t;
  cin >> t;
  
  for(int i = 1; i <= t; i++) {
    bool verbose = (z == -1 or z == i);
    if(verbose) cout << "Case #" << i << ": ";
    test(verbose);
  }
  
  return 0;
}
