#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int n;
    cin>>n;
    for(int t=1;t<=n;t++)
    {
        int k;
        string str;
        cin>>str>>k;
        bool ss=true;
        for(int i=0;i<str.size();i++)
        {
            if(str[i]=='-')
            {
                ss=false;
                break;
            }
        }
        if(ss)
        {
            cout<<"Case #"<<t<<": 0"<<endl;
            continue;
        }
        long long int ans=0;
        for(int i=0;i<str.size();i++)
        {
            if(str[i]=='-'&&i+k<=str.size())
            {
                ans++;
                for(int j=i+1;j<i+k;j++)
                {
                    if(str[j]=='+')
                        str[j]='-';
                    else
                        str[j]='+';
                }
                str[i]='+';
            }
        }
        ss=true;
        for(int i=0;i<str.size();i++)
        {
            if(str[i]=='-')
            {
                ss=false;
                break;
            }
        }
        if(ss)
        {
            cout<<"Case #"<<t<<": "<<ans<<endl;
            continue;
        }
        for(int i=str.size();i>=0;i--)
        {
            if(str[i]=='-'&&i-k>=0)
            {
                ans++;
                for(int j=i+1;j>i-k;j--)
                {
                    if(str[j]=='+')
                        str[j]='-';
                    else
                        str[j]='+';
                }
                str[i]='+';
            }
        }
        ss=true;
        for(int i=0;i<str.size();i++)
        {
            if(str[i]=='-')
            {
                ss=false;
                break;
            }
        }
        if(ss)
        {
            cout<<"Case #"<<t<<": "<<ans<<endl;
            continue;
        }
        else
        {
            cout<<"Case #"<<t<<": IMPOSSIBLE"<<endl;
        }

    }
    return 0;
}
