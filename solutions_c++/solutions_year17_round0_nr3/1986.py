#include<cstdio>

bool is_odd(long long n)
{
    if (n % 2 == 1)
        return true;
    else
        return false;
}

int main(int argc, char** argv)
{
    int t;
    long long n, k, max, min, num, tmax, tmin, oddnum, evalnum;
    FILE *input, *output;

    if (argc != 3)
    {
        printf("intput을 제대로 넣어주세요.\n");
        return 0;
    }

    input = fopen(argv[1], "r+");
    output = fopen(argv[2], "w+");

    fscanf(input, "%d", &t);

    for (int i = 1; i <= t; i++)
    {
        fscanf(input, "%lld %lld", &n, &k);

        num = 1;

        tmax = tmin = n;
        if (is_odd(n))
            oddnum = 1;
        else
            oddnum = 0;
        evalnum = num - oddnum;

        while (1)
        {
            max = tmax / 2;
            min = (tmin - 1) / 2;

            if (k < num * 2)
                break;

            n /= 2;
            num *= 2; 

            if (is_odd(tmax))
            {
                if (is_odd(max))
                    oddnum = oddnum * 2 + evalnum;
                else
                {
                    evalnum = oddnum * 2 + evalnum;
                    oddnum = num - evalnum;
                }
            }
            else
            {
                if (is_odd(max))
                {
                    evalnum = oddnum * 2 + evalnum;
                    oddnum = num - evalnum;
                }
                else
                    oddnum = oddnum * 2 + evalnum;
            }

            tmax = max;
            tmin = min;
        }

        if (is_odd(tmax))
        {
            if (oddnum > k - num)
                min = max;
        }
        else
        {
            if (evalnum <= k - num)
                max = min;
        }

        fprintf(output, "Case #%d: %lld %lld\n", i, max, min);
    }

    fclose(input);
    fclose(output);

    return 0;
}
