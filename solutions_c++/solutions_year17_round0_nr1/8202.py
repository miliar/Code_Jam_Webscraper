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
    freopen("A-large.in","r",stdin);
    freopen("inp.out","w",stdout);
    int t,k;
    string str;
    cin >> t;
    for (int i=0;i<t;i++)
    {
        int cnt=0;
        cin >> str;
        cin >> k;
        int l=str.size();
        for (int j=0;j<=l-k;j++)
        {

            if (str[j]=='-')
            {

                for (int x=j;x<(k+j);x++)
                {

                    if (str[x]=='+'){str[x]='-';}
                    else {str[x]='+';}
                }
                cnt++;
                /*for (int m=0;m<l;m++)
            {
                cout << str[m] << " ";
            }
            cout << "\n";*/
            }

        }
        int c=1;
        for (int j=0;j<l;j++)
        {
            if (str[j]=='-'){c=0;break;}
        }

        cout << "Case #" << i+1 << ": ";
        if (c){
        cout << cnt << "\n";
        }
        else {cout << "IMPOSSIBLE\n";}
    }






}
