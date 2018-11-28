#include <iostream>
#include <cstdio>
#include <string>
using namespace std;

#define rep(i,a,b) for(int i=a;i<b;i++)
string s;    int k;

int proc() {
    int len = s.size();
    int cnt = 0;
    bool flag = 0;
    rep(i, 0, len - k + 1) {
        if (s[i] == '-') {
            cnt++;
            rep(j, i, i + k) {
                s[j] ^= 6;
            }
        }
    }

    rep(i, len - k, len) {
        if (s[i] == '-') {
            flag = 1;
            break;
        }
    }
    if (flag)
        return -1;
    return cnt;
}
int main() {
    ios_base::sync_with_stdio(false); cin.tie(0);
    freopen("A-large.in", "r", stdin);
    int t, ans;
    cin >> t;

    rep(tc, 1, t + 1) {
        cin >> s >> k;
        ans = proc();
        if (ans == -1)
            printf("Case #%d: IMPOSSIBLE\n", tc, ans);
        else
            printf("Case #%d: %d\n", tc, ans);
    }
    return 0;
}
