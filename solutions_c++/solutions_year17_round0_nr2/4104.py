/** @xigua */
#include<cstdio>
#include<cmath>
#include<iostream>
#include<algorithm>
#include<vector>
#include<stack>
#include<cstring>
#include<queue>
#include<set>
#include<string>
#include<map>
#include<climits>
#define PI acos(-1)
using namespace std;
typedef long long ll;
typedef double db;
const int maxn = 2e2 + 5;
const int mod = 1e9 + 7;
const int INF = 1e8 + 5;
const ll inf = 1e15 + 5;
const db eps = 1e-6;

void solve() {
    char n[25];

    cin >> n;
    int len = strlen(n);
   // cout << n << ' ' << len << endl;
    int flag = 1;
    /*for (int i = 0; i < len; i++)
        if (n[i] == '0') flag = 0;
    if (!flag) {
        for (int i = 1; i < len; i++)
            cout << '9';
        cout << endl;
    }
    else {
        ll ans = 0, xx = 1, minn = 10;
        for (int i = len-1; i >= 0; i--) {
            minn = min(minn, (ll)n[i] - '0');
            ans += minn * xx;
            xx *= 10;
        }
        cout << ans << endl;
    }*/
    int ans[25]; int minn = n[len-1] - '0';
    ans[len-1] = minn;
    for (int i = len-2; i >= 0; i--) {
        if (n[i] - '0' <= minn) {
            minn = n[i] - '0';
            ans[i] = minn;
        }
        else {
            for (int j = i + 1; j < len; j++)
                ans[j] = 9;
            ans[i] = n[i] - 1 - '0';
            minn = ans[i];
        }
    }
    flag = 0;
    for (int i = 0; i < len; i++) {
        if (ans[i]) flag = 1;
        if (flag) cout << ans[i];
    }
    cout << endl;
}

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int t = 1, cas = 1;
    cin >> t;
    //init();
    while(t--) {
        printf("Case #%d: ", cas++);
        solve();
    }
    return 0;
}
