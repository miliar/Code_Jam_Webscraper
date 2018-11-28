#include <iostream>
#include <vector>
#include <iomanip>
#include <algorithm>
#include <utility>
#include <cmath>
#include <functional>
#include <queue>
#include <cstdlib>

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
        double U;
        cin >> U;
        vector<double> P(N);
        REP (i, 0, N) cin >> P[i];
        priority_queue<double, vector<double>, greater<double>> pq;
        REP (i, 0, N) pq.push(P[i]);
        while (U >= 1e-9) {
            double f = pq.top();
            int cnt = 0;
            while (pq.size() && abs(f - pq.top()) <= 1e-9) {
                cnt++;
                pq.pop();
            }
            if (pq.size() == 0) {
                f += U / cnt;
                U = 0;
                REP (i, 0, N) pq.push(f);
                break;
            } else {
                double diff = pq.top() - f;
                if (diff * cnt <= U) {
                    REP (i, 0, cnt) {
                        pq.push(f + diff);
                    }
                } else {
                    REP (i, 0, cnt) {
                        pq.push(f + U / cnt);
                    }
                }
                U = max(0.0, U - diff * cnt);
            }
        }

        double ans = 1.0;
        REP (i, 0, N) {
            ans *= pq.top();
            pq.pop();
        }
        cout << "Case #" << _ + 1 << ": " << fixed << setprecision(10) << ans << endl;
    }
    return 0;
}
