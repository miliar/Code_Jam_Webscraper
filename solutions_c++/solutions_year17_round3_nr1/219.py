#include <algorithm>
#include <iostream>
#include <cmath>
#include <vector>
#include <map>
using namespace std;

long double calcMaxArea(const vector<pair<long long, long long>>& cakes, int k, int takenId) {
    vector<pair<long long, long long>> cs(cakes.begin(), cakes.end());
    cs.erase(cs.begin() + takenId);
    sort(cs.begin(), cs.end(), [](const pair<long long, long long>& a, const pair<long long, long long>& b) {
        return a.first * a.second > b.first * b.second;
    });
    long double result = cakes[takenId].first * cakes[takenId].second * 2 * M_PI;
    for (int i = 0; i < k - 1; ++i) {
        result += cs[i].first * cs[i].second * 2 * M_PI;
    }
    result += pow((long double)cakes[takenId].first, 2.0) * M_PI;
    return result;
}

long double calcMaxArea(const vector<pair<long long, long long>>& cakes, int k) {
    long double maxArea = 0;
    int n = cakes.size();
    for (int i = 0; i < n; ++i) {
        maxArea = max(maxArea, calcMaxArea(cakes, k, i));
    }
    return maxArea;
}


int main() {
    ios_base::sync_with_stdio(false);
    int numTests;
    cin >> numTests;
    cout.precision(10);
    cout << fixed;
    for (int tId = 0; tId < numTests; ++tId) {
        int n, k;
        cin >> n >> k;
        vector<pair<long long, long long>> cakes(n);
        for (int i = 0; i < n; ++i) cin >> cakes[i].first >> cakes[i].second;
        cout << "Case #" << tId + 1 << ": " << calcMaxArea(cakes, k) << endl;
    }
    return 0;
}
