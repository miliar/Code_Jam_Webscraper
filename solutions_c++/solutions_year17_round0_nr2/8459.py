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



ll solve (){
    string ip;
    cin >> ip;
    int n = ip.length();
    int i;
    while(true) {
        for(i = 0; i < n - 1; i++) {
            if(ip[i] > ip[i + 1]) {
                break;
            }
        }
        if(i == n - 1) {
            break;
        }
        else {
            ip[i]--;
            for(int j = i + 1; j < n; j++) {
                ip[j] = '9';
            }
        }
    }
    return stoll(ip);

}

int main() {
   ios_base::sync_with_stdio(false);
   if(!debug) {
        freopen("large.in", "r", stdin);
        freopen("large.out", "w", stdout);
    }
    int t;
    cin >> t;
    int i;
    for(i = 1; i <= t; i++) {
        cout << "Case #" << i << ": ";
        ll sl = solve();

        cout << sl << '\n';

        cerr << "Case " << i << '\n';
    }
    return 0;
}
