#include <stdio.h>
#include <string.h>

char arr[25];

void flip(int flag, int len){
    for(int i = flag ; i <= len ; i++){
        arr[i] = 9;
    }
}

void process(){
    scanf("%s",arr+1);
    int len = strlen(arr+1);
    for(int i = 1 ; i <= len ; i++) arr[i] -= '0';
    for(int i = len ; i >= 1 ; i--){
        if(arr[i]<arr[i-1]){
            arr[i-1]--;
            flip(i,len);
        }
    }
    int ok = 0;
    for(int i = 0 ; i <= len ; i++){
        if(arr[i]!=0) ok=1;
        if(ok) printf("%d",arr[i]);
    }
}

int main(){
    int t;
    //freopen("B.in","rt",stdin);
    //freopen("B.txt","wt",stdout);
    scanf("%d",&t);
    for(int i = 1 ; i <= t ; i++){
        printf("Case #%d: ",i);
        process();
        puts("");
    }
}
