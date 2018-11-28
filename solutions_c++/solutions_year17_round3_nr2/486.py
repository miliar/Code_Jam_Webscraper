#include <bits/stdc++.h>

using namespace std;

const int CAMERON = 0;
const int JAMIE = 1;

const int MAXM = 1445;
const int MAXEACH = 725;
const int INF = 1e9;

int AC, AJ;

int memo[MAXM][2][MAXEACH];

// Who is occupied at a min.
array<int, MAXM> min_doing;

int other_left(int min, int left) {
    return 720 - (min - (720 - left));
}

int STARTING = 0;

int solve(int minute, int who, int left) {
    int other = other_left(minute, left);
    if (left < 0 || other < 0)
        return INF;

    // At minute, who is with the baby with left time left.
    if (memo[minute][who][left] != -1)
        return memo[minute][who][left];

    if (minute == 1440)
        return who == STARTING ? 0 : 1;

    int ans;
    if (min_doing[minute] == who) {
        int after = solve(minute + 1, 1 - who, other - 1);
        ans = 1 + after;
    } else if (min_doing[minute] == 1 - who) {
        ans = solve(minute + 1, who, left - 1);
    } else {
        ans = min(solve(minute + 1, who, left - 1), 1 + solve(minute + 1, 1 - who, other - 1));
    }

    return (memo[minute][who][left] = ans);
}

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        min_doing.fill(-1);


        cin >> AC >> AJ;
        for (int i = 0; i < AC; i++) {
            int s, e;
            cin >> s >> e;
            for (int j = s; j < e; j++)
                min_doing[j] = CAMERON;
        }
        for (int i = 0; i < AJ; i++) {
            int s, e;
            cin >> s >> e;
            for (int j = s; j < e; j++)
                min_doing[j] = JAMIE;
        }

        for (int i = 0; i < MAXM; i++)
            for (int j = 0; j < 2; j++)
                for (int k = 0; k < MAXEACH; k++)
                    memo[i][j][k] = -1;
        STARTING = 0;
        int a = solve(0, 0, 720);

        for (int i = 0; i < MAXM; i++)
            for (int j = 0; j < 2; j++)
                for (int k = 0; k < MAXEACH; k++)
                    memo[i][j][k] = -1;
        STARTING = 1;
        int b = solve(0, 1, 720);

        printf("Case #%d: %d\n", t, min(a, b));
    }
    return 0;
}
