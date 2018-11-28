#include <iostream>
#include <cstring>
#include <cstdio>

using namespace std;

const int maxn = 20 + 5;

char s[maxn];

int findpos(int len)
{
    for(int i = 0; i < len - 1; ++i) if(s[i] > s[i + 1]) return i;
    return len - 1;
}

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("answer.out", "w", stdout);
    int T, cas = 0;
    scanf("%d", &T);
    while(T--)
    {
        scanf("%s", s);
        int len = strlen(s);
        while(true)
        {
            int pos = findpos(len);
            if(pos == len - 1) break;
            --s[pos];
            for(int i = pos + 1; i < len; ++i) s[i] = '9';
        }
        int p = 0;
        while(p < len - 1 && s[p] == '0') ++p;
        printf("Case #%d: ", ++cas);
        printf("%s\n", s + p);
    }
    return 0;
}
