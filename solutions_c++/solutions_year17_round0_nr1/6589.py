#include <iostream>
#include <string>
using namespace std;

char flip(char c)
{
    if(c=='+')
        return '-';
    else
        return '+';
}

int main() {
    int t;
    cin>>t;
    for(int tt=1;tt<=t;tt++)
    {
        string s;
        int k;
        cin>>s>>k;

        int ans=0;
        for(int i=0;i<=s.size()-k;i++)
        {
            if(s[i]=='-')
            {
                ans++;
                for(int j=0;j<k;j++)
                {
                    s[i+j] = flip(s[i+j]);
                }
            }
        }

        bool flag = false;
        for(int i=0;i<s.size();i++)
        {
            if(s[i]=='-')
                flag = true;
        }

        if(flag)
            printf("Case #%d: IMPOSSIBLE\n", tt);
        else
            printf("Case #%d: %d\n", tt, ans);
    }
}