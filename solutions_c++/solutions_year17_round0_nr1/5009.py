#include <iostream>
#include <stdio.h>

using namespace std;

void mySwap(string &s, int j, int k)
{
    int l;
    for(l=j; l<j+k; l++)
    {
        if(s[l]=='-')
            s[l]='+';
        else
            s[l]='-';
    }
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int t, i, k, counter, j, len;
    string s;
    bool possible;
    cin>>t;
    for(i=1; i<=t; i++)
    {
        possible = true;
        counter = 0;
        cin>>s>>k;
        len = s.size();
        for(j=0; j<=len-k; j++)
        {
            if(s[j]=='-')
            {
                counter++;
                mySwap(s, j, k);
            }
        }
        for(j=len-k+1; j<len; j++)
        {
            if(s[j]=='-')
            {
                possible = false;
                break;
            }
        }
        if(!possible)
        {
            cout<<"Case #"<<i<<": "<<"IMPOSSIBLE"<<endl;
            continue;
        }
        cout<<"Case #"<<i<<": "<<counter<<endl;
    }
    return 0;
}
