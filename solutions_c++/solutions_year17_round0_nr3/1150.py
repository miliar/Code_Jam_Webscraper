#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <string.h>
#include <stdio.h>
#include <math.h>
#include <queue>
#include <stack>
#include <map>
#include <set>

using namespace std;


const double eps = 1e-8;
const double pi = acos(-1.0);

map<long long, long long> cnt;
set<long long> has;
long long n;

long long calc(long long k) {
    if (!has.count(k)) {
        return 0;
    }
    if (k == n) {
        return cnt[k] = 1;
    }
    if (cnt.count(k)) {
        return cnt[k];
    }

    long long f1 = k * 2LL;
    long long f2 = (k + 1) * 2LL;
    long long f3 = k * 2LL + 1;

    long long sum = (k == 0 ? 0 : calc(f1)) + calc(f2) + 2LL * calc(f3);
    return cnt[k] = sum;
}

void dfs(long long k) {
    if (has.count(k)) {
        return;
    }
    has.insert(k);
    if (k == 0) {
        return;
    }
    if (k & 1) {
        dfs(k / 2LL);
    } else {
        dfs(k / 2LL);
        dfs(k / 2LL - 1);
    }
}

int main() {
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);

    int T;
    cin >> T;

    for (int cas = 1; cas <= T; cas++) {
        long long k;
        cin >> n >> k;
        has.clear();
        cnt.clear();
        dfs(n);
        calc(0);

        long long mx, mi;
        for (map<long long, long long>::reverse_iterator it = cnt.rbegin(); it != cnt.rend(); it++) {
            if (it->second >= k) {
                if ((it->first) & 1) {
                    mx = mi = (it->first) / 2LL;
                } else {
                    mx = (it->first) / 2LL;
                    mi = mx - 1;
                }
                break;
            }
            k -= it->second;
        }

        cout << "Case #" << cas << ": " << mx << " " << mi << endl;
    }
    return 0;
}

