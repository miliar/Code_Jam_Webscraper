#include <iostream>
#include <memory.h>
#include <algorithm>

using namespace std;

const int maxN = 1010;
const double pi = 3.14159265358979323846264338327;

struct Pancake {
    double r, h, round, side;
}pancakes[maxN];

bool myCmp(const Pancake&a, const Pancake&b) {
    return a.r > b.r;
}

int main() {
    int t;
    cin >> t;
    int K, N;
    double dp[maxN][maxN];

    for(int i = 0; i < t; i ++) {
        cin >> N >> K;
        for(int j = 0; j < N; j ++) {
            cin >> pancakes[j].r >> pancakes[j].h;
            pancakes[j].round = pi * pancakes[j].r * pancakes[j].r;
            pancakes[j].side = 2 * pi * pancakes[j].r * pancakes[j].h;
        }

        sort(pancakes, pancakes + N, myCmp);

        memset(dp, 0, sizeof(dp));
        for(int j = 0; j < N; j ++) {
            dp[j][0] = 0;
            dp[j][1] = pancakes[j].round + pancakes[j].side;
        }

        for(int j = 1; j < N; j ++) {
            for(int k = 2; k <= K; k ++) {
                for(int l = 0; l < j; l ++) {
                    if(dp[l][k - 1] == -1)
                        continue;
                    if(dp[j][k] < dp[l][k - 1] + pancakes[j].side)
                        dp[j][k] = dp[l][k - 1] + pancakes[j].side;
                }
            }
        }

        printf("Case #%d: ", i + 1);
        double res = 0;
        for(int j = 0; j < N; j ++) {
            if(res < dp[j][K])
                res = dp[j][K];
        }
        printf("%.9lf\n", res);
    }
    return 0;
}

