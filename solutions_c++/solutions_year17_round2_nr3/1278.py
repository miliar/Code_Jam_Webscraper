#include <iostream>
#include <cstdio>
#include <vector>
#include <utility>
#include <algorithm>
using namespace std;

int N, Q;
int E[100]; // total dist
int S[100]; // speed

int dist[100][100];
int U[100];
int V[100];

double ans[100];

void solve()
{
    fill(ans, ans + 100, 1e13);
    ans[0] = 0;

    for (int i = 0; i < N; i++) {
        int d = 0;
        for (int j = i + 1; j < N; j++) {
            d += dist[j-1][j];
            if (E[i] < d) {
                break;
            }
            ans[j] = min(ans[j], ans[i] + (double)d / S[i]);
        }
    }
    printf("%.7f", ans[N-1]);
}

int main()
{
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        cin >> N >> Q;
        for (int j = 0; j < N; j++) {
            cin >> E[j] >> S[j];
        }
        for (int j = 0; j < N; j++) {
            for (int k = 0; k < N; k++) {
                cin >> dist[j][k];
            }
        }
        for (int j = 0; j < Q; j++) {
            cin >> U[j] >> V[j];
        }

        cout << "Case #" << i + 1 << ": ";
        solve();
        cout << endl;
    }
}
