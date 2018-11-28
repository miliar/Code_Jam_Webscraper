#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
#include <cassert>
#include <map>
#include <utility>
#include <iomanip>

#define FOR(i,n) for(int i=0;i<int(n);++i)

using namespace std;

using ull = unsigned long long;

void test() {
    int d,n;
    double t = -1.0;
    cin >> d >> n;
    FOR (i, n) {
        int k,s; cin >> k >> s;
        t = max(t, double(d-k)/double(s));
    }
    cout << std::setprecision(12) << double(d)/t << endl;
}

int main() {
    
    int tn; cin >> tn;
    FOR (t, tn) {
        cout << "Case #" << t+1 << ": ";
        test();
    }
    
    return 0;
}
