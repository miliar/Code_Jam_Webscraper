#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <cstring>
using namespace std;
char flip(char c){
    if(c=='+')
        return '-';
    else
        return '+';
}
void cal(){
    char pan[1100]={0};
    int k,num=0;
    scanf("%s %d",pan,&k);
    //printf("%s %d",pan,k+1);
    for(int i=k-1;i<strlen(pan);i++){
        if(pan[i-(k-1)]=='-'){
                num++;
            for(int j=i-(k-1);j<=i;j++)
                pan[j]=flip(pan[j]);
        }
    }
    for(int i=strlen(pan)-(k-1);i<strlen(pan);i++){
        if(pan[i]=='-'){
            printf("IMPOSSIBLE");
            return;
        }
        else if(i==strlen(pan)-1)
            printf("%d",num);
    }

}
int main() {
    int n;
    scanf("%d",&n);
    for(int i=1;i<=n;i++){
        printf("Case #%d: ",i);
        cal();
        printf("\n");
    }
    return 0;
}
