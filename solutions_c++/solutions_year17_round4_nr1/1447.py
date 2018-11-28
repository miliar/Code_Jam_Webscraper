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


int main(int argc, const char  * argv[]) {
    std::ios::sync_with_stdio(false);
    
    ifstream cin("/Users/artem/ACMGeneral/ACMGeneral/in.txt");
    ofstream cout("/Users/artem/ACMGeneral/ACMGeneral/out.txt");
    int T;
    cin >> T;
    
    for (int t = 0; t < T; ++t) {
        std::cout << t << endl;
        int n, p;
        cin >> n >> p;
        vector<int> r(p);
        for (int i = 0; i < n; ++i) {
            int v;
            cin >> v;
            ++r[v % p];
        }
        int res = r[0];
        if (p == 2) {
            res += r[1] / 2;
            res += r[1] % 2;
        }
        if (p == 3) {
            int mi = min(r[1], r[2]);
            res += mi;
            r[1] -= mi;
            r[2] -= mi;
            int z = r[1] + r[2];
            if (z > 0) {
                res += 1 + (z - 1) / 3;
            }
        }
        if (p == 4) {
            int mi = min(r[1], r[3]);
            res += mi;
            r[1] -= mi;
            r[3] -= mi;
            int z = r[1] + r[3];
            
            res += r[2] / 2;
            int y = r[2] % 2;
            
            if (y == 1) {
                if (z >= 2) {
                    z -= 2;
                    res += 1;
                }
                else {
                    z = 0;
                    res += 1;
                }
            }
            if (z > 0) {
                res += 1 + (z - 1)/ 4;
            }
        }
        assert(res <= n);
        cout << "Case #" << t + 1 << ": " << res << endl;
    }
    return 0;
}
