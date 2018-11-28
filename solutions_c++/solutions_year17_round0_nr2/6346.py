#include <bits/stdc++.h>

using namespace std;

int main()
{
   freopen("B-large.in", "r", stdin);
    freopen("B.txt", "w", stdout);
    int test;

    cin>>test;

    for(int cas = 1; cas<=test; cas++)
    {
        string s;

        cin>>s;

        bool f = false;

        for(int i = s.size() - 1; i>=1; i--)
        {


            if(s[i]<s[i-1] )
            {
                s[i] = '9';
                s[i-1]--;

                for(int j = i; j<s.size(); j++)
                {
                    s[j] = '9';
                }
            }
        }

        string ans = "";


        {
            bool zero = true;

            for(int i = 0; i<s.size(); i++)
            {
                if(s[i] != '0')
                {
                    zero = false;
                    ans += s[i];
                }

                else if(!zero) ans += s[i];

            }
        }


        printf("Case #%d: %s\n", cas, ans.c_str());

    }
}
