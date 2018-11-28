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
#define ROF(i,n) for(int i=int(n)-1;i>=0;--i)

using namespace std;

using ull = unsigned long long;

void test() {
    
    int n,c,m; cin >> n >> c >> m;
    
    vector<int> cu(1111, 0), ro(1111, 0);
    int mx_cu = 0;
    FOR (i, m) {
        int p, z; cin >> p >> z; p--; z--;
        cu[z]++;
        ro[p]++;
        mx_cu = max(mx_cu, cu[z]);
    }
    
    int res = 0;
    int k = mx_cu;
    for (;; ++k) {
        res = 0;
        
        int free = 0;
        FOR (i, n) {
            if (ro[i] <= k) {
                free += k - ro[i];
            } else if (ro[i]-k <= free) {
                free -= ro[i]-k;
                res  += ro[i]-k;
            } else {
                // not poss
                goto CONT;
            }
        }
        
        break;
        
    CONT:;
    }
    
//    assert(res > 0);
    
    cout << k << " "<< res << endl;
    
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
