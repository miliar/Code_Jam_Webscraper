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
int b[30];
bool check(int*b,int pos)
{
    for(int i=pos;i>=2;--i)
    if(b[i]>b[i-1])return false;
    return true;
}
int main()
{
    fre1();
    int t,cas=1;
    LL n;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%lld",&n);
        int pos=0;
        while(n)
        {
            b[++pos]=n%10;
            n/=10;
        }
        while(true)
        {
            bool flag=false;
            if(check(b,pos))break;
            for(int i=pos; i>=1; --i)
            {
                if(flag)b[i]=9;
                else if(i>1&&b[i]>b[i-1])
                {
                    int tem=i;
                    while(!b[tem])
                    {
                        b[tem]=9;
                        tem++;
                    }
                    b[tem]-=1;
                    flag=true;
                }
            }
//            for(int i=pos;i>=1;--i)putchar('0'+b[i]);
//            puts("");
        }
        while(!b[pos])--pos;
        printf("Case #%d: ",cas++);
        for(int i=pos;i>=1;--i)putchar('0'+b[i]);
        puts("");
    }
    return 0;
}
