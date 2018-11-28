#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
using namespace std;

int main() {
    freopen("/Users/zty/Downloads/B-small-attempt0.in","r",stdin);
    freopen("/Users/zty/Downloads/B-small-attempt0.txt","w",stdout);

    const int maxn=60;
    int N,P;
    int que[maxn][maxn];
    int tmp[maxn];
    int val[maxn];
    int cas;
    scanf("%d",&cas);
    for(int t=1;t<=cas;t++) {
        scanf("%d%d",&N,&P);
        for(int i = 1;i <= N;i++) {
            scanf("%d",&val[i]);
        }
        for(int i = 1;i <= N;i++) {
            for(int j = 1;j <= P;j++) {
                scanf("%d",&que[i][j]);
            }
            sort(que[i]+1,que[i]+1+P);
        }
        fill(tmp,tmp+maxn,0);
        int ans = 0;
        for(int j = 1;j <= 1e6+5;j++) {
            bool f = false;
            for(int i = 1;i <= N;i++) {
                long long d = ceil(0.9 * j * val[i]);
                while (tmp[i] <= P && que[i][tmp[i]] < d) {
                    tmp[i]++;
                }
                d = floor(1.1 * j * val[i]);
                if(que[i][tmp[i]] > d || tmp[i] > P) {
                    f = true;
                }
            }
            if(!f) {
                ans++;
                j = j - 1;
                for(int i = 1;i <= N;i++)
                    tmp[i]++;
            }
            f = true;
            for(int i = 1;i <= N;i++) {
                if(tmp[i] > P) {
                    f = false;
                }
            }
            if(!f) {
                break;
            }
        }
        printf("Case #%d: %d\n",t,ans);
    }
    return 0;
}