#include <bits/stdc++.h>
using namespace std;

#define TRACE(x) x
#define WATCH(x) TRACE(cout << #x" = " << x << endl)
#define WATCHR(a, b) TRACE(for (auto it=a; it!=b;) cout << *(it++) << " "; cout << endl)
#define WATCHC(V) TRACE({cout << #V" = "; WATCHR(V.begin(), V.end());})

#define all(x) (x).begin(), (x).end()

typedef long long ll;
typedef vector<bool> vb;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<ll> vll;
typedef vector<vll> vvll;

int dp[5][101][101][101][4];

const int LIM = 100;
void init() {
    for (int P = 1; P <= 4; P++) {
        for (int one = 0; one <= (P > 1 ? LIM : 0); one++) {
            for (int two = 0; two <= (P > 2 ? LIM : 0); two++) {
                for (int thr = 0; thr <= (P > 3 ? LIM : 0); thr++) {
                    for (int rem = 0; rem < P; rem++) {
                        int &v = dp[P][one][two][thr][rem];
                        if (one) {
                            v = max(v, !rem + dp[P][one-1][two][thr][(rem+1)%P]);
                        }
                        if (two) {
                            v = max(v, !rem + dp[P][one][two-1][thr][(rem+2)%P]);
                        }
                        if (thr) {
                            v = max(v, !rem + dp[P][one][two][thr-1][(rem+3)%P]);
                        }
                    }
                }
            }
        }
    }
}

int solve() {
    int N, P;
    cin >> N >> P;

    array<int, 4> g = { 0, 0, 0, 0 };
    for (int i = 0; i < N; i++) {
        int siz;
        cin >> siz;
        g[siz % P]++;
    }

    return g[0] + dp[P][g[1]][g[2]][g[3]][0];
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0), cout.tie(0);
    cout << fixed << setprecision(15);

    init();

    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        cout << "Case #" << t << ": " << solve() << endl;
    }

    return 0;
}

