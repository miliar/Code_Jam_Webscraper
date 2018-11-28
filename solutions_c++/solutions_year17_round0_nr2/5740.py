#include <iostream>
#include <cstdio>
#include <vector>
#include <fstream>

using namespace std;

int64_t Solution(int64_t n);
bool IsGood(int64_t n);

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    // freopen("in.txt", "r", stdin);
    // freopen("out.txt", "w", stdout);
    // ifstream cin("in.txt");
    // ofstream cout("out.txt");
    int cntTest;
    cin >> cntTest;
    for (int test = 0; test < cntTest; ++test) {
        int64_t n;
        cin >> n;
        cout << "Case #" << test + 1 << ": ";
        int64_t ans = Solution(n);
        if (ans == -1) {
            cout << "IMPOSSIBLE\n";
        } else {
            cout << ans << "\n";
        }
    }
   /* int t;
    cin >> t;
    cout << IsGood(t) << endl;*/
    return 0;
}
bool IsGood(int64_t n) {
    if (n < 10) {
        return true;
    }

    while (n) {
        if (n % 10 < (n / 10) % 10 ) {
            return false;
        }
        n /= 10;
    }
    return true;
}

int64_t Solution(int64_t n) {
    if (n < 10) {
        return n;
    }
    if (IsGood(n)) {
        return n;
    }

    int64_t buf = n, l = 0;
    while (buf) {
        ++l;
        buf /= 10;
    }
    int64_t step = 1;
    for (int64_t i = 0; i < l; ++i) {
        int64_t q = ((n / step) - 1) * step + (step - 1);
        //cerr << q << endl;
        if (q <= n && IsGood(q)) {
            cerr << "ww = " << q << endl;
            return q;
        }
        step *= 10;
    }

}