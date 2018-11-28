#include<bits/stdc++.h>
using namespace std;

main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        int ans = 0;
        string str;
        cin>>str;
        int k;
        cin>>k;
        for(int j = str.length()-1 ; j>=k-1 ; j--)
        {
            if(str[j]=='-')
                {
                    for(int p=j; p>=j-k+1 && p>=0 ;p--)
                    {
                        if(str[p]=='-')
                            str[p]='+';
                        else
                            str[p]='-';
                    }
                    ans++;
                }
        }
        int status =0;
        for(int j=0;j<str.length();j++)
        {
            if(str[j]=='-')
            {
                cout<<"Case #"<<i<<": "<<"IMPOSSIBLE"<<endl;
                status=1;
                break;
            }
        }
        if(status == 0)
            cout<<"Case #"<<i<<": "<<ans<<endl;
        //cout<<str<<endl;
    }
}
