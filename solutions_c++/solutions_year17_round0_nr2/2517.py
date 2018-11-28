#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
using namespace std;

char s[20];

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T;
    cin >> T;
    for(int br = 1; br <= T; br++)
    {
        printf("Case #%i: ", br);
        scanf("%s", &s);
        int n = strlen(s);
        int k = 0;
        for(; k < n && s[k] >= s[k - 1]; k++);
        //printf("%i\n", k);
        if(k != n)
        {
            while(k > 1 && s[k - 1] == s[k - 2])
                k--;
            //printf("%i\n", k);
            s[k - 1] -= 1;
            for(int i = k; i < n; i++)
                s[i] = '9';
            if(s[0] == '0')
                for(int i = 0; i < n; i++)
                    s[i] = s[i + 1];
        }
        printf("%s\n", s);
    }
    return 0;
}
