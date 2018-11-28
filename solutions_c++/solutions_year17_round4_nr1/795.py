#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
using namespace std;

int n,p,cnt[5];
int dp[105][5];

int main() {
    int tc;
    scanf("%d",&tc);
    for (int t=1; t<=tc; t++) {
        scanf("%d%d",&n,&p);
        memset(cnt,0,sizeof(cnt));
        for (int i=0; i<n; i++) {
            int a;
            scanf("%d",&a);
            cnt[a%p]++;
        }
        printf("Case #%d: ",t);
        int ans,mi,mx;
        if (p == 2) {
            printf("%d\n",cnt[0]+(cnt[1]+1)/2);
        }
        else if (p == 3) {
            ans = cnt[0];
            mi = min(cnt[1],cnt[2]);
            ans += mi; cnt[1] -= mi; cnt[2] -= mi;
            mx = max(cnt[1],cnt[2]);
            ans += (mx+2)/3;
            printf("%d\n",ans);
        }
        else {
            ans = cnt[0];
            ans += cnt[2]/2;
            cnt[2] %= 2;
            mi = min(cnt[1],cnt[3]);
            ans += mi; cnt[1] -= mi; cnt[3] -= mi;
            mx = max(cnt[1],cnt[3]);

            if (cnt[2] == 1) {
                if (mx >= 2) {
                    mx -= 2; cnt[2] = 0;
                    ans++;
                }
                else {
                    mx = 0; cnt[2] = 0;
                    ans++;
                }
            }
            ans += (mx+3)/4;
            printf("%d\n",ans);
        }
    }
	return 0;
}
