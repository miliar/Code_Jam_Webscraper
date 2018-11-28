#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t,k,c=1;
    char str[2000],temp[2000];
    cin>>t;
    while(t--)
    {
        cin>>str>>k;
        strcpy(temp,str);
        int cnt=0,len=strlen(str);
        for(int i=0;i<=len-k;i++)
        {
            if(str[i]=='-')
            {
                cnt++;
                for(int j=0;j<k && i+j<len;j++)
                {
                    if(str[i+j]=='+')str[i+j]='-';
                    else str[i+j]='+';
                }
            }
        }

        for(int i=len-1;i>=0;i--)
        {
            if(str[i]=='-')
            {
                cnt=INT_MAX;
                break;
            }
        }

        strcpy(str,temp);
        int cnt2=0;
        for(int i=len-1;i>=k-1;i--)
        {
            if(str[i]=='-')
            {
                cnt2++;
                for(int j=0;j<k && i-j>=0;j++)
                {
                    if(str[i-j]=='+')str[i-j]='-';
                    else str[i-j]='+';
                }
            }
        }

        for(int i=0;i<len;i++)
        {
            if(str[i]=='-')
            {
                cnt2=INT_MAX;
                break;
            }
        }

        if(cnt==cnt2&&cnt==INT_MAX)cout<<"Case #"<<c++<<": "<<"IMPOSSIBLE"<<endl;
        else cout<<"Case #"<<c++<<": "<<min(cnt,cnt2)<<endl;

    }
    return 0;
}
