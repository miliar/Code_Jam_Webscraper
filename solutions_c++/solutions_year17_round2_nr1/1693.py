#include <iostream>
#include <iomanip>
#include <vector>
#include <utility>
#define REP(i,a,b) for(int i=int(a);i<int(b);i++)

using namespace std;

typedef long long int lli;
typedef pair<int, int> pii;

int main () {
    int T;
    cin >> T;
    REP (_, 0, T) {
        int D, N;
        cin >> D >> N;
        vector<pii> data(N);
        REP (i, 0, N) cin >> data[i].first >> data[i].second;
        double cmax = 0;
        REP (i, 0, N) {
            cmax = max(cmax, (double)(D - data[i].first) / data[i].second);
        }
        double ans = D / cmax;
        cout << "Case #" << _ + 1 << ": " << fixed << setprecision(10) << ans << endl;
    }
    return 0;
}
