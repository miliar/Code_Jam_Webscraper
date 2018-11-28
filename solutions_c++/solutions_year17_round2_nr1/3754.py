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
#include <cassert>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    int t;
    cin >> t;
    cout.precision(17);
    for (int j = 1; j <= t; ++j) {
        long long D;
        long long N;
        cin >> D >> N;
        vector<double> horses(N);
        double tmax = -1.0;
        for (int i = 0; i < N; ++i) {
            int di, sp;
            cin >> di >> sp;

            tmax = max(tmax, (D - di) / (double)sp);
        }

        double ans = D / tmax;
        assert(tmax != -1.0);
        cout << "Case #" << j << ": " << ans << endl;
    }

    return 0;
}
