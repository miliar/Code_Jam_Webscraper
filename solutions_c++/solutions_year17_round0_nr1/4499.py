

#include<iostream>
#include<algorithm>
#include<memory.h>
#include<stdio.h>
#include<string>
#include<vector>
#include<bitset>
#include<climits>
#include<fstream>

using namespace std;

typedef long long int lli;
typedef unsigned long long int ulli;

int main()
{
    int t,k,flag,ans;
    string s;
    ofstream a_out("a.txt");

    cin>>t;

    for(int i=1;i<=t;i++)
    {
        flag=0;
        ans=0;
        cin>>s;

        cin>>k;

        for(int j=0;j<s.length()-(k-1);j++)
        {
            if(s[j]=='-')
            {
                ans++;
                for(int l=j;l<(j+k);l++)
                {
                    s[l]= '+' + '-' - s[l];
                }
            }
        }

        for(int j=s.length()-(k-1);j<s.length();j++)
        {
            if(s[j]=='-')
            {
                flag=1;
                break;
            }
        }

        if(flag==0)
        {
            cout<<"Case #"<<i<<": "<<ans<<endl;
            a_out<<"Case #"<<i<<": "<<ans<<endl;
        }

        else
        {
            cout<<"Case #"<<i<<": "<<"IMPOSSIBLE"<<endl;
            a_out<<"Case #"<<i<<": "<<"IMPOSSIBLE"<<endl;
        }

    }


    return 0;
}

/*
7
--- 3
---+-++- 3
+++++ 4
-+-+- 4
+-+++++-+ 3
-+++-+-+++-++----++---- 4
---------- 2
*/


