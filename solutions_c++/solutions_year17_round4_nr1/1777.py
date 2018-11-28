#include <bits/stdc++.h>

using namespace std;

const size_t N = 110;
int dp_4[N][N][N][N], dp_3[N][N][N], dp_2[N][N];

void update(int& val, int new_val) {
    if (val == -1) {
        val = new_val;
    }
    else {
        val = max(val, new_val);
    }
}

void count_4() {
    dp_4[0][0][0][0] = 0;
    for (int i = 0; i < 100; ++i) {
        for (int j = 0; j <= i; ++j) {
            for (int k = 0; k + j <= i; ++k) {
                for (int l = 0; k + j + l <= i; ++k) {
                    if (dp_4[i][j][k][l] == -1) {
                        continue;
                    }
                    int happy = (k + 2 * l + (i - j - k - l) * 3) % 4 ? 0 : 1;
                    int val = dp_4[i][j][k][l] + happy;
                    update(dp_4[i + 1][j + 1][k][l], val);
                    update(dp_4[i + 1][j][k + 1][l], val);
                    update(dp_4[i + 1][j][k][l + 1], val);
                    update(dp_4[i + 1][j][k][l], val);
                }
            }
        }
    }
}

void count_3() {
    dp_3[0][0][0] = 0;
    for (int i = 0; i < 100; ++i) {
        for (int j = 0; j <= i; ++j) {
            for (int k = 0; k + j <= i; ++k) {
                if (dp_3[i][j][k] == -1) {
                    continue;
                }
                int happy = (k + (i - j - k) * 2) % 3 ? 0 : 1;
                int val = dp_3[i][j][k] + happy;
                update(dp_3[i + 1][j + 1][k], val);
                update(dp_3[i + 1][j][k + 1], val);
                update(dp_3[i + 1][j][k], val);
            }
        }
    }
}

void count_2() {
    dp_2[0][0] = 0;
    for (int i = 0; i < 100; ++i) {
        for (int j = 0; j <= i; ++j) {
            if (dp_2[i][j] == -1) {
                continue;
            }
            int happy = (i - j) % 2 ? 0 : 1;
            int val = dp_2[i][j] + happy;
            update(dp_2[i + 1][j + 1], val);
            update(dp_2[i + 1][j], val);
        }
    }
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    ios_base::sync_with_stdio(false);

    memset(dp_4, -1, N * N * N * N * sizeof(int));
    memset(dp_3, -1, N * N * N * sizeof(int));
    memset(dp_2, -1, N * N * sizeof(int));

    count_4();
    count_3();
    count_2();

    int T;
    cin >> T;

    for (int t = 1; t <= T; ++t) {
        int n, p;
        int mods[4];
        memset(mods, 0, 4 * sizeof(int));
        cin >> n >> p;
        for (int i = 0; i < n; ++i) {
            int x;
            cin >> x;
            ++mods[x % p];
        }
        cout << "Case #" << t << ": ";
        if (p == 2) {
            cout << dp_2[n][mods[0]];
        }
        else if (p == 3) {
            cout << dp_3[n][mods[0]][mods[1]];
        }
        else {
            cout << dp_4[n][mods[0]][mods[1]][mods[2]];
        }
        cout << "\n";
    }

    return 0;
}
