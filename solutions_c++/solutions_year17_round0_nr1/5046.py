#include <iostream>
#include <bits/stdc++.h>
using namespace std;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large output.in","w",stdout);
    int t,i,j,flag,k,count=0;
    string s;
    cin>>t;
    for(int c=1;c<=t;c++)
    {
        count=0;
        cin>>s;
        cin>>k;
        for(i=0;i<=(s.length()-k);i++)
        {
            if(s[i]=='-')
            {
                count++;
                j=i;
                while(j<i+k)
                {
                    if(s[j]=='-')
                        s[j]='+';
                    else if(s[j]=='+')
                        s[j]='-';

                    j++;
                }
            }

        }
        i=s.length()-k+1;
        flag=0;
        for(;i<s.length();i++)
        {
            if(s[i]=='-')
            {
                flag=1;
                break;
            }
        }
        cout<<"Case #"<<c<<": ";
        if(flag==1)
            cout<<"IMPOSSIBLE"<<endl;
        else
            cout<<count<<"\n";
    }
}
