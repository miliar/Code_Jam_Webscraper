#include <bits/stdc++.h>
using namespace std;


bool ok(int s)
{
    int last = 10;
    while(s)
    {
        if(last < s % 10)
            return 0;
        last = s % 10;
        s /= 10;
    }
    return 1;
}
int main()
{
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);
    int t;
    cin >> t;
    for(int cnt = 1; cnt <= t; cnt++)
    {
        int n, ans;
        cin >> n;
        for(int i = n; i >= 1; i--)
            if(ok(i))
            {
                ans = i;
                break;
            }
        printf("Case #%d: %d\n", cnt, ans);
    }
    return 0;
}