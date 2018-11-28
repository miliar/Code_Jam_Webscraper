#include <stdio.h>

int t;
char s[30];

int main()
{
    freopen("/Users/IohcEjnim/Desktop/TEMP/B-large.in", "r", stdin);
    freopen("/Users/IohcEjnim/Desktop/TEMP/result.out", "w", stdout);

    int tn, i, j;
    scanf("%d", &t);
    
    for (tn = 1; tn <= t; tn++)
    {
        scanf("%s", s);
        for (i = 0; s[i]; i++);
        for (i--; i >= 1; i--)
        {
            if (s[i-1] <= s[i]) continue;
            s[i-1]--;
            for (j = i; s[j]; j++) s[j] = '9';
        }
        
        printf("Case #%d: ", tn);
        i = 0;
        while (s[i] == '0') i++;
        puts(s+i);
    }
}