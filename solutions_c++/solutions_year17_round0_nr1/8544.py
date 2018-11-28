#include <iostream>
#include <cstdio>
using namespace std;

int T,n;
char s[1005];

int main()
{
    freopen("A-small-attempt1.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&T);
    for(int q = 1;q<=T;q++){
        char s[1005] = {};
        scanf("%s%d",s,&n);
        int cnt = 0;
        bool flag = true;
        for(int i = 0;i<s[i] != NULL;i++){
            if(flag && s[i] == '-'){
                for(int j = i;j<i+n;j++){
                    if(s[j] == NULL){
                        flag = false;
                        break;
                    }
                    if(s[j] == '-'){
                        s[j] = '+';
                    }
                    else{
                        s[j] = '-';
                    }
                }
                cnt++;
            }
            /*
            for(int j = 0;s[j] != NULL;j++){
                printf("%c",s[j]);
            }
            printf("\n");
            */
        }
        printf("Case #%d: ",q);
        if(!flag){
            printf("IMPOSSIBLE\n");
        }
        else{
            printf("%d\n",cnt);
        }
    }
}
