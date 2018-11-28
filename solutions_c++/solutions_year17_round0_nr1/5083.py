#include <bitset>
#include <vector>
#include <iostream>
#include <cstdio>
using namespace std;

bitset<1001> cakes;
bitset<1001> spat;
int s, k;

int main() {
    int t; cin >> t;
    for(int tc = 1; tc <= t; ++tc) {
        string cakesStr; cin >> cakesStr;
        s = cakesStr.size();
        cin >> k;

        cakes.reset();
        spat.reset();
        for(int i = 0; i < s; ++i) if(cakesStr[i] == '+') cakes.set(i);
        for(int i = 0; i < k; ++i) spat.set(i);
        int count = 0;
        for(int left = 0; left+k-1 < s; ++left) {
            // cout << cakes.to_string().substr(1000-s,s) << endl;
            // cout << spat.to_string().substr(1000-s,s) << endl << endl;
            if(!cakes.test(left)) {
                cakes ^= spat;
                ++count;
            }
            spat <<= 1;
        }
        // cout << cakes.to_string().substr(1000-s,s) << endl;
        // cout << spat.to_string().substr(1000-s,s) << endl << endl;

        printf("Case #%d: ", tc);
        if(cakes.count() != s) cout << "IMPOSSIBLE" << endl;
        else cout << count << endl;
    }

    return 0;
}
