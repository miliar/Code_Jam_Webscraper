#include <cstdio>
#include <cstring>
using namespace std;

char s[50];
char ans[50];
int n;

int T;

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    scanf("%d", &T);
    for (int z = 1; z <= T; ++z)
    {
        scanf("%s", s);
        n = strlen(s);
        ans[0] = s[0];
        int i, j;
        for (i = 1; i < n; ++i)
        {
            if (s[i] >= s[i - 1])
            {
                ans[i] = s[i];
                continue;
            }
            for (j = i - 1; ; --j)
            {
                ans[j] -= 1;
                if (j == 0 && ans[j] == '0')
                {
                    memset(ans, '9', (n - 1) * sizeof (char));
                    ans[n - 1] = '\0';
                    i = n;
                    break;
                }
                if (j == 0 || ans[j] >= ans[j - 1])
                {
                    memset(ans + j + 1, '9', n * sizeof (char));
                    ans[n] = '\0';
                    i = n;
                    break;
                }
            }
        }
        ans[n] = '\0';
        
        printf("Case #%d: %s\n", z, ans);
    }
    
    fclose(stdin);
    fclose(stdout);
    return 0;
}
