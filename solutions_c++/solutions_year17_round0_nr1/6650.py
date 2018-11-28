#include<stdio.h>
#include<string.h>
int tt, n, psize;
bool imp;
char s[1010];
int main(){
    freopen("A-large.in", "r", stdin);
    freopen("outputl.txt", "w", stdout);
    scanf("%d", &tt);
    for (int test = 1; test <= tt; test++){
        printf("Case #%d: ", test);
        scanf("%s", s);
        scanf("%d",  &psize);
        n = strlen(s);
        int cnt=0;
        for(int i=0;i<=n-psize;i++){
            if(s[i]=='+')
                continue;
            else{
                for(int j=i;j<psize+i;j++){
                    if(s[j]=='-')
                        s[j]='+';
                    else
                        s[j]='-';
                }
                cnt++;
            }
        }
        imp=true;
        for(int i=n-psize+1;i<n;i++){
            if(s[i]=='-'){
                imp=false;
                break;
                }
        }
        if(imp==true)
            printf("%d\n",cnt);
        else
            printf("IMPOSSIBLE\n");
    }
    return 0;
}
