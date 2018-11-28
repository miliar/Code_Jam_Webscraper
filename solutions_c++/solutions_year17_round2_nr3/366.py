#include <cstdlib>
#include <cstring>

#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>

using namespace std;
typedef long long LL;

LL f[200][200];
int n, q;
LL e[200], s[200];
LL d[200][200];
LL u[200], v[200];

double g[200][200];

void init() {
    cin >> n >> q;
    for (int i = 0; i < n; i++) cin >> e[i] >> s[i];
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> d[i][j];
            f[i][j] = d[i][j];
        }
    }
    for (int i = 0; i < q; i++) {
        cin >> u[i] >> v[i];
    }
}

void floyd() {
    for (int k = 0; k < n; k++) {
        for (int i = 0; i < n; i ++) if (i != k && f[i][k] != -1) {
            for (int j = 0; j < n; j ++) if (j != k && j != i && f[k][j] != -1) {
                if (f[i][k] + f[k][j] < f[i][j] || f[i][j] == -1) {
                    f[i][j] = f[i][k] + f[k][j];
                }
            }
        }
    }
}

void floyd_g() {
    for (int k = 0; k < n; k++) {
        for (int i = 0; i < n; i ++) if (i != k && g[i][k] != 1e100) {
            for (int j = 0; j < n; j ++) if (j != k && j != i && g[k][j] != 1e100) {
                if (g[i][k] + g[k][j] < g[i][j] || g[i][j] == 1e100) {
                    g[i][j] = g[i][k] + g[k][j];
                }
            }
        }
    }
}



void prepare() {
    for (int i = 0; i < n; i ++)
        for (int j = 0; j < n; j ++) g[i][j] = 1e100;

    for (int i = 0; i < n; i ++) {
        for (int j = 0; j < n; j ++) if (i != j) {
            if (f[i][j] != -1 && f[i][j] <= e[i]) {
                g[i][j] = double(f[i][j]) / s[i];
            }
        }
    }

}


void work() {
    init();
    floyd();
    prepare();
/*
    std::cout << endl;
    for (int i = 0; i < n; i ++) {
        for (int j = 0; j < n; j ++) cout << g[i][j] << ' ';
        cout << endl;
    }
*/
    floyd_g();
    for (int i = 0; i < q; i ++) {
        printf(" %.9lf", g[u[i] - 1][v[i] - 1]);
    }
    cout << endl;
}

int main() {
    int tot; cin >> tot;
    for (int cas = 1; cas <= tot; cas ++) {
        cout << "Case #" << cas << ":";
        work();
    }
    return 0;
}
