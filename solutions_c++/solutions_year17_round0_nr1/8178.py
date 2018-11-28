#include<bits/stdc++.h>
using namespace std;

char str[1005];

int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T, ca = 0;
    scanf("%d",&T);
    while(T--){
        int k;
        scanf("%s%d",str+1,&k);
        int len = strlen(str+1);
        int ans = 0;
        bool flag = 0;
        for(int i = 1; i <= len ;++i){
            if(str[i] == '-'){
                ans++;
                if(i+k-1 > len){
                    flag = 1;
                    break;
                }
                for(int j = i; j <= i+k-1; ++j){
                    if(str[j] == '-') str[j] = '+';
                    else str[j] = '-';
                }
            }
        }
        if(flag)    printf("Case #%d: IMPOSSIBLE\n",++ca);
        else   printf("Case #%d: %d\n",++ca,ans);
    }
    return 0;
}
