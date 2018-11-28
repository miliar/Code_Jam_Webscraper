#include <iostream>
#include <string>
using namespace std;


string X[30];
bool f[30][30][30][30];
bool z[30][30][30][30];

bool dp(int a, int b, int c, int d) {
    if (z[a][b][c][d]) return f[a][b][c][d];
    z[a][b][c][d] = true;
    f[a][b][c][d] = false;
    int cnt = 0;
    for (int i = a; i <= c; ++i) {
        for (int j = b; j <= d; ++j) {
            if (X[i][j] != '?') ++cnt;
        }
    }
    if (cnt == 1) return f[a][b][c][d] = true;
    if (cnt == 0) return f[a][b][c][d] = false;
    for (int i = a; i < c; ++i) f[a][b][c][d] |= (dp(a, b, i, d) && dp(i + 1, b, c, d));
    for (int i = b; i < d; ++i) f[a][b][c][d] |= (dp(a, b, c, i) && dp(a, i + 1, c, d));
    return f[a][b][c][d];
}

void fill(int a, int b, int c, int d) {
    int cnt = 0;
    char temp;
    for (int i = a; i <= c; ++i) {
        for (int j = b; j <= d; ++j) {
            if (X[i][j] != '?') {
                ++cnt;
                temp = X[i][j];
            }
        }
    }
    if (cnt == 1) {
        for (int i = a; i <= c; ++i) {
            for (int j = b; j <= d; ++j) X[i][j] = temp;
        }
        return ;
    }
    for (int i = a; i < c; ++i) {
        if (dp(a, b, i, d) && dp(i + 1, b, c, d)) {
            fill(a, b, i, d);
            fill(i + 1, b, c, d);
            return ;
        }
    }
    for (int i = b; i < d; ++i) {
        if (dp(a, b, c, i) && dp(a, i + 1, c, d)) {
            fill(a, b, c, i);
            fill(a, i + 1, c, d);
            return ;
        }
    }
}


int main() {
    int T;
    cin >> T;
    for (int times = 1; times <= T; ++times) {
        int N, M;
        cin >> N >> M;
        for (int i = 0; i < N; ++i) cin >> X[i];
        memset(z, 0, sizeof(z));
        dp(0, 0, N - 1, M - 1);
        fill(0, 0, N - 1, M - 1);
        cout << "Case #" << times << ":" << endl;
        for (int i = 0; i < N; ++i) cout << X[i] << endl; 
    }
    return 0;
}