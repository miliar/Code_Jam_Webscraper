#include<stdio.h>
#include<string.h>
int findneg(char *s, int l) 
{
    int neg = 0;
    while(neg < l && s[neg] == '+')
        ++neg;
    return neg;
}
void flipk(char *s, int j, int k)
{
    while(k) {
        if(s[j] == '+') s[j] = '-';
        else s[j] = '+';
        --k;++j;
    }
    return;
}
int main()
{
    int T,k;
    char s[1001];
    scanf("%d",&T);
    for(int i = 1; i <= T; i++){
        scanf("%s%d",s,&k);
        int l = strlen(s);
        int j = findneg(s,l);
        if( j == l ) {
            printf("Case #%d: 0\n",i);
            continue;
        }
        int f = 0;
        while( l - j >= k ) {
            flipk(s,j,k);
            ++f;
            j = findneg(s,l);
        }
        if( j == l ) 
            printf("Case #%d: %d\n",i,f);
        else
            printf("Case #%d: IMPOSSIBLE\n",i);
    }
    return 0;
}
