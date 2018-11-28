#include <iostream>
#include <cstring>
#include <string>
#include <cmath>
#include <algorithm>
#include <queue>
#include <vector>
#include <climits>
using namespace std;
typedef int64_t ll;

int t;
ll k;

ll core(ll n) {
    string s = to_string(n);
    int l = (int) s.length();
    if (l < 2)
        return n;
    int p = l - 1;
    while (p > 0) {
        if(s[p]<s[p-1]) {
            for (int i = p; i < l; i++)
                s[i] = '9';
            s[p - 1]--;
        }
        p--;
    }
    return stoll(s);
}

int main() {
    //freopen("out.txt", "w", stdout);
    //freopen("in.txt", "r", stdin);
    scanf("%d", &t);
    for (int m = 1; m <= t; m++) {
        scanf("%lld", &k);
        printf("Case #%d: %lld\n", m, core(k));
    }
    return 0;
}