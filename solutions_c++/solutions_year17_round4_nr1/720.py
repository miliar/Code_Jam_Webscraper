#include <iostream>
#include <string.h>
#include <queue>
#include <tuple>
#include <cmath>
#include <iomanip>
#include <algorithm>
#include <map>
#include <unordered_set>
#include <numeric>
#include <assert.h>

using namespace std;

const int N = (int) 2e5;

void solve(int test) {
    cout << "Case #" << test << ": ";
    int n, p;
    cin >> n >> p;
    vector <int> cnt(p);

    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        cnt[x % p]++;
    }
    int pref = 0;
    int ans = 0;
    for (int i = 0; i < n; i++) {
        if (!pref) {
            ans++;
        }
        int x = (p - pref) % p;
        if (cnt[x]) {
            cnt[x]--;
            pref = (pref + x) % p;
            continue;
        }
        for (int i = 0; i < p; i++) {
            if (cnt[i]) {
                pref = (pref + i) % p;
                cnt[i]--;
                break;
            }
        }
    }
    cout << ans << "\n";
}

int main() {
    freopen("A-small-attempt1.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t;
    cin >> t;
    for (int i = 1; i <= t; i++) {
        solve(i);
    }
    return 0;
}