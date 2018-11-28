#include <iostream>
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

int n,m;
string s;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>n;
    int T=0;
    while(n--)
    {
        printf("Case #%d: ",++T);
        cin>>s>>m;
        int l=s.length();
        int ans=0;
        for(int i=0; i<l; i++)
        {
            if(s[i]=='-')
            {
                if(i+m-1<l)
                {
                    ans++;
                    for(int j=i; j<=i+m-1; j++)
                    {
                        if(s[j]=='-')
                            s[j]='+';
                        else
                            s[j]='-';
                    }
                }
                else
                {
                    ans=-1;
                    break;
                }
            }
        }
        if(ans==-1)
        {
            printf("IMPOSSIBLE\n");
        }
        else
        {
            printf("%d\n",ans);
        }
    }

    return 0;
}
