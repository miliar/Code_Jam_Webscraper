#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
#include <cassert>
#include <map>
#include <unordered_map>
#include <utility>
#include <iomanip>
#include <cmath>
#include <cstdio>

#define FOR(i,n) for(ull i=0;i<ull(n);++i)

using namespace std;

using ull = unsigned long long;

void test() {
    
    int n, p; cin >> n >> p;
    int gc[5]; FOR(i, 5) gc[i] = 0;
    FOR (i, n) {
        int g; cin >> g;
        gc[ g % p ]++;
    }
    
    int res = 0;
    if (p == 2) {
        res =  gc[0]+gc[1]/2;
        
        if (gc[1] % 2) res ++;
    } else if (p == 3) {
        int x = min(gc[1],gc[2]);
        gc[1] -=x; gc[2] -=x;
        res = gc[0]+x+gc[1]/3+gc[2]/3;
        
        if (gc[1]%3 || gc[2]%3) res ++;
    } else if (p == 4) {
        
        res = gc[0]+gc[2]/2;
        
        int x = min(gc[1], gc[3]);
        gc[1] -=x; gc[3] -=x;
        res += x;
        
        res += gc[1]/4 + gc[3]/4;
        
        int rem = gc[1]%4 + gc[2]%4 + gc[3]%4;
        if (gc[2]%2 == 1) {
            if (gc[1] % 4 >= 2) {
                res ++; // 2 + 1 + 1 = 4
                rem -= 3;
            } else if (gc[3] % 4 >= 2) {
                res ++; // 2 + 3 + 3 = 8
                rem -= 3;
            }
        }
        
        if (rem) res++;
        
    } else {
        assert(false);
    }

    cout << res << endl;
//    else cout << res+1 << endl;
    
}

int main() {
    
    ull tn; cin >> tn;
    FOR (t, tn) {
        cerr << t << endl;
        cout << "Case #" << t+1 << ": ";
        test();
    }
    
    return 0;
}
