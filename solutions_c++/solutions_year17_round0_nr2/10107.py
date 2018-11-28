#include <cstdio>
#include <cstring>
#include <string>

bool judge(int n)
{
    char str[105];

    sprintf(str, "%d", n);
    for(int i = 1; str[i] != '\0'; i++)
        if(str[i] < str[i-1])
            return false;
    return true;
}

int main()
{
    int t, n;

    scanf("%d", &t);
    for(int tt = 1; tt <= t; tt++)
    {
        scanf("%d", &n);
        for(int i = n; i; i--)
        {
            if(judge(i))
            {
                printf("Case #%d: %d\n", tt, i);
                break;
            }
        }
    }

    return 0;
}