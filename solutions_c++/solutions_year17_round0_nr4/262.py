#include <iostream>
#include <string>
#include <cassert>
#include <set>
#include <vector>
#include <queue>

using namespace std;
typedef long long ll;

// Two separate problems!

int main() {
  ll T;
  cin >> T;
  for(ll cas=1; cas<=T; cas++) {
    ll n, m;
    cin >> n >> m;
    vector<vector<char>> G(n, vector<char>(n, '.'));
    for(ll i=0; i<m; i++) {
      char ch;
      ll r, c;
      cin >> ch >> r >> c;
      r--;
      c--;
      G[r][c] = ch;
    }
    vector<vector<int>> P(n, vector<int>(n, false));
    vector<int> UR(n, false);
    vector<int> UC(n, false);
    vector<vector<int>> X(n, vector<int>(n, false));
    set<ll> D1;
    set<ll> D2;
    for(ll r=0; r<n; r++) {
      for(ll c=0; c<n; c++) {
        if(G[r][c] == 'x' || G[r][c] == 'o') {
          X[r][c] = true;
          UR[r] = true;
          UC[c] = true;
        }
        if(G[r][c] == '+' || G[r][c]=='o') {
          P[r][c] = true;
          D1.insert(r+c);
          D2.insert(r-c);
        }
      }
    }
    for(ll r=0; r<n; r++) {
      for(ll c=0; c<n; c++) {
        if(!UR[r] && !UC[c]) {
          X[r][c] = true;
          UR[r] = true;
          UC[c] = true;
        }
      }
    }
    priority_queue<tuple<ll,ll,ll>> Q;
    for(ll r=0; r<n; r++) {
      for(ll c=0; c<n; c++) {
        ll d = min(r, n-1-r) + min(c, n-1-c);
        Q.push(make_tuple(-d, r, c));
      }
    }
    while(!Q.empty()) {
      ll d, r, c;
      std::tie(d, r, c) = Q.top();
      Q.pop();
      if(D1.count(r+c)==0 && D2.count(r-c)==0) {
        P[r][c] = true;
        D1.insert(r+c);
        D2.insert(r-c);
      }
    }

    vector<vector<char>> G2(n, vector<char>(n, '.'));
    for(ll r=0; r<n; r++) {
      for(ll c=0; c<n; c++) {
        if(P[r][c] && X[r][c]) {
          G2[r][c] = 'o';
        } else if(P[r][c]) {
          G2[r][c] = '+';
        } else if(X[r][c]) {
          G2[r][c] = 'x';
        } else {
          G2[r][c] = '.';
        }
      }
    }

    ll score = 0;
    ll ans = 0;
    for(ll r=0; r<n; r++) {
      for(ll c=0; c<n; c++) {
        if(G2[r][c] == 'o') {
          score += 2;
        } else if(G2[r][c] == 'x') {
          score++;
        } else if(G2[r][c] == '+') {
          score++;
        }
        if(G2[r][c] != G[r][c]) {
          ans++;
        }
      }
    }
    cout << "Case #" << cas << ": " << score << " " << ans << endl;
    for(ll r=0; r<n; r++) {
      for(ll c=0; c<n; c++) {
        if(G2[r][c] != G[r][c]) {
          cout << G2[r][c] << " " << r+1 << " " << c+1 << endl;
        }
      }
    }
    /*
    assert(score == (n==1 ? 2 : 3*n-2));
    for(ll r=0; r<n; r++) {
      for(ll c=0; c<n; c++) {
        cout << G[r][c];
      }
      cout << endl;
    }
    for(ll r=0; r<n; r++) {
      for(ll c=0; c<n; c++) {
        cout << G2[r][c];
      }
      cout << endl;
    }
    cout << score << " " << (3*n-2) << endl;
    if(cas==3) { break; }
    */
  }
}
