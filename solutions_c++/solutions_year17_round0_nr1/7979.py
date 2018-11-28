#include <cstdio>
#include <cstring>

using namespace std;

int tc, k, ans;
char cad[1000+5];

int main()
{
    freopen("in.in", "r", stdin);
    freopen("out.out", "w", stdout);
    scanf("%d", &tc);
    for(int t=1; t<=tc; t++)
    {
        ans = 0;
        scanf("%s%d", cad, &k);
        for(int i=0; i<strlen(cad)-k+1; i++)
        {
            if(cad[i] == '-')
            {
                ans++;
                for(int j=0; j<k; j++)
                {
                    if(cad[j+i] == '-')
                        cad[j+i] = '+';
                    else
                        cad[j+i] = '-';
                }
            }
        }

        for(int i=0; i<strlen(cad); i++)
            if(cad[i] == '-')ans = -1;

        printf("case #%d: ", t);

        if(ans == -1)
            printf("IMPOSSIBLE\n");
        else
            printf("%d\n", ans);
    }
    return 0;
}
