#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
using namespace std;

int main(){
    int cas;
    while(scanf("%d", &cas)!=EOF){
        char str[25];
        for(int t=1;t<=cas;t++){
            scanf("%s", str);
            int len = strlen(str);
            for(int i=len-1;i>=0;i--){
                if(str[i] < str[i-1] || (i==len-1 && str[i]=='0')){
                    str[i] = '9';
                    for(int j=i+1;j<len;j++)
                        str[j] = '9';
                    str[i-1]--;
                    for(int j=i-1;j > 0;){
                        if(str[j] < '0'){
                            str[j] = '9';
                            str[j-1]--;
                            j--;
                        }
                        else
                            break;
                    }
                }
            }
            printf("Case #%d: ", t);
            int i;
            for(i=0;str[i] == '0';i++);
            for(;i<len;i++)
                printf("%c", str[i]);
            printf("\n");
        }
    }
    return 0;
}
