#include <bits/stdc++.h>
using namespace std;

vector<pair<long long, double>> hor;
long long d[105][105];
double d2[105][105];

int n;

void fw() {
    for(int i = 1 ; i <= n ; i++) {
        for(int j = 1 ; j <= n ; j++) {
            if (d[i][j] == -1) {
                d[i][j] = 1e12;
            }
        }
    }
    
    for(int k = 1 ; k <= n ; k++) {
        for(int i = 1 ; i <= n ; i++) {
            for(int j = 1 ; j <= n ; j++) {
                d[i][j] = min(d[i][k] + d[k][j], d[i][j]);
            }
        }
    }
}

void fw2() {
    for(int i = 1 ; i <= n ; i++) {
        for(int j = 1 ; j <= n ; j++) {
            if (d[i][j] > hor[i].first) {
                d2[i][j] = 1e20;
            }
            else {
                d2[i][j] = d[i][j] / hor[i].second;
            }
        }
    }
    for(int k = 1 ; k <= n ; k++) {
        for(int i = 1 ; i <= n ; i++) {
            for(int j = 1 ; j <= n ; j++) {
                d2[i][j] = min(d2[i][k] + d2[k][j], d2[i][j]);
            }
        }
    }
}

void solve() {
    int q;
    memset(d, -1, sizeof(d));
    cin >> n >> q;
    hor.clear();
    hor.resize(n+1);
    for(int i = 1 ; i <= n ; i++) {
        cin >> hor[i].first >> hor[i].second;
    }
    for(int i = 1 ; i <= n ; i++) {
        for(int j = 1 ; j <= n ; j++) {
            cin >> d[i][j];
        }
    }
    fw();
    fw2();
    
//    for(int i = 1 ; i <= n ; i++) {
//        for(int j = 1 ; j  <= n ; j++) {
//            cout << d[i][j] << " ";
//        }
//        cerr  << endl;
//    }
//    cerr << endl;
//    for(int i = 1 ; i <= n ; i++) {
//        for(int j = 1 ; j  <= n ; j++) {
//            cout << d2[i][j] << " ";
//        }
//        cerr  << endl;
//    }
    while (q--) {
        int u, v;
        cin >> u >> v;
        cout << fixed << setprecision(10) << d2[u][v] << " ";
    }
    cout << endl;
}

int main(int argc, const char **argv) {
    if(argc>=2) {
        freopen(argv[1], "r", stdin);
        freopen(argv[2], "w", stdout);
    }
    int T;
    cin >> T;
    for(int t = 1 ; t <= T ; t++) {
        printf("Case #%d: ", t);
        solve();
        fprintf(stderr, "Finished case %d\n\n", t);
    }
}
