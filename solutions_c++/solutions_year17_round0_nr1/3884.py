#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
using namespace std;

int main(){
    int cas;
    while(scanf("%d", &cas)!=EOF){
        for(int t=1;t<=cas;t++){
            char str[1010];
            int k;
            scanf("%s", str);
            scanf("%d", &k);
            
            int count = 0;
            int len = strlen(str);
            for(int i=0;i<=len-k;i++){
                if(str[i] == '-'){
                    count++;
                    for(int j=i;j<i+k;j++)
                        str[j] = (str[j] == '-'?'+':'-');
                }
            }
            printf("Case #%d: ", t);
            bool flag = false;
            for(int i=len-1;i>len-1-k;i--)
                if(str[i] == '-'){
                    flag = true;
                    break;
                }
            if(flag)
                printf("IMPOSSIBLE\n");
            else
                printf("%d\n", count);
        }
    }
    return 0;
}
