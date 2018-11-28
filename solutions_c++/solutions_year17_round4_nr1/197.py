#include <iostream>
#include <algorithm>
#include <set>
#include <vector>
#include <string>
#include <cmath>
#include <map>

#define X first
#define Y second

using namespace std;

typedef long long ll;
typedef long double ld;


const int inf = 1e9 + 7;
const long double eps = 1e-7;

void prt(int tt, int x) {
    cout << "Case #" << tt + 1 << ": " << x << endl;
}

int main() {
ios_base::sync_with_stdio(0);
#ifdef _DEBUG
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif

    int t;
    cin >> t;
    for (int tt = 0; tt < t; ++tt) {
        int n, p;
        cin >> n >> p;
        
        vector<int> dt(p);
        for (int i = 0; i < n; ++i) {
            int x;
            cin >> x;
            ++dt[x % p];
        }
        if (p == 2) {
            int ans = dt[0] + (dt[1] + 1) / 2;
            prt(tt, ans);
        }
        if (p == 3) {
            if (dt[1] >= dt[2]) {
                int ans = dt[0] + dt[2];
                dt[1] -= dt[2];
                ans += (dt[1] + 2) / 3;
                prt(tt, ans);
            } else {
                int ans = dt[0] + dt[1];
                dt[2] -= dt[1];
                ans += (dt[2] + 2) / 3;
                prt(tt, ans);
            }
        }
        if (p == 4) {
            int ans = dt[0];
            if (dt[1] > dt[3])
                ans += dt[3], dt[1] -= dt[3], dt[3] = 0;
            else 
                ans += dt[1], dt[3] -= dt[1], dt[1] = 0;

            ans += dt[2] / 2;
            dt[2] %= 2;


            
            if (dt[2] && dt[3] >= 2)
                ans ++, dt[2] = 0, dt[3] -= 2;

            if (dt[2] && dt[1] >= 2)
                ans ++, dt[2] = 0, dt[1] -= 2;

            if ((dt[1] + dt[3]) == 0 && dt[2])
                ans ++, dt[2] = 0;

            ans += (dt[1] + dt[3] + 3) / 4;
            prt(tt, ans);
        }
    }
    return 0;
}