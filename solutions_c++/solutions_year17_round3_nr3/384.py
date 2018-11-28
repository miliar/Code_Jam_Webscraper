#include <iostream>
#include <algorithm>
#include <set>
#include <vector>
#include <string>
#include <cmath>
#include <map>
#include <cstdio>
#include <cassert>

#define X first
#define Y second

using namespace std;

typedef long long ll;
typedef long double ld;

const long double inf = 1e18 + 7;
const long double eps = 1e-18;

void prtans(int ans, int tt) {
    cout << "Case #" << tt + 1 << ": " << ans << endl; 
} 

int main() {
ios_base::sync_with_stdio(0);
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t;
    cin >> t;
    for (int tt = 0; tt < t; ++tt) {
        int n, m;
        cin >> n >> m;
        vector<pair<int, int> > a, b;
        for (int i = 0; i < n; ++i) {
            int l, r;
            cin >> l >> r;
            a.push_back({l, r});
        }
        sort(a.begin(), a.end());
        for (int i = 0; i < m; ++i) {
            int l, r;
            cin >> l >> r;
            b.push_back({l, r});
        }
        sort(b.begin(), b.end());
        
        if (n == 1 || m == 1) {
            prtans(2, tt);
            continue;
        }
        if (m == 2)
            swap(n, m), swap(a, b);
        if (n == 2) {
            if (a[1].second - a[0].first > 720) {
                if (a[0].second + 24 * 60 - a[1].first > 720) {
                    prtans(4, tt);
                    continue;
                }
            }
            prtans(2, tt);
        } 
    }
    return 0;
}