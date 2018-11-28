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
        int n, k;
        cin >> n >> k;
        long double u;
        cin >> u;
        vector<long double> data(n);
        map<long double, int> s;
        for (int i = 0; i < n; ++i) {
            cin >> data[i];
            ++s[data[i]];
        }
        while (true) {
            if (s.size() == 1) {
                pair<long double, int> c = *s.begin();
                long double a = u / c.second;
                c.first += a;
                s.erase(s.begin());
                s.insert(c);
                break;
            }
            pair<long double, int> c = *s.begin();
            pair<long double, int> c2 = *(++s.begin());
            s.erase(s.begin());
            long double d = c2.first - c.first;
            assert(d >= 0);
            long double need = d * c.second;
            if (need <= u) {
                u -= need;
                s[c2.first] += c.second;
            }
            else {
                long double a = u / c.second;
                c.first += a;
                s.insert(c);
                break;
            }
        }
        
        assert(s.size() > 0);
        auto c = *s.begin();
        if (s.size() == 1) assert(c.second == n);
        
        long double one = 1.0;
        long double res = 1.0;
        for (auto i = s.begin(); i != s.end(); ++i) {
            res *= pow(min(i->first, one),  i->second);
        }
        cout << "Case #" << t + 1 << ": " << setprecision(12) << fixed << res << endl;
    }
    return 0;
}
