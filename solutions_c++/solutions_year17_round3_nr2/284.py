#include "vector"
#include "string"
#include "set"
#include "map"
#include "sstream"
#include "algorithm"
#include "cmath"
#include "cassert"
#include "iostream"
#include "numeric"
#include "fstream"
#include "queue"
#include <functional>
#include <climits>
#include <cstring>
#include <ctime>
#include <list>
#include <iomanip>
#include <limits>
#include <unordered_map>
#include <unordered_set>
#include <limits>
#include <complex>

#define int64 long long

#include <iostream>

using namespace std;
long double Pi = 3.1415926535897932384626433832795028841;

vector<int64> s;
int64 Get(vector<pair<int64, int64>> &data, int p, int k) {
    if (k == 0) {
        return 0;
    }
    if (p >= data.size()) {
        return 0;
    }
    s.clear();
    for (int i = p; i < data.size(); ++i) {
        int64 r = data[i].first;
        int64 h = data[i].second;
        s.push_back(2 * r * h);
    }
    sort(s.rbegin(), s.rend());
    
    int64 res = 0;
    for (int i = 0; i < s.size(); ++i) {
        if (k == 0) break;
        res += s[i];
        --k;
        
    }
    return res;
}

int main(int argc, const char  * argv[]) {
    std::ios::sync_with_stdio(false);
    
    ifstream cin("/Users/artem/ACMGeneral/ACMGeneral/in.txt");
    ofstream cout("/Users/artem/ACMGeneral/ACMGeneral/out.txt");
    int T;
    cin >> T;
    
    for (int t = 0; t < T; ++t) {
        std::cout << t << endl;
        int n, m;
        cin >> n >> m;
        vector<pair<pair<int, int>, bool>> data;
        int leave_b = 720;
        for (int i = 0; i < n; ++i) {
            int x1, x2;
            cin >> x1 >> x2;
            data.push_back({{x1, x2}, true});
            leave_b -= x2 - x1;
        }
        
        int leave_a = 720;
        for (int i = 0; i < m; ++i) {
            int x1, x2;
            cin >> x1 >> x2;
            data.push_back({{x1, x2}, false});
            leave_a -= x2 - x1;
        }
        if (n + m <= 1) {
            cout << "Case #" << t + 1 << ": " << 2 << endl;
            continue;
        }
        sort(data.begin(), data.end());
        data.push_back(data[0]);
        data.back().first.first += 720 * 2;
        data.back().first.second += 720 * 2;
        
        int res = 0;
        vector<pair<int, pair<int, int>>> b_intervals;
        vector<pair<int, pair<int, int>>> a_intervals;
        for (int i = 0; i < data.size() - 1; ++i) {
            int x1 = data[i].first.second;
            int x2 = data[i + 1].first.first;
            int d = x2 - x1;
            if (data[i].second == data[i + 1].second) {
                
                if (data[i].second) {
                    b_intervals.push_back({d, {x1, x2}});
                }
                else {
                    a_intervals.push_back({d, {x1, x2}});
                }
            }
            else {
                ++res;
            }
        }
        sort(b_intervals.begin(), b_intervals.end());
        sort(a_intervals.begin(), a_intervals.end());
        for (int i = 0; i < b_intervals.size(); ++i) {
            int x1 = b_intervals[i].second.first;
            int x2 = b_intervals[i].second.second;
            int d = x2 - x1;
            assert(d == b_intervals[i].first);
            if (d > leave_b) {
                if (leave_b > 0) {
                    d -= leave_b;
                    leave_b = 0;
                }
                leave_a -= d;
                assert(leave_a >= 0);
                res += 2;
            }
            else {
                leave_b -= d;
            }
        }
        
        for (int i = 0; i < a_intervals.size(); ++i) {
            int x1 = a_intervals[i].second.first;
            int x2 = a_intervals[i].second.second;
            int d = x2 - x1;
            assert(d == a_intervals[i].first);
            if (d > leave_a) {
                if (leave_a > 0) {
                    d -= leave_a;
                    leave_a = 0;
                }
                leave_b -= d;
                assert(leave_b >= 0);
                res += 2;
            }
            else {
                leave_a -= d;
            }
        }
        assert(res >= 2);
        cout << "Case #" << t + 1 << ": " << res << endl;
    }
    return 0;
}
