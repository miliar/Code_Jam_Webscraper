#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int, int> pi;



int main() {
  ios_base::sync_with_stdio(false); cin.tie(NULL); cout.precision(20);
  int T;
  cin >> T;
  for (int t = 1;  t <= T; t++) {
    int ac, aj;
    cin >> ac >> aj;
    int nact = ac + aj;
    vector<pair<pi, int> > act(nact);
    int tc, tj, tm;
    tc = tj = tm = 0;
    for (int i = 0; i < ac; i++) {
      cin >> act[i].first.first >> act[i].first.second;
      act[i].second = 0;
      tc += act[i].first.second - act[i].first.first;
    }
    for (int i = 0; i < aj; i++) {
      cin >> act[i].first.first >> act[i].first.second;
      act[i].second = 1;
      tj += act[i].first.second - act[i].first.first;
    }
    sort(act.begin(), act.end());
    vector<int> gapc, gapj, gapm;
    for (int i = 0; i < nact-1; i++) {
      int forat  = act[i+1].first.first-act[i].first.second;
      if (act[i].second == 0 and act[i+1].second == 0) gapc.push_back(forat);
      if (act[i].second == 1 and act[i+1].second == 1) gapj.push_back(forat);
      if (act[i].second == 0 and act[i+1].second == 1) gapm.push_back(forat);
      if (act[i].second == 1 and act[i+1].second == 0) gapm.push_back(forat);
    }
    int llarg = act[0].first.first + 1440 - act[nact-1].first.second; 
    if (act[0].second == 0 and act[nact-1].second == 0) gapc.push_back(llarg);
    if (act[0].second == 1 and act[nact-1].second == 1) gapj.push_back(llarg);
    if (act[0].second == 0 and act[nact-1].second == 1) gapm.push_back(llarg);
    if (act[0].second == 1 and act[nact-1].second == 0) gapm.push_back(llarg);
   
    
    for (auto x: gapc) tc += x;
    for (auto x: gapj) tj += x;
    for (auto x: gapm) tm += x;
    

    
    if (tc > tj) {
      swap(tc, tj);
      swap(gapc, gapj);
    }
    sort(gapj.rbegin(), gapj.rend());
    
    int cnt = gapm.size();
    int i = 0;
    while (tc + tm < 720) {
      cnt += 2;
      tc += gapj[i];
      i++;
    }
    
    cout << "Case #" << t << ": " << cnt << "\n";
  }
  return 0;
}
