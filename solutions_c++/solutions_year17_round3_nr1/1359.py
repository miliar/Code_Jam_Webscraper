#include <bits/stdc++.h>
using namespace std;

const int MAX_ITEMS = 1001;
const double PI = 3.141592653589793238;
int T, n, k;

typedef struct {
    int r, h;
} Pancake;

Pancake pancake;
vector<Pancake> pancakes;

double res, val, dp[MAX_ITEMS][MAX_ITEMS];

bool sortPancakes(Pancake p1, Pancake p2) {
    return p1.r > p2.r;
}

void solve() {
    memset(dp, 0, (MAX_ITEMS) * (MAX_ITEMS) * sizeof(double));
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= i; j++) {
            val = 2 * PI * pancakes[i-1].r * pancakes[i-1].h;
            if (j == 1) {
                val += PI * pancakes[i-1].r * pancakes[i-1].r;
            }
            dp[i][j] = max(dp[i-1][j-1] + val, dp[i-1][j]);
        }
    }
    res = dp[n][k];
    pancakes.clear();
}

int main (int argc, char** argv) {
    cin >> T;
    for (int t = 1; t <= T; t++) {
        cout << "Case #" << t << ": ";
        cin >> n >> k;
        for (int i = 0; i < n; i++) {
            cin >> pancake.r >> pancake.h;
            pancakes.push_back(pancake);
        }
        sort(pancakes.begin(), pancakes.end(), sortPancakes);
        solve();
        printf("%.10lf\n", res);
    }
}