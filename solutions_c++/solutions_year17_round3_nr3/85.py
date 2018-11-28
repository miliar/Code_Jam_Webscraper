#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <string>
#include <tuple>
#include <sstream>
#include <cmath>
#include <vector>
#include <unordered_map>
#include <queue>
#include <cstdlib>
using namespace std;


int main () {
    int cases;
    cin >> cases;
    for (int cc = 1; cc <= cases; ++cc) {
        cout << "Case #" << cc << ": ";
        int k, n;
        double u;
        cin >> n >> k >> u;
        vector<double> v;
        for (int i = 0; i < n; ++i) {
            double d;
            cin >> d;
            v.push_back(d);
        }
        sort(v.begin(), v.end());
        for (int i = 0; i < v.size() - 1; ++i) {
            double diff = v[i + 1] - v[i];
            double area = diff * (i + 1);
            //cout << "area " << area << ' ' << u << ' ' << diff << ' ' << v[i] << ' ' << v[i + 1] << endl;
            if (u <= area) {
                double addition = u / (i + 1);
                for (int j = 0; j <= i; ++j) {
                    v[j] += addition;
                }
                u = 0;
                break;
            } else {
                for (int j = 0; j <= i; ++j) {
                    v[j] = v[i + 1];
                }
                u -= area;
            }
        }
        if (u > 0) {
            double addition = u / v.size();
            for (int i = 0; i < v.size(); ++i) {
                v[i] += addition;
            }
        }
        double sol = 1;
        for (int i = 0; i < v.size(); ++i) {
            sol *= v[i];
        }
        printf("%.8lf\n", sol);
    }
}
