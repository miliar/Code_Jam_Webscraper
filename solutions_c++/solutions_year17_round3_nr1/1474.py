#include <iostream>
#include <algorithm>
#include <vector>
#include <utility>

using namespace std;

const double pi = 3.14159265358979;

int main() {
    int T;
    cin >> T;
    for (int I = 1; I <= T; I++) {
        int n, k;
        cin >> n >> k;
        vector<pair<double, double>> sf;
        for (int i = 0; i < n; i++) {
            int rr, hh;
            cin >> rr >> hh;
            sf.push_back({pi * 2 * rr * hh, pi * rr * rr});
        }
        sort(sf.begin(), sf.end(), greater<pair<double, double>>());
        double sum = 0, max = 0;
        for (int i = 0; i < k; i++) {
            auto &t = sf[i];
            sum += t.first;
            if (t.second > max) max = t.second;
        }
        double v1 = sum + max;
        sum -= sf[k-1].first;
        max = 0;
        for (int i = k - 1; i < n; i++) {
            double v = sf[i].first + sf[i].second;
            if (v > max) max = v;
        }
        if (sum + max > v1) v1 = sum + max;
        printf("Case #%d: %.9f\n", I, v1);
    }
    return 0;
}

