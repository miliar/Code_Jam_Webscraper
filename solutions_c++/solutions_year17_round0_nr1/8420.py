#include<stdlib.h>
#include<iostream>
#include<string.h>

using namespace std;

int main()
{
    int t,i;
    cin>>t;
    for(i=1;i<=t;i++)
    {
        int ans=0,k,j,lastC=0;
        char str[1002];
        cin>>str>>k;
        int l=strlen(str);

        for(j=0;j+k<=l;j++)
        {
            if(str[j]=='-')
            {
                for(int p=0;p<k;p++)
                {
                    if(str[j+p]=='-')
                        str[j+p]='+';
                    else
                        str[j+p]='-';
                }
                ans++;
            }
        }
        for(;j<l;j++)
        {
            if(str[j]=='-')
                break;
        }
        if(j<l)
            cout<<"Case #"<<i<<": "<<"IMPOSSIBLE"<<endl;
        else
            cout<<"Case #"<<i<<": "<<ans<<endl;
    }
}
