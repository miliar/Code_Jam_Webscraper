#include <bits/stdc++.h>
using namespace std;

const int maxN = 20;

char in[maxN];

int main()
{
    int t;
    scanf ("%d", &t);

    for (int test=1; test<=t; test++)
    {
        scanf ("%s", in);
        int n = strlen(in);

        for (int i=0; i<n-1; i++)
        {
            if (in[i + 1] >= in[i]) continue;
            
            int j = i;

            while (j > 0 and in[i] == in[j - 1])    j--;
            in[j]--;
            while (j < n - 1)   in[++j] = '9';

            break;
        }

        printf("Case #%d: %s\n", test, (in[0] == '0' ? in + 1 : in));
    }

    return 0;
}