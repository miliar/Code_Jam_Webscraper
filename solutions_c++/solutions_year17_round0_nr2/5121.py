#include<stdio.h>
#include<string.h>
int main()
{
    int T,i,j,l,k;
    char s[20];
    scanf("%d",&T);
    for(i = 1; i <= T; i++) {
        scanf("%s",s);
        l = strlen(s);
        for(j = 0; j < l-1; j++) {
            if(s[j] > s[j+1]) break;
        }
        if( j == l-1 ) {
            printf("Case #%d: %s\n",i,s);
            continue;
        }
        if(s[j] == '1') {
            for(k = 0; k < l-1; k++)
                s[k] = '9';
            s[l-1] = '\0';
            printf("Case #%d: %s\n",i,s);
            continue;
        }
        for(; j > 0; j--) {
            if(s[j] - 1 >= s[j-1]){
                break;
            }
        }
        --s[j];
        for(k = j+1; k < l; k++) {
            s[k] = '9';
        }
        printf("Case #%d: %s\n",i,s);
    }
    return 0;
}
