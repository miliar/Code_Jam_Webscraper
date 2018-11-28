#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <queue>
using namespace std;
#define INF 0x3f3f3f3f
#define fi first
#define se second
#define mem(a,b) memset((a),(b),sizeof(a))

string s;

void cut(int x)
{
    if(s[x]!='0')
        --s[x];
    else
    {
        s[x]='9';
        cut(x-1);
    }
}

int main()
{
    freopen("/Users/xuehao/Documents/s1/in", "r", stdin);
    freopen("/Users/xuehao/Documents/s1/out", "w", stdout);
    int T;
    scanf("%d",&T);
    for(int cas=1;cas<=T;++cas)
    {
        printf("Case #%d: ",cas);
        cin>>s;
        int len=s.length();
        while(true)
        {
            bool update=false;
            for(int i=0;i<len-1;++i)
            {
                if(s[i]>s[i+1])
                {
                    update=true;
                    cut(i);
                    for(int j=i+1;j<len;++j)
                        s[j]='9';
                    break;
                }
            }
            if(!update)
                break;
        }
        if(s[0]!='0')
            putchar(s[0]);
        for(int i=1;i<len;++i)
            putchar(s[i]);
        putchar('\n');
    }
    
    return 0;
}
