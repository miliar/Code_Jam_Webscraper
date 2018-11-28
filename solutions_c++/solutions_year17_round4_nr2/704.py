#include<bits/stdc++.h>
using namespace std; 
typedef long long ll;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef vector<vii> vvii;
#define MP make_pair 
#define PB push_back 
#define FR(i, a, b) for(int i=(a); i<(b); i++) 
#define FOR(i, n) FR(i, 0, n) 
#define RF(i, a, b) for(int i=(b)-1; i>=(a); i--) 
#define ROF(i, n) RF(i, 0, n) 
#define EACH(it,X) for(__typeof((X).begin()) it=(X).begin(); it!=(X).end(); ++it) 

typedef vector<int> VI;
typedef vector<VI> VVI;

bool FindMatch(int i, const VVI &w, VI &mr, VI &mc, VI &seen) {
  for (int j = 0; j < w[i].size(); j++) {
    if (w[i][j] && !seen[j]) {
      seen[j] = true;
      if (mc[j] < 0 || FindMatch(mc[j], w, mr, mc, seen)) {
        mr[i] = j;
        mc[j] = i;
        return true;
      }
    }
  }
  return false;
}

int BipartiteMatching(const VVI &w, VI &mr, VI &mc) {
  mr = VI(w.size(), -1);
  mc = VI(w[0].size(), -1);
  
  int ct = 0;
  for (int i = 0; i < w.size(); i++) {
    VI seen(w[0].size());
    if (FindMatch(i, w, mr, mc, seen)) ct++;
  }
  return ct;
}

int main() {
  ios::sync_with_stdio(0);
  int T;
  cin >> T;
  for (int tt = 1; tt <= T; tt++) {
    int N, C, M, p, b;
    cin >> N >> C >> M;
    VVI pos(C);
    for (int i = 0; i < M; i++) {
      cin >> p >> b;
      b--;
      //cout << p << " " << b << endl;
      pos[b].push_back(p);
      //cout << " push_back: " << b << " " << p << endl;
    }

    if (pos[0].size() == 0) {
      int ans = pos[1].size();
      cout << "Case #" << tt << ": " << ans << " " << 0 << endl;
      continue;
    }
    if (pos[1].size() == 0) {
      int ans = pos[0].size();
      cout << "Case #" << tt << ": " << ans << " " << 0 << endl;
      continue;
    }

    /*
    map<ii, int> m;
    map<int, ii> rev_m;
    int idx = 0;
    for (int i = 0; i < pos[1].size(); i++) {
      m[MP(1, i)] = idx;
      rev_m[idx] = MP(1, i);
      idx++;
    }
    */

    //cout << "here: " << pos[0].size() << " " << pos[1].size() << endl;
    VVI w(pos[0].size(), VI(pos[1].size()));
    for (int i = 0; i < pos[0].size(); i++) {
      for (int j = 0; j < pos[1].size(); j++) {
        //cout << " " << i << " " << j << ": " << pos[0][i] << " " << pos[1][j] << endl;
        if (pos[0][i] != pos[1][j]) {
          w[i][j] = 1;
        }
      }
    }

    VI b1, b2;
    BipartiteMatching(w, b1, b2);
    VI remaining1, remaining2;
    int ans = 0;
    int upgrades = 0;
    bool has_remaining = false;
    for (int i = 0; i < b1.size(); i++) {
      if (b1[i] == -1) {
        remaining1.push_back(pos[0][i]);
        //cout << "remaining 1: " << pos[0][i] << endl;
        has_remaining = true;
      } else {
        ans++;
      }
    }
    for (int i = 0; i < b2.size(); i++) {
      if (b2[i] == -1) {
        remaining2.push_back(pos[1][i]);
        //cout << "remaining 2: " << pos[1][i] << endl;
        has_remaining = true;
      }
    }

    if (has_remaining) {
      int remaining_seat = -1;
      if (remaining1.size() > 0) remaining_seat = remaining1[0];
      if (remaining2.size() > 0) remaining_seat = remaining2[0];
      if (remaining_seat == 1) {
        ans += remaining1.size();
        ans += remaining2.size();
      } else {
        int minner = min(remaining1.size(), remaining2.size());
        upgrades += minner;
        ans += remaining1.size() + remaining2.size() - minner;
      }
    }

    cout << "Case #" << tt << ": " << ans << " " << upgrades << endl;
  }
  return 0;
}

