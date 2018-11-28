#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen ("A-large.in","r",stdin);
    freopen ("A-large.txt","w",stdout);
    unsigned int xn;
    short s=0;
    cin>>xn;
    string x;
    unsigned int y;
    for(unsigned int i=0;i<xn;i++)
    {
        cin>>x>>y;
        for(unsigned int j=0;j<x.size();j++)
        {
            if(x[j]=='-'&&x.size()-j>=y)
            {
                x[j]='+';
                for(unsigned int c=j+1;c<=j+y-1;c++)
                {
                    if(x[c]=='+')
                    {
                        x[c]='-';
                    }
                    else
                    {
                        x[c]='+';
                    }
                }
                s++;
            }
            else if(x[j]=='-')
            {
                s=-1;
                break;
            }
        }
        cout<<"Case #"<<i+1<<": ";
        if(s==-1)
        {
            cout<<"IMPOSSIBLE";
        }
        else
        {
            cout<<s;
        }
        cout<<endl;
        s=0;
    }
    return 0;
}
