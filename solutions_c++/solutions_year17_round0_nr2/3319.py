#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>

using namespace std;

char str[100];

int main()
{
    freopen("x.in", "r", stdin);
    freopen("x.txt", "w", stdout);
    int T;
    cin >> T;
    for (int cas = 1; cas <= T; cas++)
    {
        int n;
        scanf(" %s", str);
        printf("Case #%d: ", cas);
        int len = strlen(str);
        if (len == 1) puts(str);
        else
        {
            int cur = 0;
            bool flag = false;
            for (int i = 1; i < len; i++)
            {
                if (str[i - 1] < str[i]) cur++;
                if (str[i - 1] > str[i]) {flag = true; break;}
            }
            if (!flag) puts(str);
            else
            {
                for (int i = 0; i < cur; i++)
                    printf("%c", str[i]);
                if (str[cur] > '1') printf("%c", str[cur] - 1);
                for (int i = cur + 1; i < len; i++)
                    printf("9");
                puts("");
            }
        }
    }
    return 0;
}
