#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int L = 1e3 + 5;

char str[L];
int T, n;

int main()
{
    scanf("%d", &T);
    for(int Case = 1; Case <= T; ++Case)
    {
        scanf("%s%d", str, &n);
        int l = strlen(str);
        bool flag = 1;
        int calc = 0;
        for(int i = 0; i < l; ++i)
        {
            if(str[i] == '-')
            {
                if(i + n - 1 >= l)
                {
                    flag = 0;
                    break;
                }
                else
                {
                    ++calc;
                    for(int j = 0; j < n; ++j) str[i + j] = '-' + '+' - str[i + j];
                }
            }
        }
        printf("Case #%d: ", Case);
        if(flag) printf("%d\n", calc);
        else printf("IMPOSSIBLE\n");
    }
    return 0;
}
