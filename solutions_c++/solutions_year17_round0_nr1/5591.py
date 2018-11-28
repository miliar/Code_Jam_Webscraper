#include<bits/stdc++.h>
using namespace std;

int main()
{
    freopen("input.txt","r", stdin);
    freopen("output.txt", "w", stdout);
    int tc;
    cin>>tc;
    int cs = 0;
    while(tc--)
    {
        cs++;
        string str;
        cin>>str;
        int k;
        cin>>k;
        bool flag = false;
        int sz = str.size();
        int cnt = 0;
        int ans = 0;
        for(int i = 0; i < sz ; i++)
        {
            if(str[i]=='+')
                continue;
            if(str[i]=='-')
            {
                flag = true;
                ans++;
            }
            if(flag && i+k <= sz)
            {
                for(int j = i; j < i+k ; j++ )
                {
                    if(str[j]=='+')
                        str[j]='-';
                    else if(str[j]=='-')
                        str[j] = '+';
                }
                flag = false;
            }
        }
        flag = false;
        for(int i = 0; i < sz ; i++)
        {
            if(str[i]=='-')
            {
                flag = true;
                break;
            }
        }
        if(flag)
            cout<<"Case #"<<cs<<": IMPOSSIBLE"<<endl;
        else
        cout<<"Case #"<<cs<<": "<<ans<<endl;
    }
    return 0;
}
