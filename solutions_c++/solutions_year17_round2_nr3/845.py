#include <iostream>
#include <vector>

using namespace std;

int n, q, u, v;
vector <long double> E, S;
vector < vector <long double > > D;


void doit() {
    vector<long double> T(n, 1e16); 
    T[0] = 0;
    long double t, d;
    for (int i = 0; i < n; ++i) {
        // cerr << i << ": ";
        t = d = 0;
        for (int j = i + 1; j < n; ++j) {
            d += D[j - 1][j];
            t = d / S[i];
            if (d > E[i])
                break;
            T[j] = min(T[j], T[i] + t);
            // cerr << "(" << j << ", " << T[j] << "), ";
        }
        // cerr << "\n";
    }
    cout << T[n - 1] << "\n";
}


void solve() {
    cin >> n >> q;
    E.resize(n); S.resize(n);
    for (int i = 0; i < n; ++i)
        cin >> E[i] >> S[i];
    D.resize(n);
    for (int i = 0; i < n; ++i) {
        D[i].resize(n);
        for (int j = 0; j < n; ++j)
            cin >> D[i][j];
    }
    for (int i = 0; i < q; ++i) {
        cin >> u >> v;
        doit();
    }

}

int main() {
    int T; cin >> T;
    cout.precision(30);
    for (int t = 1; t <= T; ++t) {
        printf("Case #%d: ", t);
        solve();
    }
    return 0;
}