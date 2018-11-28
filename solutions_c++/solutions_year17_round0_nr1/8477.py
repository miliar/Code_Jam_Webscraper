//
//  main.cpp
//  GoogleCodeJam
//
//  Created by yujian liu on 4/6/17.
//  Copyright © 2017 yujian liu. All rights reserved.
//
#include <iostream>  // includes cin to read from stdin and cout to write to stdout
using namespace std;  // since cin and cout are both in namespace std, this saves some text
int main() {
    int t, n, m, flag=0;
    cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
    for(auto i=0;i<t;i++)
    {
        string s;
        int res=0;
        cin >> s >> n;
        for(m=0;m<=s.size()-n;m++)
        {
            if(s[m]=='-')
            {
                res++;
                for(int k=0;k<n;k++)
                {
                    if(s[k+m]=='-')
                    {s[k+m]='+';}
                    else
                    {s[k+m]='-';}
                }
            }
        }
        cout<<"Case #"<<i+1<<": ";
        while(m<s.size())
        {
            if(s[m]=='-')
            {
                flag=1;
            }
            m++;
        }
        m=0;
        if(flag==1)
        {
            cout<<"IMPOSSIBLE"<<endl;
        }
        else
        cout<<res<<endl;
        res=0;
        flag =0;
    }
    return 0;
}
