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

#define MAXN 30
#define MOD 1000000007

int r, c;
char mat[MAXN][MAXN];
bool mat2[MAXN][MAXN];
void print() {
    FOR(i, 0, r) {
        FOR(j, 0, c) {
            cout << mat[i][j];
        }
        cout << endl;
    }
}

void llena(int i1, int j1, int i2, int j2, char c) {
    FOR(i, i1, i2+1) {
        FOR(j, j1, j2+1) {
            mat[i][j] = c;
            mat2[i][j] = false;
        }
    }
}




void solve() {
    memset(mat2, 1, sizeof(mat2));
    FOR(i, 0, r) {
        FOR(j, 0, c) {
            if (mat[i][j] != '?' && mat2[i][j]) {
                int i1 = i, j1 = j, i2 = i, j2 = j;
                for(j1 = j1 - 1; j1 >= 0 && mat[i1][j1] == '?'; j1 --);
                j1 ++;

                bool b=true;
                for(i1 = i-1; i1 >= 0 && b; i1 --) {
                    for(int k = j; k >= j1 && b; k --) {
                        b = mat[i1][k] == '?';
                        if (!b) i1 ++;
                    }
                }
                i1 ++;

                b = true;
                for(j2 = j+1; j2 < c && b; j2 ++) {
                    for(i2 = i1; i2 <= i && b; i2 ++) {
                        b = mat[i2][j2] == '?';
                        if (!b) j2 --;
                    }
                }
                j2 --;

                b = true;
                for(i2=i+1; i2 < r && b; i2 ++) {
                    for(int k = j1; k <= j2 && b; k ++) {
                        b = mat[i2][k] == '?';
                        if (!b) i2 --;
                    }
                }
                i2 --;

                //cout << i1 << " " << j1 << " " << i2 << " " << j2 << endl;
                llena(i1, j1, i2, j2, mat[i][j]);
            }
        }
    }
}

int main() { _
    int T;

    /**/
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    /**/

    cin >> T;
    FOR (t, 1, T + 1) {
        cin >> r >> c;

        FOR(i, 0, r)    FOR(j, 0, c) {
            cin >> mat[i][j];
        }

        solve();
        cout << "Case #" << t << ":" << endl;
        print();

    }



    return 0;
}
