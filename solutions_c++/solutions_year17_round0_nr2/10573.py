#include <stdio.h>
#include <cmath>

using namespace std;

bool isasc(long long x)
{
    int last = x % 10,
        curr;

    // printf("%lld\n", x);

    x /= 10;

    while ( x != 0 ) {
        curr = x % 10;
        x /= 10;

        // printf(" %d > %d\n", curr, last);

        if (curr > last)
            return false;

        last = curr;
    }

    return true;
}

long long get_top(long long x)
{
    while ( x > 1 && !isasc(x) ) {
        x--;
    }

    return x;
}

int main()
{
    int t = 0;
    long long a;

    scanf("%d", &t);

    long long answers[t];

    for ( int i = 0; i < t; ++i ) {
        scanf("%lld", &a);
        answers[i] = get_top(a);
    }

    for ( int i = 0; i < t; ++i ) {
        printf("Case #%d: %lld\n", i+1, answers[i]);
    }

    return 0;
}