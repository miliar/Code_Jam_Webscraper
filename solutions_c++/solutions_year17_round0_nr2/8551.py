#include <cstdio>

using namespace std;

void solve(int index, char *str)
{
    printf("Case #%d: ", index);
    for (int i = 1; i < str[i] != '\0'; i++)
    {
        if (str[i] < str[i - 1])
        {
            if (str[i - 1] == '1')
            {
                for (int j = 1; str[j] != '\0'; j++)
                    printf("9");
                printf("\n");
            }
            else
            {
                str[i - 1] = str[i - 1] - 1;
                if (i - 2 >= 0 && str[i - 2] > str[i - 1])
                {
                    char temp = str[i - 1];
                    int j = i - 2;
                    while (j >= 0)
                    {
                        if (str[j] <= temp)
                            break;
                        j--;
                    }
                    j++;

                    str[j] = str[j] - 1;

                    for (int k = 0; k <= j; k++)
                        printf("%c", str[k]);

                    for (j++; str[j] != '\0'; j++)
                        printf("9");
                    printf("\n");
                }
                else
                {
                    for (int j = 0; j < i; j++)
                        printf("%c", str[j]);

                    for (int j = i; str[j] != '\0'; j++)
                        printf("9");
                    printf("\n");
                }
            }
            return;
        }
    }
    printf("%s\n", str);
}

int main()
{
    int T;
    scanf("%d", &T);

    char input[100];

    for (int t = 0; t < T; t++)
    {
        scanf("%s", input);
        solve(t + 1, input);
    }
    return 0;
}
