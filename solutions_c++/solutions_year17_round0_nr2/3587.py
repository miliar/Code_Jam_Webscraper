#include <bits/stdc++.h>
using namespace std;

int digs[20];
long long memo[20][20][2];
long long powten[20];
long long num;
int t;

long long dp(int curpos, int curdig, int allsame) {

    // 17 1 1

    if(memo[curpos][curdig][allsame] != -1) return memo[curpos][curdig][allsame];
    if(curpos == 19) return curdig;
    long long ans = -1000000000000000000ll;
    if(allsame) {
        if(curdig > digs[curpos + 1]) return memo[curpos][curdig][allsame] = -1000000000000000000ll;
        for(int i=curdig; i<digs[curpos + 1]; i++) {
            ans = max(ans, dp(curpos + 1, i, 0));
        }
        ans = max(ans, dp(curpos + 1, digs[curpos + 1], 1));
    } else {
        for(int i=curdig; i<=9; i++) {
            ans = max(ans, dp(curpos + 1, i, 0));
        }
    }

    return memo[curpos][curdig][allsame] = curdig * powten[19 - curpos] + ans;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    cin >> t;

    powten[0] = 1;
    for(int i=1; i<20; i++) powten[i] = powten[i - 1] * 10;

    for(int caseno = 1; caseno <= t; caseno ++){
        cin >> num;

        memset(memo, -1, sizeof(memo));
        memset(digs, 0, sizeof(digs));

        for(int i=0; i<=19; i++) {
            digs[i] = num % 10;
            num /= 10;
        }

        reverse(digs, digs + 20);

        long long ans = 0;

        for(int i=0; i<digs[0]; i++) {
            ans = max(ans, dp(0, i, 0));
        }

        ans = max(ans, dp(0, digs[0], 1));

        cout << "Case #" << caseno << ": " << ans << '\n';
    }
}
