#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <thread>
using namespace std;

const int N = 1440;
const int H = N / 2;

int dp[2][N][2];

const int INF = 1e9;
void init(int cur) {
    for (int i = 0; i < N; ++i)
        for (int j = 0; j < 2; ++j)
            dp[cur][i][j] = INF;
}

int solve(const vector<int> &vec, int s) {
    for (int i = 0; i < 2; ++i)
        init(i);

    int cur = 0, pre = 1;
    dp[cur][H][s] = 0;

    for (int last = N; last > 0; --last) {
        cur ^= 1, pre ^= 1;
        init(cur);

        for (int x = min(last, H); x >= 0 && last - x <= H; --x) {
            int y = last - x;

            int t = N - last;
            if (vec[t] == -1 || vec[t] == 0) {
                if (x-1 >= 0)
                    for (int i = 0; i < 2; ++i) {
                        dp[cur][x-1][0] = min(dp[cur][x-1][0], dp[pre][x][i] + (i != 0));
                    }
            }

            if (vec[t] == -1 || vec[t] == 1) {
                if (y-1 >= 0)
                    for (int i = 0; i < 2; ++i)
                        dp[cur][x][1] = min(dp[cur][x][1], dp[pre][x][i] + (i != 1));
            }
        }
    }
    int x = dp[cur][0][0] + (0 != s), y = dp[cur][0][1] + (1 != s);
    return min(x, y);
}



int main() {

    freopen("in", "r", stdin);
    freopen("out", "w", stdout);
    int casnum;
    cin >> casnum;
    for (int casid = 1; casid <= casnum; ++casid) {
        int n, m;
        cin >> n >> m;
        vector<int> vec(N, -1);
        for (int i = 0; i < n + m; ++i) {
            int x, y;
            cin >> x >> y;
            for (int j = x; j < y; ++j)
                vec[j] = (i < n);
        }

        int res = min(solve(vec, 0), solve(vec, 1));
        printf("Case #%d: %d\n", casid, res);
    }
    return 0;
}

