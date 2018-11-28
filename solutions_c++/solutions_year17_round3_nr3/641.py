#include <bits/stdc++.h>
#include <ext/numeric>
#include <ext/rope>
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/hash_policy.hpp>
#include <ext/pb_ds/tree_policy.hpp>
#include <ext/pb_ds/priority_queue.hpp>
using namespace __gnu_cxx;
using namespace __gnu_pbds;
template<typename T>
using pbq = priority_queue<T>;
using namespace std;
using LL = int64_t;
using LD = long double;
const int INF = 0x3f3f3f3f;
#define X first
#define Y second
int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    fstream cin("C-small.in");
    fstream cout("out.txt");
    const LD PI = acos(-1);
    int t;
    cin >> t;
    int T = t;
    while (t--) {
        cout << "Case #" << T - t << ": ";
        int n, k;
        cin >> n >> k;
        LD u;
        cin >> u;
        vector<LD> a(n);
        for (auto& i : a) cin >> i;
        sort(a.begin(), a.end());
        for (int i = 1; i < n; i++) {
            LD sum = (a[i] - a[i - 1]) * i;
            if (u - sum <= 1e-7) {
                u /= i;
                for (int j = 0; j < i; j++) a[j] += u;
                u = 0;
                break;
            } else {
                u -= sum;
                for (int j = 0; j < i; j++) a[j] = a[i];
            }
        }
        if (u > 1e-7) {
            u /= n;
            for (int i = 0; i < n; i++) a[i] += u;
            u = 0;
        }
        cout << fixed << setprecision(6) << accumulate(a.begin(), a.end(), 1.0, multiplies<LD>()) << endl;
    }
}
