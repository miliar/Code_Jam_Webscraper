#include <bits/stdc++.h>

using namespace std;

const double inf = 1e20;
const int MAXN = 110;

int n, q;
vector<int> e, s;

long long D[MAXN][MAXN];
double A[MAXN][MAXN];

void solve(int test_num)
{
    cin >> n >> q;
    e.resize(n);
    s.resize(n);
    for (int i= 0; i < n; i++) {
        cin >> e[i] >> s[i];
    }

    memset(D, -1, sizeof(D));
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> D[i][j];
        }
    }

    for (int k = 0; k < n; k++) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (D[i][k] != -1 and D[k][j] != -1 and (D[i][j] == -1 or D[i][j] > D[i][k] + D[k][j])) {
                    D[i][j] = D[i][k] + D[k][j];
                }
            }
        }
    }

//     cerr << endl;
//     for (int i = 0; i <  n; i++) {
//         for (int j = 0; j <n ;j++) {
//             cerr << D[i][j] << ' ';
//         }
//         cerr << endl;
//     }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            A[i][j] = inf;
        }
        A[i][i] = 0;
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (D[i][j] != -1 and D[i][j] <= e[i]) {
                A[i][j] = D[i][j] * 1.0 / s[i];
            }
        }
    }

    for (int k = 0; k < n; k++) {
        for (int i = 0; i < n; i++) {
            for (int j  = 0; j < n; j++) {
                if (A[i][k] != inf and A[k][j] != inf and (A[i][j] == inf or A[i][j] > A[i][k] + A[k][j])) {
                    A[i][j] = A[i][k] + A[k][j];
                }
            }
        }
    }

//     cerr << endl;
//     for (int i = 0; i <  n; i++) {
//         for (int j = 0; j <n ;j++) {
//             cerr << A[i][j] << ' ';
//         }
//         cerr << endl;
//     }


    for (int i = 0; i < q; i++) {
        int a, b;
        cin >> a >> b;
        a--, b--;

        cout << " " << A[a][b];
    }
    cout << "\n";
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.precision(15);
    cout.setf(ios::fixed);

    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        cout << "Case #" << i + 1 << ":";
        solve(i);
    }
}
