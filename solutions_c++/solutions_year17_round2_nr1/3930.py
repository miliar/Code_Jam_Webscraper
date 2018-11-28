#include <iostream>
#include <queue>
#include <cstdlib>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <stack>
#include <iomanip>

#define FOR(i,x,y) for(int i =(int)(x); i<(int)(y); i++)
#define REP(i, N) FOR(i, 0, N)
#define SZ(x) (int)x.size()

using namespace std;

typedef vector<int> vin;
typedef pair<int, int> pii;
typedef vector<pair<int, int> > vpii;
typedef vector<vector<int> > vvin;

typedef long long LL;
typedef unsigned long long ULL;

int main ()
{
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    int T; cin >> T;
    for (int t = 1; t <= T; ++t) {
        int D, N; cin >> D >> N;
        vector<pair<int, int>> v(N);
        for (int n = 0; n < N; ++n) {
            int K, S; cin >> K >> S;
            v[n] = make_pair(K, S);
        }

        std::sort(v.begin(), v.end()); // (K, S)
        double a = D;
        double vel = std::numeric_limits<double>::max();
        for (int i = N - 1; i >= 0; --i) {
            if (i != N - 1) {
                double t = double(v[i + 1].first - v[i].first) / double(v[i].second - v[i + 1].second);
                if (t > 0) {
                    a = min(a, v[i].second * t + v[i].first);
                }

            }


            vel  = min(vel, double(a * v[i].second) / double(a - v[i].first));
        }

        cout << fixed << setprecision(9) << "Case #" << t << ": " << vel << endl;
    }
    return 0;
}
