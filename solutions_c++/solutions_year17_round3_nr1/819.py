#include <bits/stdc++.h>

using namespace std;

int T;

int main() {
    cin >> T;
    for (int t = 1; t <= T; ++t) {
        int N, K;
        cin >> N >> K;
        vector<pair<long long, int>> LtoI;
        vector<long long> Rs;
        for (int i = 0; i < N; ++i) {
            long long R, H;
            cin >> R >> H;
            long long L = R*2LL*H;
            LtoI.push_back(make_pair(L, i));
            Rs.push_back(R*R);
        }
        sort(LtoI.rbegin(), LtoI.rend());
        long long maxArea = -1;
        long long Lsuml = 0;
        for (int i = 0; i < K-1; ++i) Lsuml += LtoI[i].first;
        long long Lsum = Lsuml + LtoI[K-1].first;
        for (int i = 0; i < K; ++i) {
            long long candidate = Lsum + Rs[LtoI[i].second];
            if (candidate > maxArea) maxArea = candidate;
        }

        for (int i = K; i < N; ++i) {
            long long candidate = Lsuml + Rs[LtoI[i].second] + LtoI[i].first;
            if (candidate > maxArea) maxArea = candidate;
        }

        cout << "Case #" << t << ": " << setprecision(17) << (double)M_PI * maxArea << endl;
    }
}
