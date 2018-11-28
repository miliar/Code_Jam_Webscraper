#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main()
{
//    freopen("A-large.out","w",stdout);
//    freopen("input.txt","r",stdin);

    int t;
    cin >> t;
    for(int z=0; z<t; z++)
    {
        string s;
        int k;
        cin >> s >> k;
        int i,j,step=0,size=s.size();
        for(i=0; i<=(size-k); i++)
        {
            if(s[i]=='-')
            {
                for(j=i; j<(i+k); j++)
                {
                    if(s[j]=='-')
                        s[j]='+';
                    else
                        s[j]='-';
                }
                step++;
            }
        }
        int flag=0;
        for(i=0; i<size; i++)
        {
            if(s[i]!='+')
            {
                flag=1;
                break;
            }
        }
        if(flag==0)
            cout << "Case #"<< (z+1) << ": "<< step << endl;
        else
            cout << "Case #"<< (z+1) << ": "<< "IMPOSSIBLE" << endl;
    }
    return 0;
}
