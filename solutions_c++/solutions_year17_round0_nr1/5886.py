#include <cstdio>
#include <algorithm>
#include <cstring>
#include <iostream>
using namespace std;
int f;
int flips(char* state, int len)
{
    //printf("%s\n", state);
    if (len < f)
        return -1;
    if (len == f)
    {
        int temp = 0;
        for (int i = 0; i < len; i++)
            if (state[i] == '-')
                temp++;
        if (temp == 0) return 0;
        if (temp == f) return 1;
        return -1000000000;
    }
    if (state[0] == '+')
    {
        return flips(state+1, len-1);
    }
    else
    {
        for (int i = 0; i < f; i++)
        {
            if (state[i] == '-') state[i] = '+';
            else state[i] = '-';
        }
        return flips(state+1, len-1)+1;
    }
}
int main()
{
    freopen("a2.in", "r", stdin);
    freopen("a2.out", "w", stdout);
    int t;
    cin >> t;
    for (int i = 1; i <= t; i++)
    {
        char input[1010];
        cin >> input >> f;
        int len = strlen(input);
        int ans = flips(input, len);
        if (ans >= 0)
            printf("Case #%d: %d\n", i, ans);
        else
            printf("Case #%d: IMPOSSIBLE\n", i);
    }
    return 0;
}
