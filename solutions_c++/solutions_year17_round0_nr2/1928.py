#include<cstdio>

int nth = 0;

bool is_tidy(long long n)
{
    int digit;

    nth = 0;
    digit = n % 10;
    n /= 10;

    while (n > 0)
    {
        nth++;
        if (digit < n % 10)
            return false;

        digit = n % 10;
        n /= 10;
    }

    return true;
}

long long pow_10(int n)
{
    if (n == 0)
        return 1;

    return 10 * pow_10(n - 1);
}

int main(int argc, char** argv)
{
    int t;
    long long n, surplus, temp;

    FILE *input, *output;

    if (argc != 3)
    {
        printf("input을 제대로 넣어주세요.\n");
        return 0;
    }

    input = fopen(argv[1], "r+");
    output = fopen(argv[2], "w+");

    fscanf(input, "%d", &t);

    for (int i = 1; i <= t; i++)
    {
        fscanf(input, "%lld", &n);

        while (1)
        {
            if (is_tidy(n))
            {
                fprintf(output, "Case #%d: %lld\n", i, n);
                break;
            }
            else
            {
                temp = pow_10(nth);
                surplus = n % temp;
                n -= surplus + 1;
            }
        }
    }

    fclose(input);
    fclose(output);

    return 0;
}
