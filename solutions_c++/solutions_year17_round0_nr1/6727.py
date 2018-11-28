#include <iostream>
#include <fstream>
#include <stdio.h>
#include <math.h>
#include <algorithm>
#include <bits/stdc++.h>
#define PI 3.14159265
#define MOD 1000000007
using namespace std ;


int main()
{

    #ifndef ONLINE_JUDGE
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    #else
     online submission
    #endif

    int t;
    cin>>t;
    int m=1;
    while(m<=t)
    {
        char s[1001];
        int k,l,ans=0,i,j;
        bool flag=true;
        cin>>s>>k;
        l = strlen(s);
        for (i=0;i<=l-k;i++)
        {
             if (s[i]=='+')
                continue ;
            ans++;
            for (j=0;j<k;j++)
            {
               if(s[i+j]=='+')
               s[i+j]='-';
               else
               s[i+j]='+';
            }
        }
        for(;i<l;i++)
        {
            if(s[i]=='-')
            {
                flag=false;
                break;
            }
        }
        if(!flag)
        cout<<"Case #"<<m<<": IMPOSSIBLE\n";
        else
        cout<<"Case #"<<m<<": "<<ans<<"\n";
        m++;
    }




   return 0;
}
