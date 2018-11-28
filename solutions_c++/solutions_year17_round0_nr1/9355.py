#include<iostream>
#include<bits/stdc++.h>

using namespace std;

int main()
{
    int t,k,ctr,in;
    string s;
    cin>>t;
    in=t;
    while(t--)
    {   ctr=0;
        cin>>s>>k;
        for(int i=0;i<s.length();i++)
        {
            if(s[i]=='-')
            {   ctr++;
                for(int j=i;j<i+k;j++)
                {
                    if(j>=s.length())
                        ctr = -1;
                    if(s[j]=='-')
                        s[j]='+';
                    else
                        s[j]='-';
                }
            }
        }
        if(ctr==-1)
            cout<<"Case #"<<in-t<<": IMPOSSIBLE"<<endl;
        else
            cout<<"Case #"<<in-t<<": "<<ctr<<endl;
    }
}
