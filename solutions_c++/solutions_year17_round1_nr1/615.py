#include <stdio.h>

int t;
int r, c;
char cake[30][30];

int max(int a, int b) {return a > b ? a : b;}

int main()
{
    freopen("/Users/IohcEjnim/Desktop/TEMP/A-large.in", "r", stdin);
    freopen("/Users/IohcEjnim/Desktop/TEMP/result.out", "w", stdout);
    int tn, i, j, rf, cf;
    char state = 0;
    scanf("%d", &t);
    for (tn = 1; tn <= t; tn++)
    {
        scanf("%d %d", &r, &c);
        for (i = 1; i <= r; i++)
            scanf("%s", cake[i]+1);
        
        rf = 0;
        for (i = 1; i <= r; i++)
        {
            cf = 0;
            for (j = 1; j <= c; j++)
            {
                if (cf == 0)
                {
                    if (cake[i][j] == '?') continue;
                    state = cake[i][j];
                    cf = j;
                }
                else
                {
                    if (cake[i][j] != '?') state = cake[i][j];
                    cake[i][j] = state;
                }
            }
            for (j = 1; j < cf; j++) cake[i][j] = cake[i][cf];
            
            if (rf == 0)
            {
                if (cf == 0) continue;
                rf = i;
            }
            if (cf == 0)
                for (j = 1; j <= c; j++) cake[i][j] = cake[i-1][j];
        }
        
        printf("Case #%d:\n", tn);
        for (i = 1; i <= r; i++)
            printf("%s\n", cake[max(i, rf)]+1);
    }
}