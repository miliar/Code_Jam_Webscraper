#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using vl = vector<ll>;
using vvl = vector<vl>;
using pll = pair<ll,ll>;
using vb = vector<bool>;
const ll oo = 0x3f3f3f3f3f3f3f3fLL;
const double eps = 1e-9;
#define	sz(c) ll((c).size())
#define	all(c) begin(c),end(c)
#define	mp make_pair
#define mt make_tuple
#define	pb push_back
#define eb emplace_back
#define xx first
#define yy second
#define	has(c,i) ((c).find(i) != end(c))
#define FOR(i,a,b) for (ll i = (a); i < (b); i++)
#define	FORD(i,a,b) for (ll i = (b)-1; i >= (a); i--)

ll dp[101][101][101][4][4];

int main(){
  ios::sync_with_stdio(false);
  ll TC;
  cin >> TC;
  FOR(p,2,5){
  FOR(one, 0, 101){
    FOR(two, 0, 101){
      FOR(three, 0, 101){
        FOR(last, 0, 4){
          dp[one][two][three][last][p] = 0;
        }
      }
    }
  }
  FOR(one, 0, 101){
    FOR(two, 0, 101){
      FOR(three, 0, 101){
        FOR(last, 0, 4){
          ll cur = 0;
          if(one > 0){
            cur = max(cur, dp[one-1][two][three][(last+1)%p][p] + (last == 0));
          }
          if(two > 0){
            cur = max(cur, dp[one][two-1][three][(last+2)%p][p] + (last == 0));
          }
          if(three > 0){
            cur = max(cur, dp[one][two][three-1][(last+3)%p][p] + (last == 0));
          }
          dp[one][two][three][last][p] = cur;
        }
      }
    }
  }
  }
  FOR(tc,1,TC+1){
    ll n, p;
    cin >> n >> p;
    vl num(4, 0);
    FOR(i,0,n){
      ll g;
      cin >> g;
      num[g%p]++;
    }
    cout << "Case #" << tc << ": "; 
      cout << num[0] + dp[num[1]][num[2]][num[3]][0][p] << endl;
  }
}
