/*
 * (c) fushar (Ashar Fuadi)
*/

#include <bits/stdc++.h>
using namespace std;

#define REP(i,n) for (int i = 0; i < n; i++)
#define RESET(c,v) memset(c, v, sizeof c)

typedef long long ll;

int T;
int N, P;
int total, cnt[4];
int dp[2000001];

int curState[4];

void extractState(int state) {
    for (int i = 1; i < P; i++) {
        curState[i] = state%(N+1);
        state /= (N+1);
    }
}

int computeState() {
    int state = 0;
    for (int i = P-1; i >= 1; i--) {
        state = state * (N+1) + curState[i];
    }
    return state;
}

int main() {
    scanf("%d", &T);
    REP(tc, T) {
        scanf("%d %d", &N, &P);
        RESET(cnt, 0);
        total = 0;

        REP(i, N) {
            int g;
            scanf("%d", &g);
            g %= P;
            total += g;
            cnt[g]++;
        }
        total %= P;

        RESET(dp, 0);

        int maxState = 1;
        REP(i, P-1) {
            maxState *= (N+1);
        }

        for (int state = 1; state <= maxState; state++) {
            extractState(state);
            int curTotal = 0;
            for (int i = 1; i < P; i++) {
                curTotal += i*curState[i];
            }

            int leftover = (total - (curTotal%P) + P) % P;
            int addition = leftover ? 0 : 1;

            for (int i = 1; i < P; i++) {
                if (!curState[i]) continue;
                curState[i]--;
                int nextState = computeState();
                dp[state] = max(dp[state], addition + dp[nextState]);
                curState[i]++;
            }
        }

        for (int i = 1; i < P; i++) {
            curState[i] = cnt[i];
        }

        printf("Case #%d: %d\n", tc+1, cnt[0] + dp[computeState()]);
    }
}
