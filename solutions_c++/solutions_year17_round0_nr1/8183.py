#include <iostream>
#include <set>
#include <algorithm>
#include <vector>
#include <string>
#include <stdio.h>

using namespace std;

#define MOD 1000000007


char flip(char c)
{
    if (c == '-')
    {
        return '+';
    }
    return '-';
}

int main()
{
    freopen("outputGCJ.txt", "w", stdout);
    int t;
    cin>>t;

    for(int Tloop = 1; Tloop <= t; Tloop++)
    {
        string s;
        int k;

        cin>>s>>k;

        int slen = s.length();
        int flipCount = 0;

        for (int i = 0; i <= slen - k; i++)
        {
            if (s[i] == '-')
            {
                flipCount++;
                for (int j = 0; j < k; j++)
                {
                    s[i + j] = flip(s[i + j]);
                }

            }

        }

        bool solved = true;
        for (int i = slen - k + 1; i < slen; i++)
        {
            if (s[i] == '-')
            {
                solved = false;
                break;
            }
        }
        cout<<"Case #"<<Tloop<<": ";
        if (!solved)
        {
            cout<<"IMPOSSIBLE"<<endl;
        }
        else
        {
            cout<<flipCount<<endl;
        }

    }


    return 0;
}
