#include <cstdio>
#include <vector>
#include <algorithm>
#include <string>
#include <queue>
#include <limits>


#pragma warning(disable:4996)

using namespace std;

long long map[111][111];
double times[111][111];

int main() {
    freopen("C-large.in", "r", stdin);
    freopen("test.out", "w", stdout);

    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        int N, Q;
        scanf("%d %d", &N, &Q);
        vector<int> E(N);
        vector<int> S(N);
        for (int i = 0; i < N; i++) {
            scanf("%d %d", &E[i], &S[i]);
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                int tmp;
                scanf("%d", &tmp);
                map[i][j] = (tmp == -1 ? 9999999999999 : tmp);
            }
        }

        // F-W
        for (int k = 0; k < N; k++) {
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    map[i][j] = min(map[i][j], map[i][k] + map[k][j]);
                }
            }
        }

        // fill times
        for (int i = 0; i < N; i++) {
            vector<long long> dist(N);
            for (int j = 0; j < N; j++) {
                dist[j] = -1;
            }
            dist[i] = E[i];
            priority_queue<pair<long long, long long>> Q;
            Q.push(pair<long long, long long>(E[i], i));

            while (!Q.empty()) {
                long long d = Q.top().first;
                long long v = Q.top().second;
                Q.pop();

                for (int j = 0; j < N; j++) {
                    if (dist[j] < dist[v] - map[v][j] && dist[v] - map[v][j] >= 0) {
                        dist[j] = dist[v] - map[v][j];
                        Q.push(pair<long long, long long>(dist[j], j));
                    }
                }
            }

            for (int j = 0; j < N; j++) {
                if (dist[j] == -1) {
                    times[i][j] = numeric_limits<double>::max();
                }
                else
                    times[i][j] = (double)(E[i] - dist[j]) / (double)S[i];
            }

        }

        printf("Case #%d:", t);
        for (int i = 0; i < Q; i++) {
            int from, to;
            scanf("%d %d", &from, &to);
            from--;
            to--;

            vector<double> arrival(N, numeric_limits<double>::max());
            arrival[from] = 0;

            priority_queue<pair<double, int>> QQ;
            QQ.push(pair<double, int>(0, from));

            while (!QQ.empty()) {
                double t = -QQ.top().first;
                int v = QQ.top().second;
                QQ.pop();

                for (int j = 0; j < N; j++) {
                    if (arrival[j] > arrival[v] + times[v][j]) {
                        arrival[j] = arrival[v] + times[v][j];
                        QQ.push(pair<double, int>(-arrival[j], j));
                    }
                }
            }
            printf(" %.8lf", arrival[to]);
        }
        printf("\n");

    }

    return 0;
}
