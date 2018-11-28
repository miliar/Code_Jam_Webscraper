#include<stdio.h>
int r, c;
char arr[30][30];
int main()
{
    int tt, T, i, j;
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d", &T);
    for(tt=1; tt<=T; ++tt)
    {
        scanf("%d%d", &r, &c);
        for(i=1; i<=r; ++i) scanf("%s", arr[i]+1);
        for(i=1; i<=r; ++i)
        {
            j=1;
            while(arr[i][j]=='?') ++j;
            for(; j<=c; ++j)
            {
                if(arr[i][j]!='?') continue;
                arr[i][j] = arr[i][j-1];
            }
            for(j=c-1; j>=1; --j)
            {
                if(arr[i][j]!='?') continue;
                arr[i][j] = arr[i][j+1];
            }
            if(arr[i][1] == '?' && i!=1)
            {
                for(j=1; j<=c; ++j) arr[i][j] = arr[i-1][j];
            }
        }
        for(i=r-1; i>=1; --i)
        {
            if(arr[i][1] != '?') continue;
            for(j=1; j<=c; ++j) arr[i][j] = arr[i+1][j];
        }
        printf("Case #%d:\n", tt);
        for(i=1; i<=r; ++i) printf("%s\n", arr[i]+1);
    }
}
