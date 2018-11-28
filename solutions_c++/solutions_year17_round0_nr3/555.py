#include <iostream>
#include <vector>

using namespace std;

int main() {
    #define int long long
    int t, n, k;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        cin >> n >> k;
        int lvl = 0;
        int ml = n, c1 = 1, c2 = 0;
        for (int pow = 1; lvl + pow < k; pow <<= 1) {
            if (ml % 2 == 0) {
                c2 = 2*c2 + c1;
            } else {
                c1 = 2*c1 + c2;
            }
            ml /= 2;
            lvl += pow;
        }
        int left = k - lvl;
        int d = (left <= c1) ? ml : ml - 1;
        d -= 1;
        int r = d/2 + d%2;
        int l = d/2;
        cout << "Case #" << i << ": " << r << " " << l << "\n";
    }
    return 0;
}