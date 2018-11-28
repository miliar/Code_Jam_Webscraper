//
//  CJ1.cpp
//  
//
//  Created by udita johri on 08/04/17.
//
//

#include <stdio.h>
#include<iostream>
#include<string.h>
using namespace std;
int main()
{
    ios::sync_with_stdio(false);
    int T,x=1;
    cin>>T;
    while(x<=T)
    {
        string str;
        int k,i,j,len,flips=0;
        cin>>str>>k;
        len=str.length();
        for(i=0;i<=len-k;i++)
        {
            if(str[i]=='+')
                continue;
            else
            {
                flips++;
                for(j=i;j<i+k;j++)
                {
                    if(str[j]=='+')
                        str[j]='-';
                    else
                        str[j]='+';
                }
            }
        }
        int f=0;
        for(j=i;j<len;j++)
        {
            if(str[j]!='+')
            {
                f=1;
                break;
            }
        }
        cout<<"Case #"<<x<<": ";
        if(f==1)
            cout<<"IMPOSSIBLE";
        else
            cout<<flips;
        cout<<endl;
        x++;
            
    }
    return 0;
}
