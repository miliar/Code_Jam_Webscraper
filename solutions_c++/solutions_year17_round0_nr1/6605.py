#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <string>
using namespace std;
const int maxn=1010;
int test,n,k,a[maxn],ans;
string s;

void flip(int l,int r)
{
    for (int i=l;i<=r;++i) a[i]=-a[i];
}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>test;
    for (int t=1;t<=test;++t)
    {
        ans=0;
        cin>>s>>k;
        n=s.length();
        for (int i=0;i<n;++i)
            if (s[i]=='-') a[i+1]=-1;
            else a[i+1]=1;
        for (int i=1;i<=n-k+1;++i)
            if (a[i]==-1)
            {
                ++ans;
                flip(i,i+k-1);
            }
        for (int i=1;i<=n;++i)
            if (a[i]==-1) ans=-1;
        if (ans==-1) printf("Case #%d: IMPOSSIBLE\n",t);
        else printf("Case #%d: %d\n",t,ans);
    }
    return 0;
}
