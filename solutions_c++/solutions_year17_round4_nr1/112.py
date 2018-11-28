#include <stdio.h>
#include <stdlib.h>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <vector>
#include <stack>
#include <deque>
#include <queue>
#include <set>
#include <string.h>
#define pb push_back
#define sz(V) ((int)(V).size())
#define allv(V) ((V).begin()),((V).end())
#define befv(V) ((V)[(sz(V)-2)])
#define upmin(ans,ansx) (ans)=min((ans),(ansx))
#define upmax(ans,ansx) (ans)=max((ans),(ansx))
using namespace std;
typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;

int cnt[5];
int T, N, P, Ans;

int main() {
    scanf("%d", &T); for(int t_i = 1; t_i <= T; t_i++) {
        int lcnt = 0; Ans = 0; fill(cnt, cnt+5, 0);
        for(scanf("%d%d", &N, &P); N--;) {
            int c; scanf("%d", &c);
            cnt[c%P]++;
        }
        Ans += cnt[0];
        if(2 == P) {
            cnt[1]++;
            Ans += cnt[1] / 2;
        } else if(3 == P) {
            int tmp = min(cnt[1], cnt[2]);
            Ans += tmp;
            cnt[1] -= tmp; cnt[2] -= tmp;
            cnt[1] += 2; cnt[2] += 2;
            Ans += cnt[1]/3 + cnt[2]/3;
        } else {
            Ans += cnt[2] / 2; cnt[2] = cnt[2]&1;
            int tmp = min(cnt[1], cnt[3]);
            Ans += tmp; cnt[1] -= tmp; cnt[3] -= tmp;
            if(!cnt[2]) {
                cnt[1] += 3; cnt[3] += 3;
                Ans += cnt[1]/4 + cnt[3]/4;
            } else {
                if(cnt[1]) {
                    if(2 <= cnt[1]) { Ans++; cnt[1] -= 2; cnt[2]--; }
                    Ans += cnt[1] / 4; cnt[1] %= 4;
                    if(cnt[1] && cnt[2]) Ans++;
                } else {
                    if(2 <= cnt[3]) { Ans++; cnt[3] -= 2; cnt[2]--; }
                    Ans += cnt[3] / 4; cnt[3] %= 4;
                    if(cnt[2] && cnt[3]) Ans++;
                }
            }
        }
        printf("Case #%d: %d\n", t_i, Ans);
    }
    return 0;
}
