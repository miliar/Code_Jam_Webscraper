#include <iostream>
#include <vector>
#include <iomanip>
#include <algorithm>
#include <utility>
#include <cmath>
#include <functional>

#define REP(i,a,b) for(int i=int(a);i<int(b);i++)

using namespace std;

typedef long long int lli;
typedef pair<int,int> pii;

const double PI = acos(-1);

int main () {
    int T;
    cin >> T;
    REP (_, 0, T) {
        int N, K;
        cin >> N >> K;
        vector<pii> d(N);
        REP (i, 0, N) cin >> d[i].first >> d[i].second;
        sort(d.begin(), d.end());
        double ans = 0.0;
        REP (i, K - 1, N) {
            vector<double> v;
            v.reserve(N);
            REP (j, 0, i) {
                v.push_back(2 * PI * d[j].second * d[j].first);
            }
            sort(v.begin(), v.end(), greater<double>());
            double tm = PI * d[i].first * d[i].first + 2 * PI * d[i].second * d[i].first;
            REP (j, 0, K - 1) tm += v[j];
            ans = max(ans, tm);
        }

        cout << "Case #" << _ + 1 << ": " << fixed << setprecision(10) << ans << endl;
    }
    return 0;
}
