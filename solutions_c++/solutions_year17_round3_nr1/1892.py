#include <iostream>
#include <vector>
#include <map>
#include <string>
#include <set>
#include <queue>
#include <algorithm>
#include <tuple>
#include <unordered_set>
#include <cmath>

using namespace std;

#define PI 3.14159265358979323846


double max_height(vector<double>& heights, int e, int k) {
    priority_queue<double> pq;

    for (int i = 0; i < e; ++i ){
        pq.push(-heights[i]);
        if (pq.size() > k) {
            pq.pop();
        }
    }

    double ret = 0.0;
    while (pq.empty() == false) {
        ret += -pq.top();
        pq.pop();
    }

    return ret;
}

double solve(vector<tuple<double, double>> pans, int k) {
    sort(pans.begin(), pans.end());

    vector<double> heights(pans.size());
    for (int i = 0; i < heights.size(); ++i) {
        int r = get<0>(pans[i]);
        int h = get<1>(pans[i]);
        heights[i] = 2.0 * PI * (double)r * (double)h;
    }

    double ret = 0.0;
    for (int i = k-1; i < pans.size(); ++i) {
        int r = get<0>(pans[i]);
        int h = get<1>(pans[i]);

        ret = max(ret, PI * (double)r * (double)r + 2.0 * PI * (double)r * (double)h + max_height(heights, i, k-1));
    }


    return ret;
}

int main() {
    int T; cin >> T;
    for (int kase = 1; kase <= T; ++kase) {
        int N, K;
        cin >> N >> K;
        vector<tuple<double, double>> pans(N);
        for (int i = 0; i < N; ++i) {
            int r, h;
            cin >> r >> h;
            pans[i] = make_tuple(r, h);
        }

        printf("Case #%d: %.9lf\n", kase, solve(pans, K));
    }

    return 0;
}
