#include <cstdio>
#include <cstdlib>
#include <cstring>

#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>

using namespace std;
typedef long long LL;

int n, p;
int mod[200];

int work() {
    cin >> n >> p;
    for (int i = 0; i < p; i ++) mod[i] = 0;
    for (int i = 0; i < n; i ++) {
        int x; cin >> x; x = x % p;
        mod[x] ++;
    }
    if (p == 2) {
        return mod[0] + mod[1] / 2 + mod[1] % 2;
    }
    if (p == 3) {
        int ans = mod[0];
        int tmp = min(mod[1], mod[2]);
        ans += tmp;
        mod[1] -= tmp;
        mod[2] -= tmp;
        ans += mod[1] / 3  + mod[2] / 3;
        if (mod[1] % 3 > 0 || mod[2] % 3 > 0) ans ++;
        return ans;
    }
    if (p == 4) {
        int ans = mod[0];
        int tmp = min(mod[1], mod[3]);
        ans += tmp;
        mod[1] -= tmp;
        mod[3] -= tmp;
        ans += mod[2] / 2;
        mod[2] = mod[2] % 2;
        if (mod[2] == 0) {
            ans += mod[1] / 4 + mod[3] / 4;
            if (mod[1] % 4 > 0 || mod[3] % 4 > 0) ans ++;
            return ans;
        }
        if (mod[2] == 1) {
            // NOTICE
            if (mod[3] > 0) swap(mod[3], mod[1]);
            if (mod[1] > 0) {
                if (mod[1] >= 2) {
                    ans += 1;
                    mod[1] -= 2;
                    ans += mod[1] / 4;
                    if (mod[1] % 4 > 0) ans ++;
                    return ans;
                }
                else {
                    ans ++;
                    return ans;
                }
            }
            else {
                ans ++;
                return ans;
            }
        }
    }
    return 99999999;
}

int main() {
    int tot; cin >> tot;
    for (int cas = 1; cas <= tot; cas ++) {
        cout << "Case #" << cas << ":";
        cout << ' ' << work() << endl;
    }
    return 0;
}
