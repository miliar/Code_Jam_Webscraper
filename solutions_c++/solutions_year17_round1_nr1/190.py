#include <bits/stdc++.h>
using namespace std;

#define all(x) (x).begin(), (x).end()

#define TRACE(x) x
#define WATCH(x) TRACE(cout << #x" = " << x << endl)
#define WATCHR(a, b) TRACE(for (auto it=a; it!=b;) cout << *(it++) << " "; cout << endl)
#define WATCHC(V) TRACE({cout << #V" = "; WATCHR(V.begin(), V.end());})

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<ll> vll;
typedef vector<vll> vvll;

void solve() {
    int R, C;
    cin >> R >> C;

    vector<char> first(R, '?');
    vector<string> cake(R);

    for (int r = 0; r < R; r++) {
        cin >> cake[r];
        for (int c = 0; c < C; c++)
            if (cake[r][c] != '?') {
                first[r] = cake[r][c];
                break;
            }
    }

    int r0 = 0;
    while (first[r0] == '?') r0++;

    for (int r = r0; r < R; r++) {
        if (first[r] == '?') {
            cake[r] = cake[r-1];
            continue;
        }

        char lst = first[r];
        for (int c = 0; c < C; c++) {
            if (cake[r][c] == '?') cake[r][c] = lst;
            else lst = cake[r][c];
        }
    }

    for (int r = 0; r < r0; r++)
        cake[r] = cake[r0];

    cout << "\n";
    for (string &row : cake)
        cout << row << "\n";
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0), cout.tie(0);
    cout << fixed << setprecision(15);

    int T;
    cin >> T;

    for (int t = 1; t <= T; t++) {
        cout << "Case #" << t << ": ";
        solve();
    }

    return 0;
}

