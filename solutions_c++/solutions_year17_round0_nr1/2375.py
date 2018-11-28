#include <iostream>
#include <algorithm>
using namespace std;
int main()
{
    int j,t,k,i,count,flag,n,tc;
    string s;
    cin>>t;
    for(tc=1;tc<=t;tc++)
    {
        cout<<"Case #"<<tc<<": ";
        cin>>s>>k;
        n=s.length();
        flag=0;
        count=0;
        for(i=0;i<n;i++)
        {
            if(s[i]=='-')
            {
                if(i<=n-k)
                {
                    count++;
                    for(j=i;j<i+k;j++)
                    {
                        if(s[j]=='-')
                            s[j]='+';
                        else
                            s[j]='-';
                    }
             //       cout<<s<<endl;
                }
                else
                {
                    cout<<"IMPOSSIBLE"<<endl;
                    flag=1;
                    break;
                }
            }
        }
        if(flag==0)
            cout<<count<<endl;
    }
}