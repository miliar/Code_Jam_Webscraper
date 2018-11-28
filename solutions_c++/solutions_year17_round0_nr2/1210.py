#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

char s[20 + 9];

int main()
{
    int T;
    scanf("%d", &T);
    for (int c=1; c<=T; c++)
    {
        scanf("%s", s);
        int n = strlen(s);

        char small = '9';

        for (int i=n-1; i>=0; i--)
        {
            if (s[ i ] <= small)
                small = s[ i ];
            else
            {
                s[ i ] -= 1;
                small = s[ i ];
                for (int j=i+1; j<n; j++)
                    s[ j ] = '9';
            }
        }

        char * st = s;
        while (*st == '0')
            st++;

        printf("Case #%d: ", c);
        printf("%s", st);
        printf("\n");
    }

    return 0;
}


