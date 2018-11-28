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
//#define rep(i,a,b) for (int i=(a),_ed=(b);i<_ed;i++)
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
#define eps 1e-7
#define mod 1000000007ll
using namespace std;
const int LEN = 1005;
int k;
int num;
int n;
int dir[LEN];
int f[LEN];
int cal(int k)
{
    cl(f);
    int res=0;
    int sum=0;
    for(int i=0;i+k<=n;++i)
    {
        if((dir[i]+sum)%2!=0)
        {
            res++;
            f[i]=1;
        }
        sum+=f[i];
        if(i-k+1>=0)
        {
            sum-=f[i-k+1];
        }
    }
    for(int i=n-k+1;i<n;++i)
    {
        if((dir[i]+sum)%2!=0) return -1;
        if(i-k+1>=0)
        {
            sum-=f[i-k+1];
        }
    }
    return res;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output1.out","w",stdout);
    string in;
    
    cin>>num;
    for(int z=1;z<=num;++z)
    {
        
        cin>>in;
        cin>>k;
        n=in.size();
        for(int i=0;i<in.size();++i)
        {
            if(in[i]=='-') dir[i]=1;
            else dir[i]=0;
        }
        int res=cal(k);
        printf("Case #%d: ",z);
        if(res==-1) printf("IMPOSSIBLE\n");
        else printf("%d\n",res);
    }
    return 0;
}