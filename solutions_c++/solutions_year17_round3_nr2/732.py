#include <bits/stdc++.h>

#define F first
#define S second
#define pb push_back
#define INF (1 << 30)
#define SQR(a) ((a) * (a))

using namespace std;

const int M = 24 * 60;
const int N = M + 10; 

int f[N][N][2];
int d[N * N];

void rundp() {
    for (int i = 0; i <= M / 2; i++) {
        for (int j = 0; j <= M / 2; j++) {
            if (i == j && j == 0)
                continue;
            
            int t = i + j;
            t--;

            if (i > 0)
                f[i][j][0] = f[i - 1][j][0];
            if (j > 0)
                f[i][j][0] = min(f[i][j][0], f[i][j - 1][1] + 1);
            if (d[t] == 1)
                f[i][j][0] = INF;

            if (j > 0)
                f[i][j][1] = f[i][j - 1][1];
            if (i > 0)
                f[i][j][1] = min(f[i][j][1], f[i - 1][j][0] + 1);
            if (d[t] == 2)
                f[i][j][1] = INF;

            //printf("f[%d][%d][0] = %d, f[%d][%d][1] = %d\n", i, j, f[i][j][0], i, j, f[i][j][1]);
        }
    }
}

void solve() {
    int ac, aj;
    cin >> ac >> aj;

    fill(d, d + N, 0);

    for (int i = 0; i < ac; i++) {
        int s, f;
        cin >> s >> f;
        for (int j = s; j < f; j++) {
            d[j] = 1;
        }
    }

    for (int j = 0; j < aj; j++) {
        int s, f;
        cin >> s >> f;
        for (int j = s; j < f; j++) 
            d[j] = 2;
    }

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            f[i][j][0] = f[i][j][1] = INF;
        }
    }

    f[0][0][0] = 0;

    rundp();

    int ans = INF;
    ans = min(ans, f[M / 2][M / 2][0]);
    ans = min(ans, f[M / 2][M / 2][1] + 1);

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            f[i][j][0] = f[i][j][1] = INF;
        }
    }

    f[0][0][1] = 0;

    rundp();

    ans = min(ans, f[M / 2][M / 2][1]);
    ans = min(ans, f[M / 2][M / 2][0] + 1);

    cout << ans;
}

int main()
{
    //freopen("input.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);
    
    
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        cout << "Case #" << i << ": ";
        solve();
        cout << endl;
    }

    return 0;
}
