#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#define PI acos(-1.0)
#define EPS 1e-6

using namespace std;

int dcmp(double x) { return x < -EPS ? -x : x > EPS; }

int N, P;
int cnt[5];

void solve() {
    int n, ans = 0;
    memset(cnt,0,sizeof(cnt));
    scanf("%d%d",&N,&P);
    for (int i = 0; i < N; ++i) {
        scanf("%d",&n);
        ++cnt[n%P];
    }
    if (P == 2) { /// cnt[0] and cnt[1]
        ans += cnt[0];
        ans += (cnt[1]+1)/2;
    }
    else if (P == 3) { /// cnt[0] and cnt[1] and cnt[2]
        ans += cnt[0];
        int min12 = min(cnt[1],cnt[2]);
        ans += min12;
        if (cnt[1] != cnt[2]) {
            int left = max(cnt[1],cnt[2]) - min12;
            ans += (left+2)/3;
        }
    }
    else if (P == 4) {
        ans += cnt[0];
        ans += (cnt[2])/2;
        cnt[2] %= 2; /// cnt[2] = 0 or 1
        int min13 = min(cnt[1],cnt[3]);
        ans += min13;
        cnt[1] -= min13;
        cnt[3] -= min13;
        if (cnt[1] != 0) {
            if (cnt[2] != 0 && cnt[1] >= 2) { /// 2 1 1 match
                ans += 1;
                cnt[1] -= 2;
            }
            ans += (cnt[1]+3)/4;
        }
        else if (cnt[3] != 0) {
            if (cnt[2] != 0 && cnt[3] >= 2) { /// 2 3 3 match
                ans += 1;
                cnt[3] -= 2;
            }
            ans += (cnt[3]+3)/4;
        }
        else { /// cnt[1] = cnt[3] = 0
            if ( cnt[2] != 0)
                ans += 1;
        }
    }
    else {
        printf("[ERROR]!\n");
    }
    printf("%d\n",ans);
}

int main() {
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int test;
    scanf("%d",&test);
    for (int t = 1; t <= test; ++t) {
        printf("Case #%d: ",t);
        solve();
    }
    return 0;
}
