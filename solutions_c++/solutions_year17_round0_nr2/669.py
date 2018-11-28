#include <cstdio>
#include <cstring>

char s[20];
char ans[20];

int main()
{
    int T;
    scanf("%d", &T);
    for (int kase = 1; kase <= T; ++kase)
    {
        scanf("%s", s);
        int n = strlen(s);
        s[n] = '9';
        for (int i = n; i >= 0; --i)
        {
            bool flag = true;
            for (int j = 0; j < i; ++j)
                if (s[j] > s[j + 1])
                {
                    flag = false;
                    break;
                }
            if (!flag)
                continue;
            if (i < n && s[i] - 1 < s[i - 1])
                continue;
            for (int j = 0; j < i; ++j)
                ans[j] = s[j];
            ans[i] = s[i] - 1;
            for (int j = i + 1; j < n; ++j)
                ans[j] = '9';
            break;
        }
        ans[n] = 0;
        printf("Case #%d: ", kase);
        if (ans[0] == '0')
        {
            for (int i = 0; i < n - 1; ++i)
                putchar('9');
            puts("");
        }
        else
            puts(ans);
    }
    return 0;
}