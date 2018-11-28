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
    fstream cin("B-small.in");
    fstream cout("out.txt");
    const LD PI = acos(-1);
    int t;
    cin >> t;
    int T = t;
    while (t--) {
        cout << "Case #" << T - t << ": ";
        int n, m;
        cin >> n >> m;
        vector<pair<int, int>> a(n), b(m);
        for (auto& i : a) cin >> i.X >> i.Y;
        for (auto& i : b) cin >> i.X >> i.Y;
        if (n < 2 && m < 2) cout << "2\n";
        else {
            auto& tmp = (n == 2 ? a : b);
            sort(tmp.begin(), tmp.end());
            if (tmp[1].Y - tmp[0].X > 720 && 24 * 60 + tmp[0].Y - tmp[1].X > 720) cout << "4\n";
            else cout << "2\n";
        }
    }
}
