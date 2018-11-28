#include <bits/stdc++.h>
using namespace std;

typedef long long LL;
typedef pair < int, int > PII;

int n;
char s[20];

bool check()
{
    for(int i = 1; i < n; i++)
        if(s[i] > s[i + 1]) return false;
    return true;
}

int main()
{
    int te; scanf("%d", &te);
    for(int t = 1; t <= te; t++)
    {
        scanf(" %s", s + 1);
        n = strlen(s + 1);
        int p = n;
        while(!check())
        {
            s[p] = '9';
            s[p - 1]--;
            p--;
        }
        if(s[1] == '0') printf("Case #%d: %s\n", t, s + 2);
        else printf("Case #%d: %s\n", t, s + 1);
    }
    return 0;
}
