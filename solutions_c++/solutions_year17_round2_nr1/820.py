#include <iostream>
#include <vector>

using namespace std;

long double EPS = 0.00000098;

vector<long double> K, S;
long double d;
int n;


bool ok(long double s, int i) {
    if (s < S[i])
        return true;
    return d * S[i] >= s * (d - K[i]);
}


bool allOk(long double s) {
    bool f = true;
    for (int i = 0; i < n; ++i)
        f &= ok(s, i);
    return f;
}


void solve() {
    cin >> d >> n;
    cerr << d << " " << n << "\n";

    K.resize(n); S.resize(n);
    for (int i = 0; i < n; ++i)
        cin >> K[i] >> S[i];

    long double l, m, r;
    l = 1;
    r = 1e16;
    while (r - l > EPS) {
        m = (l + r) / (long double)2.0;
        if (allOk(m))
            l = m;
        else
            r = m;
        cerr << l << " " << m << " " << r << r - l << "\n";
    }
    cout << l << "\n";
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