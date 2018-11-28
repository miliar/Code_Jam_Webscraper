#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cctype>
#include<algorithm>
#include<cmath>
#include<vector>
#include<string>
#include<queue>
#include<list>
#include<stack>
#include<set>
#include<map>
#define ll long long
#define ull unsigned long long
#define rep(i,n) for(int i = 0;i < n; i++)
#define fil(a,b) memset((a),(b),sizeof(a))
#define cl(a) fil(a,0)
#define pb push_back
#define mp make_pair
#define exp 2.7182818
#define PI 3.141592653589793
#define inf 0x3f3f3f3f
#define fi first
#define se second
#define eps 1e-8
#define mod 1000000007ll
#define sign(x) ((x)>eps?1:((x)<-eps?(-1):(0)))
using namespace std;
double mysqrt(double x) { return max(0.0, sqrt(x)); }
struct node
{
    int pos;
    int v;
    bool operator<(const node&oth) const
    {
        return pos<oth.pos;
    }
}a[1005];

int main() 
{  
    //freopen("1011.in","r",stdin);
    //freopen("001.out","w",stdout);

    int t;
    int k,d;
    int n;
    cin>>t;
    
    for(int z=1;z<=t;++z)
    {
        scanf("%d%d",&d,&n);
        for(int i=1;i<=n;++i)
        {
            scanf("%d%d",&a[i].pos,&a[i].v);
        }
        sort(a+1,a+1+n);
        double ter=-1;
        for(int i=1;i<=n;++i)
        {
            ter=max(ter,(double)(d-a[i].pos)/(double)(a[i].v));
        }
        printf("Case #%d: %.6f\n",z,(double)d/ter);
    }    
    return 0;  
} 


