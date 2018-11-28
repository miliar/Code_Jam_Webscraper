#include <iostream>
#include <vector>
#include <map>
#include <unordered_map>
#include <list>
#include <string>
#include <algorithm>
#include <chrono>
#include <limits>
#include <cmath>
#include <unordered_set>
#include <set>

using namespace std;
using ll = long long;

int main()
{
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        ll n, k;
        cin >> n >> k;

        multiset<ll> ds;

        ds.insert(n);

        for (int i = 0; i < k - 1; ++i) {
            ll d = *ds.rbegin();
            {
                auto it = ds.find(d);
                ds.erase(it);
            }
            if (d > 1) {
                ds.insert((d + 1) / 2 - 1);
                ds.insert(d - (d + 1) / 2);
            }
        }

        ll d = *ds.rbegin();
        cout << "Case #" << t << ": ";
        cout << (d - (d + 1) / 2) << " " << ((d + 1) / 2 - 1) << endl;
    }

    return 0;
}
