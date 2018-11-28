#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include<bits/stdc++.h>
using namespace std;


int main()
{
    int t;
    cin >> t;
    for(int x=0;x<t;x++)
    {
        string s;
        int k;
        cin >> s >> k;
        int i,j,ans=0;
        int size=s.size();
        for(i=0;i<=(size-k);i++)
            {
            if(s[i]=='-')
                {
                for(j=i;j<(i+k);j++)
                    {
                    if(s[j]=='-')
                        s[j]='+';
                    else
                        s[j]='-';
                    }
               
                ans++;
                }
            }
        int flag=0;
        for(i=0;i<size;i++)
            {
            if(s[i]!='+')
                {
                flag=1;
                break;
                }
            }
        if(flag==0)
            cout << "Case #"<< (x+1) << ": "<< ans << endl;
        else
            cout << "Case #"<< (x+1) << ": "<< "IMPOSSIBLE" << endl;
    }
    return 0;
}