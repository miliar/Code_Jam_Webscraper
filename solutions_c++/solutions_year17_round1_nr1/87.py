#include <iostream>
#include <vector>
#include <set>
#include <map>

using namespace std;
typedef long long ll;
typedef pair<ll, ll> pll;
typedef vector<vector<char>> grid;

void f(grid& G, grid& G2, ll r1, ll r2, ll c1, ll c2) {
  vector<pll> P;
  for(ll r=r1; r<=r2; r++) {
    for(ll c=c1; c<=c2; c++) {
      if(G[r][c]!='?') {
        P.push_back(make_pair(r, c));
      }
    }
  }
  if(P.size() == 1) {
    ll r,c;
    std::tie(r,c) = P[0];
    char ch = G[r][c];
    for(ll r=r1; r<=r2; r++) {
      for(ll c=c1; c<=c2; c++) {
        G2[r][c] = ch;
      }
    }
  } else {
    ll ar, ac, br, bc;
    std::tie(ar, ac) = P[0];
    std::tie(br, bc) = P[1];
    if(ar!=br) {
      f(G, G2, r1, min(ar,br), c1, c2);
      f(G, G2, min(ar,br)+1, r2, c1, c2);
    } else {
      f(G, G2, r1, r2, c1, min(ac, bc));
      f(G, G2, r1, r2, min(ac,bc)+1, c2);
    }
  }
}

int main() {
  ll T;
  cin >> T;
  for(ll cas=1; cas<=T; cas++) {
    ll R, C;
    cin >> R >> C;
    vector<vector<char>> G(R, vector<char>(C, '?'));
    vector<vector<char>> G2(R, vector<char>(C, '?'));
    for(ll r=0; r<R; r++) {
      string row;
      cin >> row;
      for(ll c=0; c<C; c++) {
        G[r][c] = row[c];
      }
    }
    f(G, G2, 0, R-1, 0, C-1);
    cout << "Case #" << cas << ":" << endl;
    for(ll r=0; r<R; r++) {
      for(ll c=0; c<C; c++) {
        cout << G2[r][c];
      }
      cout << endl;
    }
  }
}
