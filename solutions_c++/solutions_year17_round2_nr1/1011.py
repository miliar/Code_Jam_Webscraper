#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<algorithm>
#include<set>
#include<map>
#include<queue>
#include<stack>
#include<vector>
#include<iostream>
#include<string>
#include<string.h>
using namespace std;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("a1.out","w",stdout);
    int t,ca=0;
    scanf("%d",&t);
    while(t--)
    {
        int n,d;
        double ans=1e60;
        scanf("%d%d",&d,&n);
        for(int i=0;i<n;++i)
        {
            int k,s;
            scanf("%d%d",&k,&s);
            ans=min(ans,1.0*d*s/(d-k));
        }
        printf("Case #%d: %.10f\n",++ca,ans);
    }
}
