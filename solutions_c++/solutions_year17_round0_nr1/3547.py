#include <cstdio>

int main(int argc, char **argv)
{
    int num_tests, num_flips, k, num_pancakes;
    char pancakes[1500];

    scanf(" %d", &num_tests);

    for (int i = 0; i < num_tests; i++)
    {
        scanf(" ");
        num_pancakes = 0;
        num_flips = 0;
        for (int j = 0; ; j++)
        {
            pancakes[j] = getc(stdin);
            if (pancakes[j] == ' ') break;
            num_pancakes++;
        }
        scanf(" %d", &k);

        for (int j = 0; j < num_pancakes - k + 1; j++)
        {
            if (pancakes[j] == '+') continue;

            for (int z = 0; z < k && j + z < num_pancakes; z++)
            {
                if (pancakes[j + z] == '-') pancakes[j + z] = '+';
                else pancakes[j + z] = '-';
            }
            num_flips++;
        }

        bool failed = false;
        for (int j = 0; j < k; j++)
        {
            if (pancakes[num_pancakes - k + j] == '-') 
            {
                failed = true;
            }
        }

        if (failed) printf("Case #%d: IMPOSSIBLE\n", i + 1);
        else printf("Case #%d: %d\n", i + 1, num_flips);
    }

    return 0;
}
