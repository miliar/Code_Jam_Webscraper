#include <cstdio>
#include <cstdlib>
#include <cstring>


void caser(int casen)
{
    char txt[20];
    scanf("%s", txt);
    printf("Case #%d: ", casen);

    for(int i = 1; txt[i]; i++)
    {
        if(txt[i - 1] > txt[i])
        {
            for(i--; i > 0; i--)
            {
                if(txt[i - 1] < txt[i])
                    break;
            }
                    char c = txt[i];
                    txt[i] = '\0';
                    printf(txt);
                    c--;
                    if(c != '0')
                    printf("%c", c);
            for(i++; txt[i]; i++)
                printf("9");
           printf("\n");
           return;
        }
    }
    printf("%s\n", txt);
}

int main()
{
    int n;
    scanf("%d\n", &n);
    for(int i = 1; i <= n; i++)
        caser(i);
    return 0;
}