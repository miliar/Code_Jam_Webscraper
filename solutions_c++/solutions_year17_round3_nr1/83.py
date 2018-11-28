#include <iostream>
#include <cmath>
#include <vector>
#include <algorithm>
#include <utility>

using namespace std;

struct pancake {
    int64_t R;
    int64_t H;
};

void solve() {
    int64_t N, K; cin >> N >> K;

    vector<pancake> P(N);
    for (auto & p : P) {
        cin >> p.R >> p.H;
    }

    auto R_comp = [](pancake p1, pancake p2)->bool {
        return p1.R > p2.R;
    };

    auto side_area_comp = [](pancake p1, pancake p2)->bool {
        return p1.H*p1.R > p2.H*p2.R;
    };

    sort(P.begin(), P.end(), R_comp);

    int64_t max_area = 0;

    for (int64_t i = 0; i < N-K+1; i++) {
        int64_t area = P[i].R * P[i].R + 2*P[i].R * P[i].H;
        vector<pancake> tmp(P.begin()+i+1, P.end());
        sort(tmp.begin(), tmp.end(), side_area_comp);
        for (int64_t j = 0; j < K-1; j++) {
            area += 2 * (tmp[j].H * tmp[j].R); 
        }
        max_area = max(max_area, area);
    }
    
    printf("%.9f\n", double(max_area)*M_PI);
}

int main (void) {
    
    int T; cin >> T;
    for (int t = 1; t <= T; t++) {
        cout << "Case #" << t << ": ";
        solve();
    }
    return 0;
}
