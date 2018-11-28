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
        int n, k;
        cin >> n >> k;
        vector<pair<int64, int64>> data(n);
        for (int i = 0; i < n; ++i) {
            cin >> data[i].first >> data[i].second;
        }
        sort(data.rbegin(), data.rend());
        int64 res = 0;
        for (int i = 0; i < n; ++i) {
            int64 r = data[i].first;
            int64 h = data[i].second;
            int64 curr = r * r + 2 * r * h + Get(data, i + 1, k - 1);
            res = max(res, curr);
        }
        cout << "Case #" << t + 1 << ": " << setprecision(12) << fixed <<res * Pi << endl;
    }
    return 0;
}
