#include <cstdio>
#include <cstring>

int main(){
    int t,n;
    scanf("%d",&t);
    for(int i=0;i<t;i++){
        char set[20]={0};
        scanf("%s",set);
        int size = strlen(set);
        for(int j=0;j<size;j++){
            set[j]-='0';
        }
        for(int j=0;j<size;j++){
            int flag=0;
            for(int k=0;k<size-1;k++){
                if(flag==1){
                    set[k+1]=9;
                }
                if(set[k]>set[k+1]){
                    set[k]--;
                    set[k+1]=9;
                    flag=1;
                }
            }
            // for(int j=0;j<size;j++){
            //     if(set[j]!=0)
            //         printf("%d",set[j]);
            // }
            // printf("\n");
        }
        printf("Case #%d: ",i+1);
        for(int j=0;j<size;j++){
            if(set[j]!=0)
                printf("%d",set[j]);
        }
        printf("\n");
    }
}