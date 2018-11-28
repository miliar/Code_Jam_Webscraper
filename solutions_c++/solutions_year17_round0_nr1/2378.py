#include <stdio.h>

int t, k;
int ans;
char s[1010];

int main()
{
    freopen("/Users/IohcEjnim/Desktop/TEMP/A-large.in", "r", stdin);
    freopen("/Users/IohcEjnim/Desktop/TEMP/result.out", "w", stdout);

    int tn, size, i, j;
    bool able;
    scanf("%d", &t);
    
    for (tn = 1; tn <= t; tn++)
    {
        scanf("%s %d", s, &k);
        for (size = 0; s[size]; size++);
        
        ans = 0;
        for (i = 0; i < size-k+1; i++)
        {
            if (s[i] == '+') continue;
            for (j = 0; j < k; j++)
                s[i+j] = '+'+'-'-s[i+j];
            ans++;
        }
        
        able = true;
        for (i = size-k+1; i < size; i++)
            if (s[i] == '-') able = false;
        
        printf("Case #%d: ", tn);
        if (!able) puts("IMPOSSIBLE");
        else printf("%d\n", ans);
    }
}