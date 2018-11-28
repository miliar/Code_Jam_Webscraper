#include <iostream>
#include <string>
#include <vector>
#include <cmath>
#include <algorithm>
#include <cassert>
#include <map>
#include <utility>

#define FOR(i,n) for(int i=0;i<int(n);++i)

using namespace std;

using ull = unsigned long long;

void test() {
    ull n, k; cin >> n >> k;
    map<ull, ull> m;
    m.emplace(n, 1);
    
    ull cnt = 0;
    ull n_=n, k_=1;
    while ( cnt < k) {
        tie(n_,k_) = *m.rbegin(); m.erase(--m.end());
        m[ (n_-1)/2 ] += k_;
        m[ (n_)/2   ] += k_;
        cnt += k_;
        //cout << "~" << (n_)/2 << " " << (n_-1)/2 << " >"  << cnt << endl;
    }
    cout << (n_)/2 << ' ' << (n_-1)/2 << endl;
}

int main() {
    
    int tn; cin >> tn;
    FOR (t, tn) {
        cout << "Case #" << t+1 << ": ";
        test();
    }
    
    return 0;
}
