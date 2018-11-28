#include<stdio.h>
#include<string.h>

int main(){
    int T;
    scanf("%d", &T);
    for(int kase=1; kase<=T; kase++){
        char s[25];
        scanf("%s", s+1);
        printf("Case #%d: ", kase);
        int n = strlen(s+1);
        bool bad = false;
        for(int i=1, j=1; i<=n-1; i++){
            if(s[i] < s[i+1]){
                j++;
            }else if(s[i] > s[i+1]){
                bad = true;
                if(j == 1){
                    if(s[1] == '1'){
                        for(int k=1; k<=n-1; k++){
                            putchar('9');
                        }
                        putchar('\n');
                    }else{
                        putchar(s[i]-1);
                        for(int k=2; k<=n; k++){
                            putchar('9');
                        }
                        putchar('\n');
                    }
                }else{
                    for(int k=1; k<=j-1; k++){
                        putchar(s[k]);
                    }
                    putchar(s[j]-1);
                    for(int k=j+1; k<=n; k++){
                        putchar('9');
                    }
                    putchar('\n');
                }
                break;
            }
        }
        if(!bad){
            puts(s+1);
        }
    }
    return 0;
}
