#include <iostream>
#include <vector>
#include <algorithm>
#include <utility>
#include <iomanip>
using namespace std;

bool cmp(const pair<long long,long long> &a, const pair<long long,long long> &b)
{
    return (a.second < b.second);
}

int main ()
{
    int T;
    cin >> T;
    for (int t = 0; t < T; t++) {
        long long N, K, sol = 0;
        cin >> N >> K;
        vector<long long> r(N), h(N);
        vector<pair<long long, long long> > rh(N);
        for (int i = 0; i < N; i++) {
            cin >> r[i] >> h[i];
            rh[i] = {r[i] * r[i], 2 * r[i] * h[i]};
        }
        sort(&rh[0], &rh[N]);

        for (int i = K - 1; i < N; i++) {
            long long curr = rh[i].first + rh[i].second;
            sort(&rh[0], &rh[i], cmp);
            for (int j = i - 1; j > i - K; j--)
                curr += rh[j].second;
            sol = max(sol, curr);
            cerr << curr << endl;
        }
        cout << std::fixed << std::setprecision(20);
        cout << "Case #" << t + 1  << ": " << 3.1415926536 * double(sol) << endl;
    }
    return 0;
}
