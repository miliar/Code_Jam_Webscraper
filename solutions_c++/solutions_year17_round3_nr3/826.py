#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <numeric>
#include <climits>
#include <cmath>

using namespace std;

int main(int argc, char **argv)
{
    int T;
    cin >> T;
    for (int testcase = 1; testcase <= T; testcase++) {
        int N, K;
        double U;
        cin >> N >> K >> U;
        vector<double> P(N);
        for (int i = 0; i < N; i++)
            cin >> P[i];
        sort(P.begin(), P.end());
        double maxr = 0;
        for (int i = 0; i <= N; i++) {
            double r = 1;
            if (i > 0) {
                double q = U;
                for (int j = 0; j < i; j++) {
                    q += P[j];
                }
                q /= i;
                for (int j = 0; j < i; j++) {
                    r *= min(q, 1.0);
                    if (q < P[j])
                        r = 0;
                }
            }
            for (int j = i; j < N; j++) {
                r *= P[j];
            }
            maxr = max(maxr, r);
        }
        cout << "Case #" << testcase << ": ";
        cout.precision(10);
        cout << maxr << endl;
    }
    return 0;
}

// vim: sw=4:
