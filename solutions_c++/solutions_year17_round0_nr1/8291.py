#include <bits/stdc++.h>

using namespace std;

const int INF = 0x3f3f3f3f;
int vis[3000];
int dp[3000];

int t;
char s[12], k;
int f = 0;

int main() {
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &t);
    while(t--) {
        scanf("%s%d", &s, &k);
        int sta = 0;
        int len = strlen(s);
        for(int i = 0; i < len; i++) {
            if(s[i] == '+')
                sta |= (1 << i);
        }
        memset(dp, INF, sizeof dp);
        memset(vis, 0, sizeof vis);
        dp[sta] = 0;
        queue<int> Q;
        Q.push(sta);
        while(!Q.empty()) {
            int tmp = Q.front();
            Q.pop();
            if(vis[tmp]) continue;
            vis[tmp] = 1;
            //cout<<tmp<<" tmp "<<endl;
            for(int i = 0; i <= len - k; i++) {
                int pp = tmp;
                //bitset<8> x, y;
                //x = pp;
                for(int j = i; j < i + k; j++) {
                    pp ^= (1 << j);
                }
                //y = pp;
                //cout<<x<<" to "<<y<<endl;
                if(!vis[pp])
                    dp[pp] = dp[tmp] + 1, Q.push(pp);
            }
        }
        printf("Case #%d: ", ++f);
        if(dp[(1<<len)-1] == INF)
            puts("IMPOSSIBLE");
        else
            printf("%d\n", dp[(1<<len)-1]);
    }
    return 0;
}
