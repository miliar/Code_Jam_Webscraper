#include <iostream>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

using namespace std;

char s[1005];

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T;
    cin >> T;
    for(int br = 1; br <= T; br++)
    {
        scanf("%s", &s);
        int k;
        int num = 0;
        cin >> k;
        int n = strlen(s);
        for(int i = 0; i < n - k + 1; i++)
            if(s[i] == '-')
            {
                num++;
                for(int j = 0; j < k; j++)
                {
                    if(s[i + j] == '-')
                        s[i + j] = '+';
                    else
                        s[i + j] = '-';
                }
            }
        for(int i = n - k + 1; i < n; i++)
            if(s[i] == '-')
                num = -1;
        printf("Case #%i: ", br);
        if(num == -1)
            printf("IMPOSSIBLE\n");
        else
            printf("%i\n", num);

    }
    return 0;
}
