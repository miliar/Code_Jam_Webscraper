#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <memory>
#include <utility>

using namespace std;

// map<pair<long long, long long>, pair<long long, long long>> m;

pair<long long, long long> find(long long n, long long k) {
    // pair<long long, long long> in(n, k);
    // if(m.count(in)) { return m[in]; }
    long long at = n / 2;
    long long y = n - at - 1;
    long long z = at - 1;
    if(k == 1) {
        return pair<long long, long long>(y, z);
    }
    long long newk = k / 2;
    // pair<long long, long long> out;
    if(k % 2 == 0) {
        // out = find(y+1, newk);
        return find(y + 1, newk);
    } else {
        // out = find(z+1, newk);
        return find(z + 1, newk);
    }
    // m[in] = out;
    // return out;
}

int main() {
    int t;
    cin >> t;
    for(int ts = 1; ts <= t; ++ts) {
        cout << "Case #" << ts << ": ";
        
        long long n;
        long long k;
        
        cin >> n >> k;
        ++n;
        pair<long long, long long> res = find(n, k);
        cout << res.first << ' ' << res.second << endl;
    }
}
