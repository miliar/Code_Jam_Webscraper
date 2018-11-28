#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#include <utility>
#include <climits>
#include <string>
#include <iomanip>
using namespace std;

typedef long long ll;
typedef double long ld;

ld getArea(int bestBase, int k, vector<pair<ll, ll> > v)
{
    ld r = v[bestBase].second;
    ld area = M_PI * v[bestBase].second * v[bestBase].second;
    ld side = 2.0 * M_PI * v[bestBase].second * v[bestBase].first;
    area += side;
    v.erase(v.begin() + bestBase);
    vector<ld> v2;
    for (int i = 0; i < v.size(); ++i) {
        if (v[i].second <= r) {
            v2.push_back(2.0 * M_PI * v[i].second * v[i].first);
        }
    }

    sort(v2.rbegin(), v2.rend());
    for (int i = 0; i < k-1; ++i) {
        if (i >= v2.size()) {
            return 0;
        }
        area += v2[i];
    }
    return area;
}

int main()
{
    int cases;
    cin >> cases;
    for (int cas = 1; cas <= cases; ++cas) {
        int n, k;
        cin >> n >> k;
        vector<pair<ll, ll> > v(n);
        for (int i = 0; i < n; ++i) {
            cin >> v[i].second >> v[i].first;
        }
        ld best = 0;
        for (int i = 0; i < n; ++i) {
            best = max(best, getArea(i, k, v));
        }
        cout << "Case #" << cas << ": " << fixed << setprecision(9) << best << endl;
    }
}
