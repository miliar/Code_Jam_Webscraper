#include <iostream>
#include <vector>
#include <math.h>
#include <limits>
#include <cfloat>
#include <iomanip>

using namespace std;

struct pancake {
    long double lateral_area;
    long double top_area;
    long double total_area;

    pancake() {}

    pancake(long double r, long double h) {
        lateral_area = 2*r*h*M_PI;
        top_area = r*r*M_PI;
        total_area = lateral_area + top_area;
    }

    bool operator < (const pancake& p) const {
        return (lateral_area > p.lateral_area);
    }
};

int main() {
    cout << setprecision(9);
    cout << fixed;
    int t;
    cin >> t;
    for(int i = 1; i <= t; ++i) {
        int n, k;
        cin >> n >> k;
        vector<pancake> pancakes(n);
        for(int j = 0; j < n; ++j) {
            long double r, h;
            cin >> r >> h;
            pancakes[j] = pancake(r, h);
        }
        sort(pancakes.begin(), pancakes.end());
        long double total_lateral_area = 0;
        long double max_top_area = 0;
        long double min_lateral_area = DBL_MAX;
        for(int j = 0; j < k; ++j) {
            total_lateral_area += pancakes[j].lateral_area;
            max_top_area = max(max_top_area, pancakes[j].top_area);
            min_lateral_area = min(min_lateral_area, pancakes[j].lateral_area);
        }
        for(int j = k; j < n; ++j) {
            if(pancakes[j].top_area > max_top_area) {
                if(pancakes[j].total_area - max_top_area > min_lateral_area) {
                    total_lateral_area -= min_lateral_area;
                    total_lateral_area += pancakes[j].lateral_area;
                    max_top_area = pancakes[j].top_area;
                    min_lateral_area = pancakes[j].lateral_area;
                }
            }
        }
        cout << "Case #" << i << ": " << total_lateral_area + max_top_area << endl;
    }
}