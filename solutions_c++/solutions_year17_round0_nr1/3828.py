#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<algorithm>
#include<cstdlib>
#include<string>
#include<stack>
#include<vector>
#include<queue>
#include<map>
#include<sstream>
using namespace std;
typedef long long LL;
typedef pair<int,int> pii;
inline void fre1()
{
    freopen("C:\\Users\\Administrator\\Desktop\\in.txt","r",stdin);/*freopen("output.txt","w",stdout);*/
    freopen("C:\\Users\\Administrator\\Desktop\\out.txt","w",stdout);
}
inline void fre2()
{
    fclose(stdin);/*fclose(stdout);*/
}
#define lowbit(x) (x&-x)//取x二进制数最小的1
#define MS(x,y) memset(x,y,sizeof(x))
#define lrt rt<<1
#define rrt rt<<1|1
#define lson ll,mid,lrt
#define rson mid+1,rr,rrt
const LL mod=1e9+7;
const int maxn=1e5+20;
const int INF=1e9+8;
const double PI=acos(-1);
const double EPS=1e-7;
char s[1010];
int main()
{
    //fre1();
    int t,k,cas=1;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%s%d",s+1,&k);
        int len=strlen(s+1),ans=0;
        bool flag=true;
        for(int i=1; i<=len; ++i)
        {
            if(s[i]=='+')continue;
            if(i+k-1>len)break;
            ans++;
            for(int j=i; j<=i+k-1; ++j)s[j]=(s[j]=='+'?'-':'+');
        }
        for(int i=1; i<=len; ++i)
            if(s[i]=='-')
            {
                flag=false;
                break;
            }
        printf("Case #%d: ",cas++);
        if(flag)printf("%d\n",ans);
        else printf("IMPOSSIBLE\n");
    }
    return 0;
}
