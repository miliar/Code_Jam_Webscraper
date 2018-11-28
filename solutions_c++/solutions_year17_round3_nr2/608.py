#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <vector>
#include <set>

using namespace std;

#define print(x) cout << x << endl
#define input(x) cin >> x

const int INF = 0x3f3f3f3f;
const int HOUR24 = 24 * 60;
const int HOUR12 = 12 * 60;
// const int HOUR12 = 2;
// const int HOUR24 = 4;
const int SIZE = HOUR24 + 1;

int dp[2][3][3][HOUR12 + 1];
int minutes[SIZE];

struct Slot {
    int st;
    int end;
    int nr;

    int length() const {
        return end - st;
    }
};

int solve() {
    int cur = 0;
    memset(dp, INF, sizeof(dp));
    if (minutes[0] != 1) {
        dp[0][1][1][1] = 0;
    }
    if (minutes[0] != 2) {
        dp[0][2][2][0] = 0;
    }

    for (int i = 1; i < HOUR24; i++) {
        int next = cur ^ 1;
        memset(dp[next], INF, sizeof(dp[next]));
        
        int flag = minutes[i];
        
        for (int j = 0; j <= i; j++) {
            int ta = j;
            int tb = i - j;
            if (ta > HOUR12 || tb > HOUR12) {
                continue;
            }
    
            if (flag != 1 && ta + 1 <= HOUR12) {
                dp[next][1][1][ta + 1] = min(dp[next][1][1][ta + 1], dp[cur][1][1][ta]);
                dp[next][1][1][ta + 1] = min(dp[next][1][1][ta + 1], dp[cur][2][1][ta] + 1);
                
                dp[next][1][2][ta + 1] = min(dp[next][1][2][ta + 1], dp[cur][1][2][ta]);
                dp[next][1][2][ta + 1] = min(dp[next][1][2][ta + 1], dp[cur][2][2][ta] + 1);
            }
            if (flag != 2 && tb + 1 <= HOUR12) {
                dp[next][2][1][ta] = min(dp[next][2][1][ta], dp[cur][2][1][ta]);
                dp[next][2][1][ta] = min(dp[next][2][1][ta], dp[cur][1][1][ta] + 1);
                
                dp[next][2][2][ta] = min(dp[next][2][2][ta], dp[cur][2][2][ta]);
                dp[next][2][2][ta] = min(dp[next][2][2][ta], dp[cur][1][2][ta] + 1);
            }
        }
        cur = next;
    }
    
    int ans = INF;
    ans = min(ans, dp[cur][1][1][HOUR12]);
    ans = min(ans, dp[cur][2][2][HOUR12]);
    ans = min(ans, dp[cur][2][1][HOUR12] + 1);
    ans = min(ans, dp[cur][1][2][HOUR12] + 1);
    return ans;
}

int main() {
    // freopen("b.txt", "r", stdin);
    int T;
    input(T);
    for (int case_ = 0; case_ < T; case_++) {
        printf("Case #%d: ", case_ + 1);
        int a, b;

        input(a >> b);
        vector<Slot> slots(a + b);
        
        memset(minutes, 0, sizeof(minutes));

        int cur = 0;

        for (int i = 0; i < a; i++) {
            scanf("%d%d", &slots[cur].st, &slots[cur].end);
            slots[cur].nr = 1;
            for (int j = slots[cur].st; j < slots[cur].end; j++) {
                minutes[j] = 1;
            }
            cur++;
        }

        for (int i = 0; i < b; i++) {
            scanf("%d%d", &slots[cur].st, &slots[cur].end);
            slots[cur].nr = 2;
            for (int j = slots[cur].st; j < slots[cur].end; j++) {
                minutes[j] = 2;
            }
            cur++;
        }


        print(solve());
    }

    return 0;

}
