#include <iostream>

using namespace std;

int T;
char x[1000];

int main() {
    scanf("%d",&T);
    for(int TC = 1; TC <= T; TC++){
        scanf("%s",x);
        int len = 0;
        for(len = 0; x[len]; len++){
            x[len] -= '0';
        }
        for(int i=len - 2; i>=0; i--){
            if(x[i] > x[i+1]){
                x[i] --;
                for(int j=i+1; j<len; j++){
                    x[j] = 9;
                }
            }
        }
        int lead0;
        for(lead0=0; x[lead0] == 0; lead0++);
        printf("Case #%d: ",TC);
        for(int i=lead0; i<len;i++){
            printf("%d",x[i]);
        }
        printf("\n");
    }
    return 0;
}