#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>
#include <unordered_set>
#include <stdio.h>
#include <stdlib.h>
#include <iomanip>
#include <utility> 
using namespace std;
void solve()
{
    cout<<endl;
    int r,c;
    char a[25][25];
    cin>>r>>c;
    for(int i=0;i<r;i++)
    {
        for(int j=0;j<c;j++)
        {
            cin>>a[i][j];
        }
    }
    char lastChar;
    int flag;
    for(int i=0;i<r;i++)
    {
        flag=0;
        for(int j=0;j<c;j++)
        {
            if(a[i][j]!='?')
            {
                flag=1;
                lastChar=a[i][j];
            }
            else
                flag=0;
            if(flag==1 && j>0)
            {
                int k=j-1;
                while(k>=0 && a[i][k]=='?')
                {
                    a[i][k]=lastChar;
                    k--;
                }
            }
            if(flag==1 && j<c-1)
            {
                int k=j+1;
                while(k<c && a[i][k]=='?')
                {
                    a[i][k]=lastChar;
                    k++;
                }
                j=k-1;
            }
        }
    }
    for(int j=0;j<c;j++)
    {
        flag=0;
        for(int i=0;i<r;i++)
        {
            if(a[i][j]!='?')
            {
                flag=1;
                lastChar=a[i][j];
            }
            else
                flag=0;
            if(flag==1 && i>0)
            {
                int k=i-1;
                while(k>=0 && a[k][j]=='?')
                {
                    a[k][j]=lastChar;
                    k--;
                }
            }
            if(flag==1 && i<r-1)
            {
                int k=i+1;
                while(k<r && a[k][j]=='?')
                {
                    a[k][j]=lastChar;
                    k++;
                }
                i=k-1;
            }
        }
    }
    for(int i=0;i<r;i++)
    {
        for(int j=0;j<c;j++)
        {
            cout<<a[i][j];
        }
        cout<<endl;
    }
}
int main() 
{
    int t;
    cin >>t;
    for(int i=1;i<=t;i++)
    {
        cout << "Case #"<<i<<": ";
        solve();
    }
	return 0;
}
