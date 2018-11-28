#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main() {

    freopen("A-large (1).in", "r", stdin); // redirects standard input
    freopen("output.txt", "w", stdout); // redirects standard output


    int t, n, m; cin >> t;
    char mp[30][30];
    for(int z = 0; z < t; ++z) {
        cin >> n >> m;
        for(int i = 0; i < n; ++i) {
            for(int j = 0; j < m; ++j) cin >> mp[i][j];
        }
        int gl_last = 0;
        for(int i = 0; i < n; ++i) {
            int c = 0, last = 0;
            for(int j = 0; j < m; ++j) {
                if(mp[i][j] != '?') {
                    c += 1;
                    for(int z = last; z <= j; ++z) mp[i][z] = mp[i][j];
                    last = j + 1;
                }
            }

            if(c > 0) {
                for(int j = last; j < m; ++j) mp[i][j] = mp[i][last-1];

                for(int zi = gl_last; zi < i; ++zi) {
                    for(int zj = 0; zj < m; ++zj) {
                        mp[zi][zj] = mp[i][zj];
                    }
                }
                gl_last = i + 1;
            }
            else {
                gl_last = min(gl_last, i);
            }
        }

        for(int zi = gl_last; zi < n; ++zi) {
            for(int zj = 0; zj < m; ++zj) {
                mp[zi][zj] = mp[gl_last-1][zj];
            }
        }
        cout << "Case #" << z + 1 << ":" << endl;
        for(int i = 0; i < n; ++i) {
            for(int j = 0; j < m; ++j) cout << mp[i][j];
            cout << endl;
        }
    }
}
