#include <iostream>
#include <cstdio>
#include <string>
#include <algorithm>
#include <unordered_set>
#include <cmath>
#include <set>
#include <unordered_map>
#include <map>
#include <functional>
#include <iomanip>
#include <vector>
#include <utility>

using namespace std;

typedef long long ll;

const bool debug = false;

unordered_map<string, ll> mp;
unordered_set<string> curr;
int k;
ll dp(string str) {
    auto it = mp.find(str);


    if(it != mp.end()) {
        return it->second;
    }

    else {
        int ct = 0;
        int i;
        int n = str.length();
        for(i = 0; i < n; i++) {
            if(str[i] == '-') {
                break;
            }
        }
        if(i == n) {
            return 0;
        }
        else {
            ll c_min = 1e18;
            for(int i = 0; i <= n - k; i++) {
                string cp = str;
                for(int j = i; j < i + k; j++) {
                    if(cp[j] == '+') {
                        cp[j] = '-';
                    }
                    else {
                        cp[j] = '+';
                    }
                }
                if(curr.find(cp) == curr.end()) {
                    curr.insert(cp);
                    ll rec = dp(cp);
                    if(rec != -1) {
                        c_min = min(c_min, rec + 1);
                    }
                    curr.erase(cp);
                }
            }
            if(c_min == 1e18)
            {
                c_min = -1;
            }
            mp[str] = c_min;
            return c_min;
        }


    }

}

ll solve (){
    mp.clear();
    curr.clear();
    string str;
    cin >> str >> k;
    return dp(str);

}

int main() {
   ios_base::sync_with_stdio(false);
   if(!debug) {
        freopen("small.in", "r", stdin);
        freopen("small.out", "w", stdout);
    }
    int t;
    cin >> t;
    int i;
    for(i = 1; i <= t; i++) {
        cout << "Case #" << i << ": ";
        int sl = solve();
        if(sl == -1) {
            cout << "IMPOSSIBLE\n";
        }
        else {
            cout << sl << '\n';
        }
        cerr << "Case " << i << '\n';
    }
    return 0;
}
