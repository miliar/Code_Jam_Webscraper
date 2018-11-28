#include<bits/stdc++.h>
using namespace std;
int main(){

    freopen("B-large.in", "r", stdin);
    freopen("output.in", "w", stdout);
    char number[20];
    int t , kase = 1;
    scanf("%d",&t);

    while(t-->0){
        scanf("%s",&number);
        int i;
        for(i = 1; i < strlen(number)  ; i++){
            if(number[i-1]>number[i]){
                    number[i] = '9';
                    number[i-1]-=1;
                break;
            }
        }
        for(int j = i-1 ; j>=1 ; j--){
            if(number[j]<number[j-1]){
                number[j] = '9';
                number[j-1]-=1;
            }
        }int test = 1;
        printf("Case #%d: ",kase++);
        for(int i = 0 ; i < strlen(number);i++){
            if(i==0&&number[i]=='0'){
                continue;
            }
            if(number[i]=='9' || test == 9){
                test = 9;
                printf("9");
            }
            else{
                printf("%c",number[i]);
            }

        }printf("\n");
    }
return 0;
}
