#include<stdio.h>
#include<string.h>
#include<math.h>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

int hourses[1001][2];
int D, N;

float solve() {
    bool first = true;
    float max_time = D * 10;
    for(int i = N - 1; i >= 0; --i) {
        float htime = (float)(D-hourses[i][0]) / (float)hourses [i][1];
        if (first)
            max_time = htime;
        else
            max_time = std::max(max_time, htime);
        first = false;
    }
    return (float)D / max_time;
}

int main() {
    int T;
    freopen("output.txt", "w", stdout);
    freopen("input.txt", "r", stdin);
    scanf("%d", &T);
    for(int i = 0; i < T;++i) {
        scanf("%d %d", &D, &N);
        for(int i = 0; i < N; ++i) {
            scanf("%d %d", &hourses[i][0], &hourses[i][1]);
        }
        printf("Case #%d: %.6f\n", i+1, solve());
    }

    return 0;
}
