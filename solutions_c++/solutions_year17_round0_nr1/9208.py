#include<set>
#include<map>
#include<list>
#include<stack>
#include<queue>
#include<ctime>
#include<cmath>
#include<vector>
#include<cstdio>
#include<string>
#include<cstring>
#include<iostream>
#include<algorithm>
#define X first
#define Y second
#define sc scanf
#define pr printf
#define MP make_pair
#define PB push_back
#define lson l,m,i<<1
#define rson m+1,r,i<<1|1
#define mem(a,b) memset(a,b,sizeof(a))
using namespace std;

typedef double db;
typedef long long ll;

const int N=1010;
char s[N];

int main()
{
    #ifdef Jove
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    #endif // Jove

    int T;
    sc("%d",&T);
    for(int TT=1;TT<=T;TT++)
    {
        pr("Case #%d: ",TT);

        int k;
        sc("%s%d",s,&k);

        int n=strlen(s);

        int ans=0;
        bool flag=0;
        queue<int>q;

        for(int i=0;i<n;i++)
        {
            while(!q.empty() && i>=q.front()) q.pop();

            int now=q.size()+((s[i]=='+')?0:1);

            //pr("%d %d\n",i,now);

            if(now%2)
            {
                if(i+k>n) flag=1;
                q.push(i+k);
                ans++;
            }
        }

        if(flag) puts("IMPOSSIBLE");
        else pr("%d\n",ans);
    }

    return 0;
}

