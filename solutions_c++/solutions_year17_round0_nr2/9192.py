#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main()
{
    ofstream file;
    file.open ("large");

    int t;
    cin>>t;
    for(int i=0; i<t; i++)
    {
        string s;
        cin>>s;
        for(int b=0; b<s.size(); b++)
        for(int j=0; j<s.size()-(b+1); j++)
        {
            if(s[j]==' ' || s[j+1]==' ')
                continue;
            int x=s[j]-48,  y=s[j+1]-48;
            if(y<x)
            {
                x--;
                s[j]=(char)x+48;
                for(int a=j+1; a<s.size(); a++)
                    s[a]='9';
            }
        }
        int f=0;
        file<< "Case #"<<i+1<<": ";
        for(int i=0; i<s.size(); i++)
        {
            if(s[i]=='0' && f==0)
                continue;
            else
            {
                file<<s[i];
                f=1;
            }
        }
        file<<endl;
    }
    file.close ();
    return 0;
}
