#include <bits/stdc++.h>

using namespace std;

int t, n, p;
int g[5];

int numZeros = 1;
bool down(int left, int psum) {
    if (left == 0) {
        if (psum % p == 0) numZeros++;
        return psum % p == 0;
    }

    for (int i = 1; i < p; i++) {
        if (g[i] > 0) {
            g[i]--;
            if (down(left - 1, psum + i)) {
                return true;
            }
            g[i]++;
        }
    }
    return false;
}

int main() {
    cin >> t;
    for (int test = 1; test <= t; test++) {
        cin >> n >> p;

        memset(g, 0, sizeof(g));
        int tmp;
        for (int i = 0; i < n; i++) {
            cin >> tmp;
            g[tmp % p]++;
        }
        numZeros = g[0] + 1;
        g[0] = 0;
        // cout << numZeros << endl;

        while (down(2, 0)) {}
        // cout << numZeros << " " << g[0] << " " << g[1] << " " << g[2] << '' endl;
        while (down(3, 0)) {}
        // cout << numZeros << endl;
        while (down(4, 0)) {}
        // cout << numZeros << endl;





        if (g[0] == 0 && g[1] == 0 && g[2] == 0 && g[3] == 0 && g[4] == 0) numZeros--;

        cout << "Case #" << test << ": " << numZeros << endl;
    }
}