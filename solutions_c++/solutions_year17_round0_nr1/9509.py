#include <bits/stdc++.h>

using namespace std;

using ll = long long;
using ull = unsigned long long;
using ld = long double;

using pll = pair<ll, ll>;
using vll = vector<ll>;
using vpll = vector<pll>;

#define pb push_back
#define FOR(i, m, n) for (ll i(m); i < n; i++)
#define REP(i, n) FOR(i, 0, n)
#define F(n) REP(i, n)
#define FF(n) REP(j, n)
#define D(x) cerr << __LINE__ << ": " << #x << " : " << x << endl
#define EPS (1e-10)
#define INF (1LL<<61)
#define CL(A,I) (memset(A,I,sizeof(A)))
#define all(x) begin(x),end(x)
#define IN(n) ll n;cin >> n;
#define x first
#define y second
void ga(ll N,int *A){F(N)cin>>A[i];}

int main(void) {
  ios_base::sync_with_stdio(false);
  IN(_);
  REP(__, _)
  {
      string S;
      cin >> S;
      IN(K);
      ll L = S.size();
      ll C = 0;
      F(L-K+1)
      {
        if (S[i] != '+')
        {
            ++C;
            FF(K)
                S[i+j] = S[i+j] == '+' ? '-' : '+';
        }
      }
      cout << "Case #" << __+1 << ": ";
      bool ok = true;
      F(L) if (S[i] != '+') {ok=false;break;}
      if (ok) cout << C; else cout << "IMPOSSIBLE"; cout << endl;
  }
  return 0;
}
