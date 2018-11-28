#include <cstdio>
#include <cstring>

int main(){
    //freopen("B-small-attempt0.in.txt", "r", stdin);
    //freopen("B-small-attempt0.out.txt", "w", stdout);
    int testCases;
    scanf("%d", &testCases);
    char num[25];
    for(int T = 1; T <= testCases; ++T){
        scanf("%s", num);
        bool chk = true;
        int len = strlen(num);
        while(chk){
            chk = false;
            for(int i = 0; i+1 < len; ++i){
                if(num[i] > num[i+1]){
                    chk = true;
                    num[i]--;
                    for(int j = i+1; j < len; ++j){
                        num[j] = '9';
                    }
                }
            }
        }
        printf("Case #%d: ", T);
        bool zero = false;
        for(int i = 0; i < len; ++i){
            if(num[i] != '0')
                zero = true;
            if(zero)
                printf("%c", num[i]);
        }
        printf("\n");
    }
    return 0;
}
