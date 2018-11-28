#include <iostream>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

char s[1050];
int n, k, A[1050];

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t, c = 0;
    scanf("%d", &t);
    while(t--)
    {
        ++c;
        scanf("%s%d", s, &k);
        n = strlen(s);

        int carry = 0;
        int ans = 0;
        for(int i = 0;i < n - k + 1;++i)
        {
            carry -= A[i];
            if(carry & 1)
            {
                if(s[i] == '-')     s[i] = '+';
                else                s[i] = '-';
            }

            if(s[i] == '-')
            {
                s[i] = '+';
                ++carry;
                ++ans;
                A[i + k] = 1;
            }
        }

        bool ok = true;
        for(int i = n - k + 1;i < n;++i)
        {
            carry -= A[i];
            if(carry & 1)
            {
                if(s[i] == '-')     s[i] = '+';
                else                s[i] = '-';
            }
            if(s[i] == '-')
                ok = false;
        }
        printf("Case #%d: ", c);
        if(ok)
            printf("%d\n", ans);
        else
            printf("IMPOSSIBLE\n");

        cerr << c << " done\n";
        memset(A, 0, sizeof(A));
    }
    return 0;
}
