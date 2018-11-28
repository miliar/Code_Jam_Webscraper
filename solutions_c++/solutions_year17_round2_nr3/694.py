#include <iostream>
#include <stdio.h>
using namespace std;


const int N = 111;
int n, q;
long long E[N];
double S[N];
long long D[N][N];

double dist[N];
bool visit[N];

void floyd() {
    for (int k = 0; k < n; k++)
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                if (D[i][k] != -1 && D[k][j] != -1)
                    if (D[i][j] == -1 || D[i][j] > D[i][k] + D[k][j])
                        D[i][j] = D[i][k] + D[k][j];
}

double solve(int s, int t) {
    for (int i = 0; i < n; i++) dist[i] = 1e30;
    memset(visit, 0, sizeof(visit));
    dist[s] = 0;
    while (true) {
        int u = -1;
        for (int i = 0; i < n; i++) {
            if (dist[i] >= 1e30) continue;
            if (!visit[i] && (u == -1 || dist[i] < dist[u]))
                u = i;
        }
        if (u == -1)
            break;
        visit[u] = true;
        for (int v = 0; v < n; v++) {
            if (visit[v]) continue;
            if (D[u][v] != -1 && D[u][v] <= E[u]) {
                dist[v] = min(dist[v], dist[u] + D[u][v] / S[u]);
            }
        }
    }
    return dist[t];
}

int main() {
    int T, Case = 1;
    cin >> T;
    while (T--) {
        cin >> n >> q;
        for (int i = 0; i < n; i++) cin >> E[i] >> S[i];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++)
                cin >> D[i][j];
            D[i][i] = 0;
        }
        floyd();

        /*
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++)
                cout << D[i][j] << " ";
            cout << endl;
        }
        */

        printf("Case #%d:", Case++);
        for (int i = 0; i < q; i++) {
            int s, t;
            cin >> s >> t;
            s--, t--;
            double ans = solve(s, t);
            printf(" %.10f", ans);
        }
        printf("\n");
    }
    return 0;
}
