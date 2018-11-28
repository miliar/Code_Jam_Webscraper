#include <iostream>
#include <vector>
#include <utility>
#include <fstream>
#include <string>
#include <cmath>
#include <algorithm>

using namespace std;

using LD = long double;
const LD eps = 0.000000001;

int main () {
    ifstream cin("input.txt");
    ofstream cout("output.txt");
    cin.tie(nullptr);
    std::ios_base::sync_with_stdio(false);
    cout.setf(std::ios_base::fixed);
    cout.precision(8);
    cerr.setf(std::ios_base::fixed);
    cerr.precision(25);
    int tt;
    cin >> tt;
    for (int t = 0; t < tt; ++t) {
        int n;
        int d;
        cin >> d >> n;
        vector < pair < LD, LD > > x(n);
        for (int i = 0; i < n; ++i) {
            cin >> x[i].first >> x[i].second;
        }
        LD bg = 0, ed = 1e18;
        for (int it = 0; it < 200; ++it) {
            LD mid = (ed + bg) / 2;
            bool ok = true;
            for (int i = 0; i < n; ++i) {
                if (x[i].second > mid) {
                    continue;
                }
                LD tm = (d - x[i].first) * mid;
                LD ftime = d * x[i].second;
                if (tm - ftime > 0.0) {
                    ok = false;
                    break;
                }
            }
            if (ok) {
                bg = mid;
            } else {
                ed = mid;
            }
        }
        /*if (bg > 1e10) {
            cerr << d / bg << " " << (d - x[0].first) / x[0].second << endl;
            cerr << d << "\n";
            for (auto p: x) {
                cerr << p.first << " " << p.second << "\n";
            }
            cerr << bg << endl;
            return 0;
        }*/
        //cerr << t << endl;
        cout << "Case #" << t + 1 << ": " << bg << "\n";
    }
    return 0;
}


