#include <cstdio>
#include <cstring>
char s[1005];
int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t;
    scanf("%d",&t);
    int k;
    for(int i = 1; i <= t; i++){
        scanf("%s%d",s,&k);
        int len = strlen(s);
        int cnt = 0;
        for(int j = 0; j < len-k+1; j++){
            if(s[j] == '-'){
                for(int l = j; l < j + k; l++){
                    s[l] = s[l] == '-' ? '+' : '-';
                }
                cnt++;
            }
        }
        bool b = true;
        for(int j = 0; j < len; j++){
            if(s[j] == '-')
                b = false;
        }
        if(b)
            printf("Case #%d: %d\n",i,cnt);
        else
            printf("Case #%d: IMPOSSIBLE\n",i);
    }
    return 0;
}
