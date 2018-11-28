#include <iostream>
#include <cstring>
#include <cctype>
#include <cmath>
#include <math.h>
#include <algorithm>
#include <vector>
#include <sstream>
#include <cstdio>

using namespace std;

int main()
{
    freopen("B-large.in","r",stdin);
    freopen("inp.out","w",stdout);
    int t, n,ot;
    string str;
    cin >> t;
    for (int i=0;i<t;i++)
    {
        cin >> str;
        int l=str.size();
        for (int j=0;j<l-1;j++)
        {
            if (str[j]>str[j+1])
            {
                int k=j;
                while ((str[k]-1)<str[k-1])
                {
                    k--;
                    if (k==0){break;}
                }
                str[k]--;
                k++;
                for (;k<l;k++)
                {
                    str[k]='9';

                }



            }



        }
        cout << "Case #" << i+1 << ": ";
        if (str[0]=='0')
        {
            for (int j=1;j<l;j++)
            {
                cout << str[j];
            }
        }
        else{
        cout << str;
        }
        cout << "\n";

    }






}
