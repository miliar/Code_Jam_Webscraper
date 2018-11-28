#include <bits/stdc++.h>

using namespace std;
int a[5];

int main(){
    int T;
    int N;
    freopen("A-small-attempt2.in","r",stdin);
    freopen("A.out","w",stdout);
    scanf("%d",&T);
    int n,p;
    for(int cs = 1;cs <= T;cs++){
        scanf("%d%d",&n,&p);
        memset(a,0,sizeof(a));
        int ans = 0;
        for(int j = 0;j < n;j++){
            int t;
            scanf("%d",&t);
            t %= p;
            a[t]++;
        }
        ans = a[0];
        if(p == 2){
            ans += (a[1]+1)/2;
            printf("Case #%d: %d\n",cs,ans);
        }
        else if(p == 3){
            int t = min(a[1],a[2]);
            ans += t+(max(a[1],a[2])-t)/3;
            if((max(a[1],a[2])-t)%3) ans++;
            printf("Case #%d: %d\n",cs,ans);
        }
    }
    return 0;
}
