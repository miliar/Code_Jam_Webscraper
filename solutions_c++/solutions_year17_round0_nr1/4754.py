#include<iostream>
#include<vector>
#include<string>
#include<stdio.h>
using namespace std;
int main()
{
    int t,l=1;
    cin>>t;
    while(l<=t)
    {
        string s;
        cin>>s;
        int k,i,j,count=0;
        cin>>k;
        for(i=0;i<s.size();i++)
        {
            if(s[i]=='-')
          {
             if(s.size()>=i+k)
            {
                count++;
                for(j=0;j<k;j++)
                {
                    if(s[i+j]=='+')
                        s[i+j]='-';
                    else
                        s[i+j]='+';
                }
            }
            else
                break;
         }

        }
        if(i==s.size())
            cout<<"Case #"<<l<<": "<<count<<endl;
        else
            cout<<"Case #"<<l<<": "<<"IMPOSSIBLE"<<endl;
        l++;
    }
}
