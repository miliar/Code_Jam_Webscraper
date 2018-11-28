#include<iostream>
#include<cstdio>

using namespace std;

const int MAX_N = 1000;

char pancake[MAX_N + 1];

int main(void)
{
    int T, K, res;  cin >> T;

    for (int t = 1; t <= T; t ++)
    {
        res = 0;
        scanf("%s %d", pancake, &K);

        for (int i = K-1; pancake[i] != '\0'; i ++)
            if (pancake[i-K+1] == '-')
            {
                for (int j = i - K + 1; j <= i; j ++)
                    pancake[j] = (pancake[j] == '+')?'-':'+';

                res++;
            }

        bool flag = true;
        for (int i = 0; pancake[i] != '\0'; i ++)
            if (pancake[i] == '-')
            {
                printf("Case #%d: IMPOSSIBLE\n", t);
                flag = false;
                break;
            }

        if (flag)
            printf("Case #%d: %d\n", t, res); 
    }
}
