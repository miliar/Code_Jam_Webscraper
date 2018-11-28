#include <bits/stdc++.h>
using namespace std;

vector<long long> v;

const long long tenp18 = 1000LL * 1000 * 1000 * 1000 * 1000 * 1000;
const long long tenp17 = tenp18 / 10;

void gen(long long x = 0) {
    assert(x >= 0);
    v.push_back(x);
    if (x >= tenp17) {
        return;
    }
    for(int i = (x % 10) + (x == 0? 1 : 0) ; i < 10 ; i++) {
        gen(x * 10LL + i);
    }
}

void solve() {
    long long x;
    cin >> x;
    cout << *(upper_bound(v.begin(), v.end(), x) - 1) << endl;
}

int main(int argc, const char **argv) {
    if(argc>=2) {
        freopen(argv[1], "r", stdin);
        freopen(argv[2], "w", stdout);
    }
    gen();
    sort(v.begin(), v.end());
    int T;
    cin >> T;
    for(int t = 1 ; t <= T ; t++) {
        printf("Case #%d: ", t);
        solve();
        fprintf(stderr, "Finished case %d\n\n", t);
    }
}
