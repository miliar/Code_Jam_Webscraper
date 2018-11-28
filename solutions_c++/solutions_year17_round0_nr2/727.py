#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

char str[30];

int main()
{
    int T;
    scanf("%d", &T);
    for(int Case = 1; Case <= T; ++Case)
    {
        scanf("%s", str);
        int l = strlen(str);
        int k = l;
        for(int i = 1; i < l; ++i)
        {
            if(str[i] < str[i - 1])
            {
                k = i - 1;
                for(int p = i - 1; p >= 0; --p)
                    if(str[p] == str[i - 1])
                        k = p;
                    else
                        break;
                break;
            }
        }
        printf("Case #%d: ", Case);
        int beg = 0;
        if(k == 0 && str[k] == '1') beg = 1;
        for(int i = beg; i < k; ++i) printf("%c", str[i]);
        if(k < l && !beg) printf("%c", str[k] - 1);
        for(int i = k + 1; i < l; ++i) printf("9");
        puts("");
    }
    return 0;
}
