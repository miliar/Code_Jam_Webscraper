#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
template<typename T> using Graph = vector<vector<T>>;

#define REP(i, a, b) for (int i = (int)(a); i < (int)(b); i++)
#define rep(i, a) REP(i, 0, a)
#define EACH(i, a) for (auto i: a)
#define ITR(x, a) for (__typeof(a.begin()) x = a.begin(); x != a.end(); x++)
#define ALL(a) (a.begin()), (a.end())
#define HAS(a, x) (a.find(x) != a.end())
#define endl '\n'

const ll inf = (ll)1e14;
int T;
int N, Q;
ll G[105][105], D[105][105];
ll E[105], S[105];
double C[105][105];

void printc() {
    rep(i, N) {
        rep(j, N) cout << C[i][j] << " ";
        cout << endl;
    }
}

void solve(int loop) {
    cin >> N >> Q;
    rep(i, N) cin >> E[i] >> S[i];
    rep(i, N) {
        rep(j, N) {
            int d;
            cin >> d;
            G[i][j] = d > 0 ? d:inf;
        }
    }

    rep(i, N) rep(j, N) D[i][j] = G[i][j];
    rep(k, N) rep(i, N) rep(j, N) D[i][j] = min(D[i][j], D[i][k] + D[k][j]);
    rep(i, N) rep(j, N) C[i][j] = i == j ? 0:inf;
    rep(i, N) rep(j, N) if (D[i][j] <= E[i]) C[i][j] = min(C[i][j], 1.0*D[i][j]/S[i]);
    rep(k, N) rep(i, N) rep(j, N) C[i][j] = min(C[i][j], C[i][k] + C[k][j]);
        
    vector<double> ans;
    rep(loop2, Q) {
        int U, V;
        cin >> U >> V;
        U--; V--;
        ans.push_back(C[U][V]);
    }


    printf("Case #%d:", loop);
    for (auto a: ans) printf(" %.10f", a);
    printf("\n");
}

int main(void) {
  cin.tie(0);
  ios::sync_with_stdio(false);

  cin >> T;
  REP(loop, 1, T + 1) solve(loop);

  return 0;
}
