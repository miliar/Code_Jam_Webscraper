#include <cstdio>
#include <string.h>
using namespace std;
int main()
{
    int t;
    scanf("%d", &t);
    char n[20];
    for (int i=0; i<t; i++)
    {
        printf("Case #%d: ", i+1);
        scanf("%s", n);
        int e=strlen(n);
        for (int j=0; j<e; j++)
        {
            if (j==e-1)
            {
                printf("%c", n[j]);
            }
            else
            {
                bool flag=false;
                int u=j+1;
                while (u<e)
                {
                    if (n[j]>n[u]) 
                    {
                        flag=true;
                        break;
                    }
                    if (n[j]==n[u]) 
                    {
                        u++;
                        continue;
                    }
                    break;
                }
                if (flag)
                {
                    if ('1'!=n[j]) printf("%c", (char)((int)n[j]-1));
                    for (int k=j+1; k<e; k++) printf("9");
                    break;
                }
                else
                {
                    printf("%c", n[j]);
                }

            }
        }
        printf("\n");
    }
    return 0;
}
