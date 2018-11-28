#include <cstdio>

int main(int argc, char **argv)
{
    int num_tests, length;
    char number[20];

    scanf(" %d", &num_tests);
    for (int i = 0; i < num_tests; i++)
    {
        for (int j = 0; j < 20; j++) number[j] = '\0';
        scanf(" ");
        length = 0;
        for (int j = 0; ; j++)
        {
            number[j] = getc(stdin);
            if (number[j] == '\n') break;
            length++;
        }

        for (int j = length - 1; j > 0; j--)
        {
            if (number[j] < number[j - 1]) 
            {
                for (int k = 0; k < (length - j); k++)
                {
                    number[length - k - 1] = '9';
                }
                number[j - 1] -= 1;
            }
        }

        for (int j = 0; j < length; j++)
        {
            if (number[j] != '0')
            {
                char *start = &number[j];
                printf("Case #%d: %s", i + 1, start);
                break;
            }
        }
    }

    return 0;
}
