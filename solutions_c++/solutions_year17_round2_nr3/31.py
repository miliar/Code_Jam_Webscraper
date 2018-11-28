#include <cstdio>

int N, Q;

long long horse_E[103];
long long horse_S[103];

long long dist[103][103];

void floyd() {
    for (int k = 1; k <= N; k ++) {
        for (int i = 1; i <= N; i ++) {
            for (int j = 1; j <= N; j ++) {
                if (dist[i][k] == -1 || dist[k][j] == -1) {
                    continue;
                }

                if (dist[i][j] == -1 || dist[i][j] > dist[i][k] + dist[k][j]) {
                    dist[i][j] = dist[i][k] + dist[k][j];
                }
            }
        }
    }
}

bool V[103];
double D[103];

double process(int st, int en) {
    for (int i = 1; i <= N; i ++) {
        V[i] = false;
        D[i] = -1;
    }

    D[st] = 0;

    for (int i = 1; i <= N; i ++) {
        int k = 0;
        double min = -1;

        for (int j = 1; j <= N; j++) {
            if (V[j]) {
                continue;
            }
            if (D[j] > -1e-8 && (min < -1e-8 || min > D[j])) {
                min = D[j];
                k = j;
            }
        }

        if (k == 0) {
            break;
        }
        V[k] = true;

        for (int j = 1; j <= N; j ++) {
            if (dist[k][j] == -1 || dist[k][j] > horse_E[k] || V[j]) {
                continue;
            }

            double tmp = dist[k][j] / (double) horse_S[k];
            if (D[j] < -1e-8 || D[j] > tmp + min) {
                D[j] = tmp + min;
            }
        }
    }

    return D[en];
}

int main() {
    int T;
    scanf("%d", &T);

    for (int test = 1; test <= T; test ++) {
        scanf("%d %d", &N, &Q);
        for (int i = 1; i <= N; i ++) {
            scanf("%lld %lld", &horse_E[i], &horse_S[i]);
        }

        for (int i = 1; i <= N; i ++) {
            for (int j = 1; j <= N; j ++) {
                scanf("%lld", &dist[i][j]);
            }
        }
        
        floyd();

        printf("Case #%d:", test);

        for (int i = 1; i <= Q; i ++) {
            int st, en;
            scanf("%d %d", &st, &en);
            printf(" %.10lf", process(st, en));
        }
        printf("\n");
    }
    return 0;
}
