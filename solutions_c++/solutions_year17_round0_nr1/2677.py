#include <bits/stdc++.h>
using namespace std;
char flip(char s)
{
    if(s == '-')
        return '+';
        return '-';

}
int main()
{
    int T;
    cin>>T;
    for(int t = 1;t<=T;t++)
    {
        string s;
        cin>>s;
        int b;
        cin>>b;
        int st = -1,en = -1;
        int len = s.length();
        int cn = 0;
        int ans = 0;
        int f = 0;
        for(int i = 0;i< len;i++)
        {
            if(s[i] == '+')
                continue;
            if(s[i] == '-' && i<=len-b)
            {
                for(int j = i;j<=i+b-1;j++)
                    s[j] = flip(s[j]);
                ans++;
            }
            else
            {
                f = 1;
                break;
            }

        }
        if(f)
        {
                    cout<<"Case #"<<t<<": "<<"IMPOSSIBLE"<<endl;

        }
        else
        cout<<"Case #"<<t<<": "<<ans<<endl;

    }

}
