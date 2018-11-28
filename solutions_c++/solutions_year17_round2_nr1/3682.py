/*
 Author:    sergioRG
*/
#include <bits/stdc++.h>
using namespace std;
typedef long double ld;
const ld epsilon = 1e-9;

bool appr(ld a, ld b) {
  return abs(a-b) < epsilon;
}

ld get_collision_time(const pair<ld, ld>& h1, const pair<ld, ld>& h2) {
  if( appr(h1.second, h2.second) ) return 1e18;
  return (h1.first - h2.first) / (h2.second - h1.second);
}

int main() {
  ios_base::sync_with_stdio(false); cin.tie(0);
  cout.setf(ios::fixed);
  cout.precision(12);
  int T;
  cin >> T;
  for(int tc=1; tc<=T; ++tc) {
    ld d;
    cin >> d;
    int n;
    cin >> n;
    set< pair<ld, ld> > S;
    for(int i=0; i<n; ++i) {
      pair<ld, ld> x;
      cin >> x.first >> x.second;
      S.insert(x);
    }
    bool converges = false;
    ld accm_time = 0.0;
    while(!converges) {
      /*
      for(auto x : S) {
        cout << x.first << " " << x.second << endl;
      }
      cout << "------ STEP ------" << endl;
      */
      converges = true;
      pair<ld, ld> a, b;
      ld best_col_time = 1e16;
      auto it = S.begin();
      while(it != S.end()) {
        auto nxt = it; ++nxt;
        if(nxt == S.end()) break;
        ld col_time = get_collision_time(*it, *nxt);
        ld col_pos = (*it).first + col_time*(*it).second;
        if(col_pos <= d && best_col_time > col_time && col_time >= 0.0) {
          a = *it, b = *nxt;
          best_col_time = col_time;
        }
        ++it;
      }
      if(best_col_time <= 1e15) {
        accm_time += best_col_time;
        converges = false;
        set< pair<ld, ld> > new_S;
        S.erase(a);
        S.erase(b);
        ld new_speed = min(a.second, b.second);
        ld new_pos   = min(a.first, b.first) + best_col_time*max(a.second, b.second);
        new_S.insert({new_pos, new_speed});
        for(auto x : S) {
          new_S.insert({x.first + best_col_time*x.second, x.second});
        }
        S = new_S;
      }
    }
    auto fc = *S.begin();
    ld time_to_d = (d - fc.first) / fc.second;
    time_to_d += accm_time;
    ld ans = d / time_to_d;
    cout << "Case #" << tc << ": ";
    cout << ans << endl;
  }
}
