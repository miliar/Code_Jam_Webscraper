#include <iostream>
#include <stdio.h>

using namespace std;

string makeTidy(string x)
{
    if (x.size()==1)
        return x;
    int i, j;
    for(i=x.size()-1; i>0; i--)
    {
        if(x[i]<x[i-1])
            {
                x[i-1]--;
                for(j=i; j<x.size(); j++)
                    x[j] = '9';
            }
    }
    string y = "";
    if(x[0]=='0')
    {
        for(i=1; i<x.size(); i++)
            y += x[i];
    }
    else
        y = x;
    return y;
}

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int t, i;
    string x, y;
    cin>>t;
    for(i=1; i<=t; i++)
    {
        cin>>x;
        y = makeTidy(x);
        cout<<"Case #"<<i<<": "<<y<<endl;
    }
    return 0;
}














