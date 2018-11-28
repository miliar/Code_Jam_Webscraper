#include <bits/stdc++.h>
using namespace std;

void solve() {
    int n, d;
    cin >> d >> n;
    double mx =  -1;
    for(int i = 0 ; i < n ; i++) {
        double x, y;
        cin >> x >> y;
        mx = max((d - x)/(double)y, mx);
    }
    cout << fixed << setprecision(10) << (double)d/mx << endl;
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
