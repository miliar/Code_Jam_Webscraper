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
#define lowbit(x) (x&-x)//取x二进制数最小的1
#define MS(x,y) memset(x,y,sizeof(x))
#define lrt rt<<1
#define rrt rt<<1|1
#define lson ll,mid,lrt
#define rson mid+1,rr,rrt
#define Keytree (ch[ch[root][1]][0])
#define rep(i,a,b) for(int i=a;i<=b;++i)
#define dwn(i,a,b) for(int i=a;i>=b;--i)
inline void fre1()
{
    freopen("C:\\Users\\Administrator\\Desktop\\in.txt","r",stdin);/*freopen("output.txt","w",stdout);*/
    freopen("C:\\Users\\Administrator\\Desktop\\out.txt","w",stdout);
}
const LL mod=1e9+7;
const int maxn=1e7+20;
const int INF=1e9+8;
const int N=1e7;
const double PI=acos(-1);
const double EPS=1e-7;
struct node{
    LL le,len;
    bool operator<(const node&rhs)const{
        if(len!=rhs.len)return len<rhs.len;
        return le>rhs.le;
    }
};
priority_queue<node>Q;
int main()
{
    fre1();
    int t,cas=1;
    LL n,k;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%lld%lld",&n,&k);
        while(!Q.empty())Q.pop();
        Q.push(node{0LL,n});
        for(int i=1;i<=k;++i)
        {
            node tem=Q.top();
            Q.pop();
            //printf("%lld %lld\n",tem.le,tem.len);
            if(i==k)printf("Case #%d: %lld %lld\n",cas++,tem.len/2,(tem.len-1)/2);
            else {
              Q.push(node{tem.le,(tem.len-1)/2});
              Q.push(node{tem.le+tem.len/2,tem.len/2});
            }
        }
    }
    return 0;
}
