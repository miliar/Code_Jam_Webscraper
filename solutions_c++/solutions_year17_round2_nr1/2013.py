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

int main()
{
    int cases;
    cin >> cases;
    for (int cas = 1; cas <= cases; ++cas) {
        ll d, n;
        cin >> d >> n;
        vector<pair<ll, ll> > horses(n);
        for (int i = 0; i < n; ++i) {
            cin >> horses[i].first >> horses[i].second;
        }
        /*if (cas == 34) {

        }*/
        double result = 1e25;
        for (int i = 0; i < n; ++i) {
            double t = (d - horses[i].first) / (1.0 * horses[i].second);
            double maxV = d / t;
            //ll tmp1 = (d * horses[i].second);
            //ll tmp2 = (d - horses[i].first);
            //double maxV = 1.0 * tmp1 / tmp2;
            //cerr << "time " << t << " - speed " << maxV << endl;
            result = min(result, maxV);
        }
        cout << "Case #" << cas << ": " << fixed << setprecision(6) << result << endl;
    }
}
