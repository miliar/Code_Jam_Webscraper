#include <iostream>
#include <cstdio>
#include <queue>
#include <limits>
#include <cstring>
#include <iomanip>
using namespace std;

typedef unsigned long ul;
typedef long double ld;

int t;
int n, q;
ul e[101]; int s[101];
ul d[101][101];
int u, v;

bool visit[101];
ld dtime[101][101];

void makeTime(int i, int city, ld timeTaken, ul rdist) {
    visit[city] = true;
    dtime[i][city] = timeTaken;
    for(int j = 1; j < n; ++j) {
        ul dist = d[city][j];
        if(!visit[j] && rdist >= dist && dist != -1)
            makeTime(i, j, timeTaken + (ld)(dist) / (ld)(s[i]), rdist - dist);
    }
}

void makeTimes() {
    for(int i = 1; i <= n; ++i)
        for(int j = 1; j <= n; ++j) {
            ul dist = d[i][j];
            if(dist <= e[i])
                dtime[i][j] = (ld)(dist) / (ld)(s[i]);
            else
                dtime[i][j] = numeric_limits<long double>::max();
        }
}

void makeDists() {
    for(int k = 1; k <= n; ++k)
        for(int i = 1; i <= n; ++i)
            for(int j = 1; j <= n; ++j) {
                if(d[i][k] == -1 || d[k][j] == -1)
                    continue;
                if(d[i][j] > d[i][k] + d[k][j]) {
                    d[i][j] = d[i][k] + d[k][j];
                }
            }
}

void fw() {
    for(int k = 1; k <= n; ++k)
        for(int i = 1; i <= n; ++i)
            for(int j = 1; j <= n; ++j) {
                if(dtime[i][k] == numeric_limits<long double>::max() ||
                   dtime[k][j] == numeric_limits<long double>::max())
                    continue;
                //cout << "made it" << endl;
                //cout << dtime[i][j] << " " << dtime[i][k] << " " << dtime[k][j] << endl;
                if(dtime[i][j] > dtime[i][k] + dtime[k][j]) {
                    //cout << "\tchange it" << endl;
                    dtime[i][j] = dtime[i][k] + dtime[k][j];
                }
            }
}

int main() {
    cin >> t;
    for(int tc = 1; tc <= t; ++tc) {
        cin >> n >> q;
        for(int i = 1; i <= n; ++i)
            cin >> e[i] >> s[i];
        for(int i = 1; i <= n; ++i)
            for(int j = 1; j <= n; ++j)
                cin >> d[i][j];
        makeDists();
        makeTimes();

        // for(int i = 1; i <= n; ++i) {
        //     for(int j = 1; j <= n; ++j) {
        //         cout << dtime[i][j] << "\t";
        //     }
        //     cout << endl;
        // }
        // cout << endl;
        fw();
        // for(int i = 1; i <= n; ++i) {
        //     for(int j = 1; j <= n; ++j) {
        //         cout << dtime[i][j] << "\t";
        //     }
        //     cout << endl;
        // }
        // cout << endl;

        printf("Case #%d:", tc);
        for(int k = 0; k < q; ++k) {
            cin >> u >> v;
            cout << " " << fixed << setprecision(7) << dtime[u][v];
        }
        cout << endl;
    }

    return 0;
}
