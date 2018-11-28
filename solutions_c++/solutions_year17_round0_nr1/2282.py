#include <cstdio>
#include <cmath>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <bitset>
#include <string>
#include <set>
#include <stack>
#include <map>
#include <queue>
#include <vector>
using namespace std;


int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T,K;
    string cake;
    cin>>T;
    for(int ca=1; ca<=T; ca++)
    {
        cin>>cake>>K;
        int ans = 0;
        bool flag = true;

        for(int i=0; i<=(cake.length() - K); i++)
        {
            if(cake[i] == '-')
            {
                ans++;
                for(int j=i; j<(i+K); j++)
                {
                    if(cake[j] == '-')
                    {
                        cake[j] = '+';
                    }
                    else
                    {
                        cake[j] = '-';
                    }
                }
            }
        }

        for(int i=(cake.length() - K + 1); i<cake.length(); i++)
        {
            if(cake[i] == '-')
            {
                flag = false;
                break;
            }
        }

        cout<<"Case #"<<ca<<": ";
        if(!flag)
        {
            cout<<"IMPOSSIBLE"<<endl;
        }
        else
        {
            cout<<ans<<endl;
        }
    }
    return 0;
}
