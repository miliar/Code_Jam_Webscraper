#include <bits/stdc++.h>

using namespace std;

char s[2500];
int a[2500],cnt[2500];

int main(){
    freopen("out.out","w",stdout);
    int T,k;
    scanf("%d",&T);
    for (int cas=1;cas<=T;cas++){
        scanf("%s%d",s,&k);
        int n=strlen(s);
        memset(cnt,0,sizeof cnt);
        for (int i=0;i<n;i++){
            a[i]=(s[i]=='+')?1:0;
        }
        int ans=0,i;
        for (i=0;i+k<=n;i++){
            if (cnt[i]&1) a[i]^=1;
            if (0==a[i]){
                cnt[i]++;
                cnt[i+k]--;
                ans++;
            }
            cnt[i+1]+=cnt[i];
        }
        bool succ=true;
        for (;i<n;i++){
            if (cnt[i]&1) a[i]^=1;
            if (!a[i]) succ=false;
            cnt[i+1]+=cnt[i];
        }
        printf("Case #%d: ",cas);
        if (succ) printf("%d\n",ans);
        else puts("IMPOSSIBLE");
    }
    return 0;
}
