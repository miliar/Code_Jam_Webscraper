#include<bits/stdc++.h>
using namespace std; 
typedef long long ll;
typedef double D;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef vector<vii> vvii;
#define MP make_pair 
#define A first 
#define B second 
#define PB push_back 
#define FR(i, a, b) for(int i=(a); i<(b); i++) 
#define FOR(i, n) FR(i, 0, n) 
#define RF(i, a, b) for(int i=(b)-1; i>=(a); i--) 
#define ROF(i, n) RF(i, 0, n) 
#define EACH(it,X) for(__typeof((X).begin()) it=(X).begin(); it!=(X).end(); ++it) 

int main() {
  ios::sync_with_stdio(0);
  int T;
  cin >> T;
  for (int tt = 1; tt <= T; tt++) {
    cout << "Case #" << tt << ": ";
    int N, P;
    cin >> N >> P;
    vi G(N);
    map<int, int> m;
    for (int i = 0; i < N; i++) {
      cin >> G[i];
      G[i] %= P;
      m[G[i]]++;
    }
    for (int i = 0; i < P; i++) {
      //cout << i << ": " << m[i] << endl;
    }
    int ans = m[0];

    if (P == 2) {
      ans += (m[1] + 1)/2;
    }
    else if (P == 3) {
      // try 1,2,1,2,...
      map<int, int> m12 = m;
      int ans1 = 0;
      int cur_mod = 0;
      while (m12[1] > 0 || m12[2] > 0) {
        if (cur_mod == 0) {
          ans1++;
          if (m12[1] > 0) {
            cur_mod = 1;
            m12[1]--;
          } else {
            cur_mod = 2;
            m12[2]--;
          }
        } else if (cur_mod == 1) {
          if (m12[2] > 0) {
            cur_mod = 0;
            m12[2]--;
          } else {
            cur_mod = 2;
            m12[1]--;
          } 
        } else if (cur_mod == 2) {
          if (m12[1] > 0) {
            cur_mod = 0;
            m12[1]--;
          } else {
            cur_mod = 1;
            m12[2]--;
          } 
        }
      }
      //cout << "ans1: " << ans1 << endl;

      // try 2,1,2,1,...
      map<int, int> m21 = m;
      int ans2 = 0;
      cur_mod = 0;
      while (m21[1] > 0 || m21[2] > 0) {
        if (cur_mod == 0) {
          ans2++;
          if (m21[2] > 0) {
            cur_mod = 2;
            m21[2]--;
          } else {
            cur_mod = 1;
            m21[1]--;
          }
        } else if (cur_mod == 1) {
          if (m21[2] > 0) {
            cur_mod = 0;
            m21[2]--;
          } else {
            cur_mod = 2;
            m21[1]--;
          } 
        } else if (cur_mod == 2) {
          if (m21[1] > 0) {
            cur_mod = 0;
            m21[1]--;
          } else {
            cur_mod = 1;
            m21[2]--;
          } 
        }
      }
      //cout << "ans2: " << ans2 << endl;

      //cout << ans << " " << ans1 << " " << ans2 << endl;
      ans += max(ans1, ans2);
    }
    cout << ans;
    cout << endl;
  }
  return 0;
}

