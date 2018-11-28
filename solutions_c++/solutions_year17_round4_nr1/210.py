#include <iostream>
#include <string.h>
#include <stdio.h>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>
#define maxn 100010
using namespace std;
int cnt[4];
int solve(int n){
    if(n==1){
        int num = cnt[0];
        cnt[0] = 0;
        return num;
    }
}
int fabs(int x){
    return x<0?-x:x;
}
int main()
{
    freopen("ddl.in","r",stdin);
    freopen("out.txt","w+",stdout);
    int ncase,T=0;
    cin >> ncase;
    while(ncase--) {
        printf("Case #%d: ",++T);
        int n,p;
        memset(cnt,0,sizeof(cnt));
        scanf("%d%d",&n,&p);
        for(int i=0;i<n;i++){
            int x;
            scanf("%d",&x);
            cnt[x%p]++;
        }
        int ans = 0;
        if(p==2){
            ans = cnt[0] + (cnt[1] + 1)/2;
        }
        else if(p == 3) {
            ans = cnt[0] + min(cnt[1], cnt[2]);
            int left = fabs(cnt[1] - cnt[2]);
            ans += (left + 2) / 3;
        }
        else if(p == 4) {
            ans = cnt[0] + cnt[2] / 2 + min(cnt[1], cnt[3]);
            int left = fabs(cnt[1] - cnt[3]);
            if (cnt[2] % 2 == 1) {
                left += 2;
            }
            ans += (left + 3) / 4;
        }
        printf("%d\n",ans);
    }
    return 0;
}
