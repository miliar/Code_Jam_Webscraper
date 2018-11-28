#include<stdio.h>
#include<string.h>
int n;
char str[20];
int main()
{
    int i, tt, T;
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d", &T);
    for(tt=1; tt<=T; ++tt)
    {
        scanf("%s", str+1);
        n = strlen(str+1);
        for(i=1; i<n; ++i)
        {
            if(str[i]>str[i+1]) break;
        }
        if(i==n){ printf("Case #%d: %s\n", tt, str+1); continue; }
        while(str[i]==str[i-1]) --i;
        --str[i];
        for(++i;i<=n; ++i) str[i] = '9';
        i=1;
        while(str[i]=='0') ++i;
        printf("Case #%d: %s\n", tt, str+i);
    }
}
