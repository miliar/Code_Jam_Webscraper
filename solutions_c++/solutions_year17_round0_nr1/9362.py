#include<iostream>
#include<bits/stdc++.h>
using namespace std;

int main()
{

freopen("A-large.in","r",stdin);
freopen("output.txt","w",stdout);
    int t,case1=1;
    cin>>t;
    int r=0;
    while(t--)
    {
        int k,count=0;
        string str;

        cin>>str>>k;

        for(int i=0;i<str.length();i++)
        {

            if(str[i]=='-')
            {
                if(str.length()-i+1>k)
                {
                    for(int j=0;j<k;j++)
                {
                    if(str[i+j]=='-')
                    str[i+j]='+';
                    else if(str[i+j]=='+')
                        str[i+j]='-';

                }
                count++;

                }
                else
                {
                    count=-1;
                    break;
                }

            }

        }

        if(count==-1)
        {
             cout<<"Case #"<<case1<<": IMPOSSIBLE"<<endl;

        }
        else
        {
            cout<<"Case #"<<case1<<": "<<count<<endl;
        }
        case1++;


    }

}
