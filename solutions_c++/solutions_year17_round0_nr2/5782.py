#include<iostream>
#include<cstdio>

using namespace std;

int digits[18];
int tmp[18];

int make_digits(long long n)
{
    int i = 0;

    while (n != 0)
    {
        tmp[i++] = n - (n / 10) * 10;

        n /= 10;
    }

    for (int j = 0; j < i; j ++)
        digits[j] = tmp[i-j-1];

    return i;
}

long long make_long(int len)
{
    long long ret = 0;
    for (int i = 0; i < len; i ++)
    {
        ret *= 10;
        ret += digits[i];
    }

    return ret;
}   

bool make_tidy(int len)
{
    int i;
    bool flag = false;

    for (i = 1; i < len; i ++)
        if (digits[i-1] > digits[i])
            break;

    for (; i < len; i ++)
    {
        digits[i] = 0;
        flag = true;
    }

    return flag;
}

int main(void)
{
    int T;  cin >> T;


    for (int t = 1; t <= T; t ++)
    {
        long long N; scanf("%lld", &N);
        int length = make_digits(N);

        while (make_tidy(length))
        {
            N = make_long(length) - 1;
            length = make_digits(N);
        }

        printf("Case #%d: %lld\n", t, N);
    }
}
