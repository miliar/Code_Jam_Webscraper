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

const double PI = acos(-1);

int main(int argc, char **argv)
{
    int T;
    cin >> T;
    for (int testcase = 1; testcase <= T; testcase++) {
        int N, K;
        cin >> N >> K;
        vector<int> R(N), H(N);
        for (int i = 0; i < N; i++)
            cin >> R[i] >> H[i];
        vector<double> A(N);
        for (int i = 0; i < N; i++)
            A[i] = 2 * PI * R[i] * H[i];
        vector<int> P(N);
        iota(P.begin(), P.end(), 0);
        sort(P.begin(), P.end(), [&](int a, int b) { return A[a] > A[b]; });
        double maxa = 0;
        for (int i = 0; i < N; i++) {
            double a = PI * R[i] * R[i] + A[i];
            int k = K - 1;
            for (int j = 0; j < N && k > 0; j++) {
                if (P[j] == i)
                    continue;
                if (R[P[j]] <= R[i]) {
                    k--;
                    a += A[P[j]];
                }
            }
            if (!k)
                maxa = max(maxa, a);
        }
        cout << "Case #" << testcase << ": ";
        cout.precision(10);
        cout << maxa << endl;
    }
    return 0;
}

// vim: sw=4:
