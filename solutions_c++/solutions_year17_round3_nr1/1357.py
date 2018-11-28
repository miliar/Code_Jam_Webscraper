//
// Created by XelaPi.
//
#include <iostream>
#include <vector>
#include <algorithm>
#include <unordered_map>

using namespace std;

long double PI = 3.14159265358979323846264338327950288419716939937510;

struct Compare {
    bool operator()(pair<int, long double> const &a, pair<int, long double> const &b) {
        return a.second > b.second;
    }
};

int main() {

    int num;

    cin >> num;

    for (int i = 0; i < num; i++) {
        cout << "Case #" << (i + 1) << ": ";

        int n, k;

        cin >> n >> k;

        vector<long double> rs;
        vector<long double> hs;

        for (int j = 0; j < n; ++j) {
            long double r, h;

            cin >> r >> h;

            rs.push_back(r);
            hs.push_back(h);
        }

        vector<pair<int, long double>> sideAreas;
        vector<long double> topAreas;

        for (int l = 0; l < n; ++l) {
            sideAreas.push_back(make_pair(l, 2 * PI * rs[l] * hs[l]));
            topAreas.push_back(PI * rs[l] * rs[l]);
        }

        sort(sideAreas.begin(), sideAreas.end(), Compare());

        long double maxSideArea = 0;
        long double maxTopArea = 0;

        unordered_map<int, bool> used;

        for (int m = 0; m < k - 1; ++m) {
            maxSideArea += sideAreas[m].second;

            maxTopArea = max(maxTopArea, topAreas[sideAreas[m].first]);

            used[sideAreas[m].first] = true;
        }

        long double maxSurfaceArea = 0;

        for (int i1 = k - 1; i1 < n; ++i1) {
            long double newTopArea = max(maxTopArea, topAreas[sideAreas[i1].first]);
            long double newTest = maxSideArea + sideAreas[i1].second + newTopArea;

            maxSurfaceArea = max(maxSurfaceArea, newTest);
        }

        cout << to_string(maxSurfaceArea) << endl;
    }

    return 0;
}