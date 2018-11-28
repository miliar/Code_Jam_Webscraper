#include <bits/stdc++.h>
#define FOR(x,n) for(int x = 0; x < n; x++)
#define ALL(a) (a).begin(), (a).end()
#define SZ(a) ((int)(a).size())
#define FIN ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0)
using namespace std;
typedef long long ll;

const int MXN = 50, MXP = 50;
int N, P;
ll R[MXN], Q[MXN][MXP];
map<ll,vector<ll> > qs[MXN] = {}, qf[MXN] = {};
set<ll> s;
int main() { FIN;
  int T; cin >> T;
  for(int cases = 1; cases <= T; cases++){
    cout << "Case #" << cases << ": ";
    cin >> N >> P;
    FOR(x,N) cin >> R[x], qs[x].clear(), qf[x].clear();
    FOR(x,N) FOR(y,P) cin >> Q[x][y];
    FOR(x,N) sort(Q[x],Q[x]+P);

    set<ll> s;
    FOR(x,N)
      FOR(y,P){
        ll tmp = 10 * Q[x][y];
        s.insert(tmp / (9LL * R[x]) + 1);
        qf[x][tmp / (9LL * R[x]) + 1].push_back(y);
        s.insert(tmp / (11LL * R[x]) + (tmp % (11LL * R[x]) != 0));
        qs[x][tmp / (11LL * R[x]) + (tmp % (11LL * R[x]) != 0)].push_back(y);
      }
    ll ans = 0;
    set<ll> a[MXN] = {};
    for(int i : s){
      for(int x = 0; x < N; x++){
        for(auto j : qs[x][i])
          a[x].insert(j);
        for(auto j : qf[x][i])
          a[x].erase(j);
      }

      bool changed = true;
      while(changed){
        changed = false;
        ll tmp = 0;
        for(int x = 0; x < N; x++)
          tmp += !a[x].empty();
        if(tmp == N){
          for(int x = 0; x < N; x++)
            a[x].erase(a[x].begin());
          ans++;
          changed = true;
        }
      }
    }
    cout << ans << "\n";
  }
}
