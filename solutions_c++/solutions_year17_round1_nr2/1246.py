#include <bits/stdc++.h>

#define PI 3.14159265358979323846
#define EPS 1e-6
#define INF 1000000000

#define _ ios_base::sync_with_stdio(0), cin.tie(0), cin.tie(0), cout.tie(0), cout.precision(15);
#define FOR(i, a, b) for(int i=int(a); i<int(b); i++)
#define RFOR(i, a, b) for(int i=int(a)-1; i>=int(b); i--)
#define FORC(cont, it) for(decltype((cont).begin()) it = (cont).begin(); it != (cont).end(); it++)
#define RFORC(cont, it) for(decltype((cont).rbegin()) it = (cont).rbegin(); it != (cont).rend(); it++)
#define pb push_back

using namespace std;

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<int> vi;

#define MAXN 55
#define MOD 1000000007

int need[MAXN];
int packs[MAXN][MAXN];
bool mat[MAXN][MAXN];

int n, p;
queue<ii> q;

bool range(int a, int b, int c) {
    // cout << a << " " << b << " " << c << endl;
    return a <= b && b <= c;
}

bool ayuda(int act) {
    while(! q.empty()) q.pop();
    bool b = true;
    FOR(j, 0, n) {
        b = false;
        FOR(k, 0, p) {
            if (mat[j][k] && range(need[j] * act * 0.9, packs[j][k], need[j] * act * 1.1)) {
                q.push(ii(j, k));
                b = true;
                break;
            }
        }
        if (!b) break;
    }

    return b;
}

int solve() {
    int ret = 0;
    memset(mat, 1, sizeof(mat));
    FOR(i, 0, p) {
        int act = packs[0][i] / need[0];
        FOR(ff, (int)(act*0.9-1000), (int)(act*1.1)+1000) {
            // cout << ff << endl;
            bool b = ayuda(ff);
            if (b) {
                FOR(i, 0, n) {
                    ii f = q.front();
                    q.pop();
                    mat[f.first][f.second] = false;
                }
                ret ++;
                continue;
            }
        }
    }

    return ret;
}

int main() { _
    int T;

    /**/
    freopen("b.in", "r", stdin);
    freopen("b.out", "w", stdout);
    /**/

    cin >> T;
    FOR (t, 1, T + 1) {
        cin >> n >> p;

        FOR(i, 0, n)    cin >> need[i];

        FOR(i, 0, n) {
            FOR(j, 0, p) {
                cin >> packs[i][j];
            }
            sort(packs[i], packs[i] + p);
        }

        cout << "Case #" << t << ": " << solve() << endl;
    }



    return 0;
}

