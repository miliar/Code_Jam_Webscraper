#include <iostream>
#include <map>

using std::map;
using std::cin;
using std::cout;
using std::endl;
using std::string;

typedef long long Long;

void solve() {
    Long n, k;
    cin >> n >> k;
    map <Long, Long> s;
    s[n] = 1;
    Long l = 0, r = 0;
    while (k > 0) { 
        auto pr = *s.rbegin();
        Long d = pr.first, v = pr.second; 
        s.erase(s.find(d));
        l = (d - 1) / 2, r = d / 2;
        s[l] += v;
        s[r] += v;
        k -= v;
    }
    cout << r << " " << l << endl;
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; ++i) {
        cout << "Case #" << i + 1 << ": ";
        solve();
    }
    return 0;
}
