#include <cstdio>
#include <cmath>
#include <algorithm>
#include <functional>
#include <iostream>

using namespace std;

long int exp(int a, int b)
{
    int res = 1;
    for (int i = 0; i < b; i++)
        res *= a;
    return res;
}

bool tidy(unsigned long long number, int length)
{
    bool tidy = true;
    int digit[length + 1], assDigit[length + 1];
    for (int i = length; i >= 1; i--)
    {
        digit[length - i] = fmod(number, exp(10, i))/exp(10, i-1);
        assDigit[length - i] = digit[length - i];
    }
    sort(assDigit,assDigit + length);

   for (int i = 0; i < length; i++)
   {
       if (assDigit[i] != digit[i])
       {
           tidy = false;
           break;
       }
   }
    return tidy;
}

int main()
{
    int t, c, test, length;
    unsigned long long number;
    scanf("%d", &t);
    for (int i = 1; i <= t; i++)
    {
        scanf("%llu", &number);

            number++;
            do {
                number--;
                length = (int)log10(number) + 1;

            } while (tidy(number, length) == false);

            printf("Case #%d: %llu\n", i, number);
    }
}
