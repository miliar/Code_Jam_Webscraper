#include <bits/stdc++.h>
#define li long long int
#define INF 1000000009
using namespace std;

int main()
{
    li t;
    cin>>t;
    for(li z=1; z<=t;z++)
    {
        string s;
        li k;
       cin>>s>>k;
       cout<<"Case #"<<z<<": ";
        li co=0;
        li fl=0;
        li n=s.size();
        for(li i=0;i<n;i++)
        {
            if(s[i]=='-')
            {
                for(li j=i; j<i+k;j++)
                {
                    if(j>=n)
                    {
                        fl=1;
                        break;
                    }
                    if(s[j]=='-')
                    {

                        s[j]='+';
                    }
                    else
                    {
                        s[j]='-';
                    }
                }
                if(fl==1)
                {
                    break;
                }

                    co++;
            }
        }
        if(fl==0)
            cout<<co;
        else
            cout<<"IMPOSSIBLE";
    if(z!=t)
        cout<<endl;
    }

}
