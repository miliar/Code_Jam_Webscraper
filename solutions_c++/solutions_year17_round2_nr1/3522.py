#include <cstdio>
#include <iostream>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <string.h>
#include <string>
#include <vector>
#include <queue>

using namespace std;
typedef long long ll;
const int INF=1e9+7;
const int MAXN=1e4+7;
int n,m,T;
pair<int,int> a[MAXN];
int main()
{
    scanf("%d",&T);
    double ta,tb;
    for(int kase=1;kase<=T;kase++)
    {
        scanf("%d%d",&m,&n);
        for(int i=0;i<n;i++)
            scanf("%d%d",&a[i].first,&a[i].second);
        sort(a,a+n);
        double ans=0;

        for(int i=n-1;i>=0;i--)
        {
            ta=(double)(m-a[i].first)/a[i].second;
            if(ta>ans)
                ans=ta;
        }
        printf("Case #%d: ",kase);
        printf("%.6f\n",m/ans);
    }
    return 0;
}
