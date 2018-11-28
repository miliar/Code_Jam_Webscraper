#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <iomanip>

using namespace std;

double PI = acos(0)*2;

typedef long long LL;
typedef pair<LL, LL> pll;

bool by_sides(pll a, pll b) {
    return a.first * a.second < b.first * b.second;
}

bool by_top(pll a, pll b) {
    return a.first * a.first < b.first * b.first;
}

double side_area(pll a) {
    return PI * 2 * a.first * a.second;
}

double top_area(pll a) {
    return PI * a.first * a.first;
}

int main() {
    int T;
    int n,k;
    vector<pll> pancakes;
    cin >> T;
    for (int cs = 1; cs <= T; cs++) {
        cin >> n >> k;
        pancakes.resize(n);
        for (int i = 0; i < n; i++) {
            cin >> pancakes[i].first >> pancakes[i].second; 
        }
        double ans = 0;
        sort(pancakes.begin(), pancakes.end(), by_top);
        ans += top_area(pancakes[n-1]);
        ans += side_area(pancakes[n-1]);
        sort(pancakes.begin(), --pancakes.end(), by_sides);
        for (int i = 1; i < k; i++) {
            ans += side_area(pancakes[n-1-i]);
        }
        double ans_2 = 0;
        LL largest_r = 0;
        sort(pancakes.begin(), pancakes.end(), by_sides);
        for (int i = 0; i < k; i++) {
            largest_r = max(largest_r, pancakes[n-1-i].first);
            ans_2 += side_area(pancakes[n-1-i]);
        }
        ans_2 += top_area({largest_r, 0});
        cout << fixed << setprecision(8) << "Case #" << cs << ": " << max(ans_2, ans) << endl;
    }
}