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

#define int64 unsigned long long

#include <iostream>

using namespace std;


int main(int argc, const char  * argv[]) {
    std::ios::sync_with_stdio(false);

    ifstream cin("/Users/artem/ACMGeneral/ACMGeneral/in.txt");
    ofstream cout("/Users/artem/ACMGeneral/ACMGeneral/out.txt");
    int T;
    cin >> T;
    
    for (int t = 0; t < T; ++t) {
        int d, n;
        cin >> d >> n;
        vector<long double> k(n), s(n);
        for (int i = 0; i < n; ++i) {
            cin >> k[i] >> s[i];
        }
        long double time = 0;
        for (int i = 0; i < n; ++i) {
            time = max(time, (d - k[i]) / s[i]);
        }
        long double res = d / time;
        cout << "Case #" << t + 1 << ": " << setprecision(16) << res << endl;
    }
    return 0;
}
