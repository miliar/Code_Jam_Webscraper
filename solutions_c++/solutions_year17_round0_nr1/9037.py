#include<bits/stdc++.h>
using namespace std;
#define MAXN 2222
char s[MAXN];
int t,n,k,ans;

int main(){
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d ",&t);
    for(int ca=1;ca<=t;ca++){
        scanf("%s %d",s,&k);

        n = strlen(s);
        ans = 0;
        for(int i = 0 ; i+k <= n;i++){
            if(s[i]=='-'){
                for(int j = 0;j<k;j++){
                    if(s[i+j]=='-')s[i+j]='+';
                    else s[i+j] = '-';
                }
                ans ++;
            }
        }
        bool valid = 1;
        for(int i = 0 ; valid && i < n;i++)
            if(s[i]=='-')valid = 0;

        if(valid)printf("Case #%d: %d\n",ca,ans);
        else printf("Case #%d: IMPOSSIBLE\n",ca);
    }
    return 0;
}
