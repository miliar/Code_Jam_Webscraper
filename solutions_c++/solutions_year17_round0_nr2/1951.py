#include <cstdio>
#include <algorithm>
#include <vector>

int main(){
    //freopen("B-large.in", "r", stdin);
    //freopen("B-large.out", "w", stdout);

    int T, lastDigit, digits;
    bool trailing9;
    char N[25];

    scanf("%d", &T);
    for(int t = 1; t <= T; t++){
        scanf(" %s", N);

        for(int i = 0; i < 25; i++){
            if(N[i] == '\0'){
                digits = i;
                break;
            }
        }

        lastDigit = 0;
        trailing9 = false;

        for(int i = 1; i < digits; i++){
            if(N[i] > N[i-1])
                lastDigit = i;
            if(N[i] < N[i-1]){
                trailing9 = true;
                break;
            }
        }

        printf("Case #%d: ", t);
        if(trailing9){
            for(int i = 0; i < lastDigit; i++)
                printf("%c", N[i]);
            if(lastDigit != 0 || N[lastDigit] != '1')
                printf("%c", N[lastDigit] - 1);
            for(int i = lastDigit+1; i < digits; i++)
                printf("9");
            printf("\n");
        }
        else
            printf("%s\n", N);
    }
}
