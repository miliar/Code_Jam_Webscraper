#include<stdio.h>
#include<string.h>
#define N (30)
char s[N];
int main(){
    int T;
    scanf("%d",&T);
    for (int tc = 1; tc <= T ; tc++){
        printf("Case #%d: ",tc);
        scanf("%s",s);
        int l = strlen(s), i;
        for (i = 0; i < l; i++){
            if (s[i] > s[i+1]){
                break;
            }
        }
        if (s[i+1]){
            int j;
            for (j = i-1; j >= 0 && s[j]==s[i]; j--){
            }
            j++;
            s[j]--;
            for (j++; j < l; j++){
                s[j] = '9';
            }
        }
        char *q = s;
        while (*q == '0') q++;
        printf("%s\n",q);
    }
}