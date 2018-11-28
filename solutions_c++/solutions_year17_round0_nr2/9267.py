#include<bits/stdc++.h>

using namespace std;

bool check(int x)
{
    string s1 = "", s2 = "";
    while(x)
    {
        int a = x % 10;
        char c = a + '0';
        s1 = c + s1;
        s2 = c + s2;
        x /= 10;
    }
    sort(s1.begin(), s1.end());
    return s1 == s2;
}

int main()
{
    freopen("B-small-attempt2.in","r",stdin);
    freopen("output.out","w",stdout);
    int cases, c = 1;
    scanf("%d", &cases);
    while(cases--)
    {
        int n, ans;
        scanf("%d", &n);
        for(int i = 1; i <= n; i++)
            if(check(i))
                ans = i;
        printf("Case #%d: %d\n", c++, ans);
    }
    return 0;
}
