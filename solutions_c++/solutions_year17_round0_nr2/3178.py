#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>


void solve()
{
    char N[20];  // 18 + 1 (for 'A') + 1 (for '\0')
    scanf("%s", N);
    strcat(N, "A");  // 'A' > '9', hack
    size_t const l = strlen(N);

    char prev = '0';
    int power = 0;
    bool nine = false;

    for(size_t i = 0; i < l; i++)
    {
        if(nine)
        {
            putchar('9');
            continue;
        }

        if(N[i] == prev)
            power++;
        else
        {
            if(N[i] > prev)
            {
                if(prev != '0')
                    while(power--)
                        putchar(prev);
            }
            else
            {
                if(prev != '1')
                    putchar(prev - 1);
                
                while(--power)
                    putchar('9');
                nine = true;
            }
            
            prev = N[i];
            power = 1;
        }
    }

}

int main()
{
    int T;
    scanf("%d", &T);

    for(int i = 0; i < T; i++)
    {
        printf("Case #%d: ", i + 1);
        solve();
        printf("\n");
    }

    return 0;
}
