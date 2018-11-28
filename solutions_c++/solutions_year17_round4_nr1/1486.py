#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
int kase,n,p,cnt[4],t;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out2.txt","w",stdout);
    scanf("%d",&kase);
    for (int cas=1;cas<=kase;++cas) {
        memset(cnt,0,sizeof cnt);
        scanf("%d%d",&n,&p);
        int res=0;
        for (int i=0;i<n;++i) {
            scanf("%d",&t);
            if (t%p==0) {
                ++res;
                continue;
            }
            ++cnt[t%p];
        }
        printf("Case #%d: ",cas);
        if (p==2) {
            res+=(cnt[1]+1)/2;
            printf("%d\n",res);
            continue;
        }
        if (p==3) {
            res+=min(cnt[1],cnt[2])+((max(cnt[2],cnt[1])-min(cnt[2],cnt[1]))+2)/3;
            printf("%d\n",res);
            continue;
        }
        while (cnt[1]>0&&cnt[3]>0) {
            --cnt[1];
            --cnt[3];
            ++res;
        }
        while (cnt[1]>=2&&cnt[2]>0) {
            --cnt[2];
            cnt[1]-=2;
            ++res;
        }
        while (cnt[3]>=2&&cnt[2]>0) {
            --cnt[2];
            cnt[3]-=2;
            ++res;
        }
        while (cnt[2]>=2) {
            ++res;
            cnt[2]-=2;
        }
        while (cnt[3]>=4) {
            cnt[3]-=4;
            ++res;
        }
        while (cnt[1]>=4) {
            cnt[1]-=4;
            ++res;
        }
        if (cnt[1]+cnt[2]+cnt[3]>0)
            ++res;
        printf("%d\n",res);
    }
    return 0;
}
