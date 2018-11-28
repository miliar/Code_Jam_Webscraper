#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t,x=0,flag,k,ct,i,j,l;
    char str[2000];
    cin>>t;
    while(t--)
    {
        x++;

     cin>>str>>k;
     flag=0;
     l=strlen(str);
     ct=0;
        for(i=0;i<l;i++)
        {
            if(str[i]=='-')
            {
                ct++;
                for(j=i;j<i+k;j++)
                {
                if(j==l)
                    {
                        flag=-1;
                        break;
                    }
                if(str[j]=='-')
                    str[j]='+';
                else
                    str[j]='-';

                }
            }
            if(flag==-1)
            break;
    }
    cout<<"Case #"<<x<<": ";
    if(flag==-1)
        cout<<"IMPOSSIBLE\n";
    else
        cout<<ct<<"\n";
        //Case #1: 3
    }
    return 0;
}
