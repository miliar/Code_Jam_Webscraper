#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <vector>
#include <string>
#include <unordered_map>
#include <unordered_set>
#include <map>
#include <set>
#include <queue>
#include <cassert>

using namespace std;

int horses[100][2];
int dist[100][100];
int N;

int dp[100][100][100];

double solve(int u, int v)
{
    --u;
    --v;

    uint64_t sumDist[100];
    memset(sumDist, 0, sizeof(sumDist));
    for (int i = N - 2; i >= 0; --i) {
        sumDist[i] = sumDist[i + 1] + dist[i][i + 1];
    }

    double timeFrom[100];
    timeFrom[N - 1] = 0.0;
    for (int i = N - 2; i >= 0; --i) {
        if (sumDist[i] <= horses[i][0]) {
            timeFrom[i] = (double)sumDist[i] / (double)horses[i][1];
        } else {
            timeFrom[i] = 1e100;
        }

        for (int j = i + 1; j < N - 1; ++j) {
            // Try using j as a stop point.
            uint64_t distToJ = sumDist[i] - sumDist[j];
            if (distToJ > horses[i][0])
                continue;
            
            double newTime = (double)distToJ / (double)horses[i][1] +
                             timeFrom[j];
            if (newTime < timeFrom[i]) timeFrom[i] = newTime;
        }
    }

    assert(u == 0);

    return timeFrom[u];
}


void solve()
{
    int qns;

    scanf("%d%d", &N, &qns);
    for (int i = 0; i < N; ++i) {
        scanf("%d%d", &horses[i][0], &horses[i][1]);
    }
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            scanf("%d", &dist[i][j]);
        }
    }

    for (int i = 0; i < qns; ++i) {
        int u, v;
        scanf("%d%d", &u, &v);

        printf(" %.6f", solve(u, v));
    }

    printf("\n");
}

int main(void)
{
    int nC;
    scanf("%d", &nC);
    for (int cC = 0; cC < nC; ++cC) {
        printf("Case #%d:", cC + 1);
        solve();
    }

    return 0;
}