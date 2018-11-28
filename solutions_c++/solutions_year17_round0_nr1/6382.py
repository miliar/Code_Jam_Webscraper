#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int test;

    cin>>test;

    for(int cas  = 1; cas<=test; cas++)
    {
        string s; int k;
        cin>>s>>k;
        int cnt  = 0;

        bool f = false;

        for(int i = 0; i<s.size(); i++)
        {
            if(s[i] == '-')
            {
                if(i+k<=s.size())
                {
                    for(int j = i; j<(i+k); j++)
                    {   //cout<<s[j];
                        if(s[j]=='-') s[j] = '+';
                        else s[j] = '-';

                    }
                    //cout<<endl;

                    cnt++;
                }
                else
                {
                    f = true;
                    break;
                }
            }
        }

        if(!f)
        printf("Case #%d: %d\n", cas, cnt);
        else printf("Case #%d: IMPOSSIBLE\n", cas);
    }
}
