/**

¼ªÁÖ´óÑ§
Jilin U

Author:     sinianluoye (JLU_LiChuang)
Date:        2015-3
Usage:

**/

#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>

#define ll long long
#define eps 1e-8
#define ms(x,y) (memset(x,y,sizeof(x)))
#define fr(i,x,y) for(int i=x;i<=y;i++)
#define sqr(x) ((x)*(x))

using namespace std;

const int maxn = 1e3+10;

int Solve(char* val,int n)
{
    int len = strlen(val) - n + 1;
    int ret = 0;
    for(int i=0;i<len;++i)
    {
        if(val[i] == '-')
        {
            for(int j=0;j<n;++j)
            {
                if(val[i+j]=='+')
                    val[i+j]='-';
                else
                    val[i+j]='+';
            }
            ++ ret;
        }
    }
    for(int i=len;val[i];++i)
        if(val[i]=='-')
            return -1;
    return ret;
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A.out","w",stdout);
    char ch[maxn];
    int n;
    int T;
    cin>>T;
    for(int cas = 0;cas < T;++cas)
    {
        printf("Case #%d: ",cas+1);
        scanf("%s%d",ch,&n);
        int ans = Solve(ch,n);
        if(ans != -1)
            cout << ans << endl;
        else
            cout << "IMPOSSIBLE" << endl;
    }
}

/*************copyright by sinianluoye (JLU_LiChuang)***********/
