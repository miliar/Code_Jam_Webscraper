#include<bits/stdc++.h>

using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.out","w",stdout);
    int cases, c = 1;
    scanf("%d", &cases);
    while(cases--)
    {
        string s;
        int k, ans = 0;
        bool flag = true;
        cin >> s >> k;
        while(1)
        {
            int tmp = k;
            bool reach = true;
            for(int i = 0; i < s.size(); i++)
                if(s[i] == '-')
                    reach = false;
            if(reach)
                break;
            for(int i = 0; i < s.size(); i++)
                if(s[i] == '-')
                {
                    if(s.size() - i >= k)
                    {
                        while(tmp--)
                        {
                            if(s[i] == '-')
                                s[i] = '+';
                            else
                                s[i] = '-';
                            i++;
                        }
                        ans++;
                        break;
                    }
                    else
                        flag = false;
                }
            if(!flag)
                break;
        }
        if(flag)
            printf("Case #%d: %d\n", c++, ans);
        else
            printf("Case #%d: IMPOSSIBLE\n", c++);
    }
    return 0;
}
