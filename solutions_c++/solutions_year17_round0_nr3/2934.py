#include <bits/stdc++.h>
using namespace std;

void print_ans_for_range(long long r) {
    auto pos = (1 + r)/2;
    cout << max(r - pos, pos - 1) << " " << min(r - pos, pos - 1) << endl;
}

void solve() {
    long long n, k;
    cin >> n >> k;
    long long rem = 1, lv = 1;
    while (rem * 2 <= k) {
        rem *= 2;
        lv *= 2;
    }
    k -= rem;
    n -= rem;
    auto p = n % lv;
    auto r = n / lv;
    if (k <= p) {
        r++;
    }
    print_ans_for_range(r);
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
