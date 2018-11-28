#include<stdio.h>

int main(){
    int t;
    scanf("%d",&t);
    for(int j=1;j<=t;j++){
        char data[20];
        scanf("%s",data);
        for(int i=1;data[i];i++){
            if(data[i-1]>data[i]){
                int s=i;
                while(1){
                    data[s]='9';
                    data[s-1]-=1;
                    if(data[s-2]<=data[s-1])
                        break;
                    s--;
                }
                for(;data[i];i++){
                    data[i]='9';
                }
                break;
            }
        }
        printf("Case #%d: ",j);
        if(data[0]>'0')
            printf("%s\n",data);
        else{
            for(int i=1;data[i];i++)
                printf("%c",data[i]);
            printf("\n");
        }
    }
    return 0;
}
