#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <climits>
#include <cstring>
#include <string>
#include <set>
#include <bitset>
#include <map>
#include <queue>
#include <stack>
#include <vector>
#define rep(i,m,n) for(i=m;i<=n;i++)
#define mod 1000000007
#define inf 0x3f3f3f3f
#define vi vector<int>
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define ll long long
#define pi acos(-1.0)
#define pii pair<int,int>
#define sys system("pause")
const int maxn=1e3+10;
const int N=1e3+10;
using namespace std;
ll gcd(ll p,ll q){return q==0?p:gcd(q,p%q);}
ll qpow(ll p,ll q){ll f=1;while(q){if(q&1)f=f*p;p=p*p;q>>=1;}return f;}
int n,m,k,t,cas;
char a[maxn];
int main()
{
    int i,j;
    //freopen("in.txt","r",stdin);
    //freopen("out.txt","w",stdout);
    scanf("%d",&t);
    while(t--)
    {
        scanf("%s%d",a,&k);
        int len=strlen(a),ret=0;
        for(i=0;i+k-1<=len-1;i++)
        {
            if(a[i]=='-')
            {
                ret++;
                for(j=i;j-i+1<=k;j++)a[j]=a[j]=='-'?'+':'-';
            }
        }
        bool flag=true;
        for(;i<len;i++)if(a[i]!='+')flag=false;
        printf("Case #%d: ",++cas);
        if(flag)printf("%d\n",ret);
        else puts("IMPOSSIBLE");
    }
    return 0;
}
