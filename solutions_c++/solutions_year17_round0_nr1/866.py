#include <stdio.h>
#include <string.h>

char arr[2000];

void flip(int flag, int k){
    for(int i = flag ; i < flag + k ; i++){
        if(arr[i]=='+') arr[i] = '-';
        else arr[i] = '+';
    }
}

void process(){
    int k;
    scanf("%s %d",arr,&k);
    int len = strlen(arr);
    int cnt = 0;
    for(int i = 0 ; i < len-k+1 ; i++){
        if(arr[i]=='-') flip(i,k), cnt++;
    }
    for(int i = 0 ; i < len ; i++){
        if(arr[i]=='-'){
            printf("IMPOSSIBLE");
            return;
        }
    }
    printf("%d",cnt);
}

int main(){
    int t;
    //freopen("A.in","rt",stdin);
    //freopen("A.out","wt",stdout);
    scanf("%d",&t);
    for(int i = 1 ; i <= t ; i++){
        printf("Case #%d: ",i);
        process();
        puts("");
    }
}
