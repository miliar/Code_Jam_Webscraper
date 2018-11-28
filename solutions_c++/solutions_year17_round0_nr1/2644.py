#include <cstdio>
#include <cstring>
char o[1010];
bool u[1010];
int main() {
    int i, j, n, m;
    int t, tc;
    int ans;
    //freopen("/Users/SeoByeongChan/Desktop/input.txt","rt",stdin);
    //freopen("/Users/SeoByeongChan/Desktop/output.txt","w",stdout);
    scanf("%d",&tc);
    for(t=1;t<=tc;t++) {
        char p[13] = {0,};
        ans = 0;
        scanf("%s %d",o, &m);
        n = (int)strlen(o);
        for(i=0;i<=n-m;i++) {
            if(!u[i]) {
                if(o[i] == '+') continue;
                else ans++;
            }
            else {
                if(o[i] == '+') ans++;
                else continue;
            }
            for(j=i;j<i+m;j++) u[j] = !u[j];
        }
        for(i=n-m+1;i<n;i++) {
            if(!u[i]) {
                if(o[i] == '-') break;
            }
            else {
                if(o[i] == '+') break;
            }
        }
        if(i < n) ans = -1;
        for(i=0;i<n;i++) u[i] = false;
        if(ans >= 0) sprintf(p, "%d", ans);
        printf("Case #%d: %s\n",t,ans >= 0 ? p : "IMPOSSIBLE");
    }
    return 0;
}
