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
    char s[20];
    char ans[20];
    cin>>s;
    int i,lf=0,index=0;
    char prev='0';
    int len=strlen(s);
    for(i=0;i<len;i++)
    {
        if(lf==1)
        {
            ans[i]='9';
        }
        else
        {
            if(s[i]>=prev)
            {
                prev=s[i];
                ans[i]=s[i];
            }
            else
            {
                ans[i-1]--;
                int index=i-1;
                char next=ans[index];
                index--;
                while(index>=0 && ans[index]>next)
                {
                    ans[index]--;
                    next=ans[index];
                    ans[index+1]='9';
                    index--;
                }
                lf=1;
                ans[i]='9';
            }
        }   
    }
    ans[i]='\0';
    int k=0;
    if(ans[0]=='0')
    {
        k++;
    }
    while(k<len)
    {
        cout<<ans[k++];
    }
    cout<<endl;
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

