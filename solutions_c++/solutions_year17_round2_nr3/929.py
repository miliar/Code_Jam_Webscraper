#include <cstdio>
#include <iostream>
#include <iomanip>

using namespace std;

#define NMAX 1000
#define INF 10000000000000000LL

long long D[NMAX][NMAX];
double V[NMAX][NMAX];

// 0 - distance, 1 - speed
long long H[NMAX][2];

int N, Q;

void RoyFloyd1()
{
    for (int k = 0; k < N; k++) {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (D[i][j] > D[i][k] + D[k][j]) {
                    D[i][j] = D[i][k] + D[k][j];
                }
            }
        }
    }
}

void RoyFloyd2()
{
    for (int k = 0; k < N; k++) {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (V[i][j] > V[i][k] + V[k][j]) {
                    V[i][j] = V[i][k] + V[k][j];
                }
            }
        }
    }
}

void solve(int t)
{
    cin >> N >> Q;

    for (int i = 0; i < N; i++) {
        cin >> H[i][0] >> H[i][1];
    }

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cin >> D[i][j];
            if (D[i][j] == -1) {
                D[i][j] = INF;
            }
        }
    }

    RoyFloyd1();
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (D[i][j] <= H[i][0]) {
                V[i][j] = 1.0 * D[i][j] / H[i][1];
            } else {
                V[i][j] = INF;
            }
        }
    }

    RoyFloyd2();

    cout << "Case #" << t << ": " << setprecision(10) << fixed;
    for (int i = 0; i < Q; i++) {
        int x, y;
        cin >> x >> y;
        cout << V[x - 1][y - 1];
        if (i < Q - 1) {
            cout << " ";
        }
    }
    cout << endl;
}

int main()
{
    freopen("ponyexpress.in", "r", stdin);
    freopen("ponyexpress.out", "w", stdout);

    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        solve(i + 1);
    }
}
