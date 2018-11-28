#include <iostream>
#include <algorithm>
#include <cstdio>
#include <vector>
#include <string>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define pb push_back
#define mp make_pair
#define fs first
#define sc second

int main() {
    freopen("B-large.in", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    ios::sync_with_stdio(false);
    int t;
    cin >> t;
    forn (q, t) {
        long long n;
        cin >> n;
        vector<int> a;
        while (n) {
            a.pb(n % 10);
            n /= 10;
        }
        int beg = a.size() - 1;
        for (int i = int(a.size()) - 1; i > 0; --i) {
            if (a[i - 1] > a[i]) {
                beg = i - 1;
            }
            if (a[i - 1] < a[i]) {
                a[beg]--;
                for (int j = beg - 1; j >= 0; --j) {
                    a[j] = 9;
                }
                break;
            }
        }
        long long ans = 0;
        for (int i = int(a.size()) - 1; i >= 0; --i) {
            ans *= 10;
            ans += a[i];
        }
        cout << "Case #" << q + 1 << ": " << ans << endl;
    }
}
