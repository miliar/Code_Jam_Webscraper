#include <iostream>
#include <stdio.h>
#include <cstring>
#include<bits/stdc++.h>
using namespace std;

int main()
{
    //ios_base::sync_with_stdio(false);
    //cin.tie(NULL);
    int n,m=0,t,k,i,j,c;
    cin>>t;
    for(m=1;m<=t;m++)
    {
    	string s;
        cin>>s;
        cin>>k;
        c=0;

        for(i=0;i<s.size();i++)
        {
            if(s[i]=='-')
            {
                n=0;
                //cout<<i<<endl;
                for(j=i;(j<(i+k)&&(i+k-1)<s.size()&&(s.size()-i)>=k);j++)
                {
                    if(s[j]=='-')s[j]='+';
                    else
                        s[j]='-';
                    n=1;
                }
                if(n==1)c++;
                //cout<<s<<endl;
            }
        }
        j=0;
        for(i=0;i<s.size();i++)
        {
            if(s[i]=='-')
            {
                j=1;
                break;
            }
        }
        if(j==1)cout<<"Case #"<<m<<": "<<"IMPOSSIBLE"<<endl;
        else
            cout<<"Case #"<<m<<": "<<c<<endl;
    }
}
