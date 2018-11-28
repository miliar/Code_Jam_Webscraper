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

    int T,R,C;
    string rec[30];
    cin>>T;
    for(int ca=1;ca<=T;ca++)
    {
        cin>>R>>C;
        for(int i=0;i<R;i++)
        {
            cin>>rec[i];
        }
        for(int i=0;i<R;i++)
        {
            for(int j=0;j<C;j++)
            {
                if(rec[i][j] == '?')
                {
                    for(int k=(j-1);k>=0;k--)
                    {
                        if(rec[i][k] != '?')
                        {
                            rec[i][j] = rec[i][k];
                            break;
                        }
                    }
                    if(rec[i][j] == '?')
                    {
                        for(int k=(j+1);k<C;k++)
                        {
                            if(rec[i][k] != '?')
                            {
                                rec[i][j] = rec[i][k];
                                break;
                            }
                        }
                    }
                }
            }
        }
        for(int i=0;i<R;i++)
        {
            for(int j=0;j<C;j++)
            {
                if(rec[i][j] == '?')
                {
                    for(int k=(i-1);k>=0;k--)
                    {
                        if(rec[k][j] != '?')
                        {
                            rec[i][j] = rec[k][j];
                            break;
                        }
                    }
                    if(rec[i][j] == '?')
                    {
                        for(int k=(i+1);k<R;k++)
                        {
                            if(rec[k][j] != '?')
                            {
                                rec[i][j] = rec[k][j];
                                break;
                            }
                        }
                    }
                }
            }
        }
        cout<<"Case #"<<ca<<":"<<endl;
        for(int i=0;i<R;i++)
        {
            cout<<rec[i]<<endl;
        }
    }
    return 0;
}
