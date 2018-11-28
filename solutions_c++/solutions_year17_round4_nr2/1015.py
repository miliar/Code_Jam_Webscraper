#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <map>
#include <vector>
using namespace std;
#define pii pair<int,int>
#define mp make_pair
#define pb push_back

vector<int> vec[1010];
int n,c,m;
int h[1010];

int calc(int ans)
{
    memset(h,0,sizeof(h));
    int ret=0;
    for (int i=1;i<=c;++i)
        if (vec[i].size()>0)
        {
            for (vector<int>::iterator it=vec[i].begin();it!=vec[i].end();++it)
            {
                int x=*it;
                while (h[x]==ans) --x;
                if (x<1) return -1;
                ++h[x];
                if (x!=*it) ++ret;
            }
        }
    return ret;
}

int main()
{
    freopen("B.in","r",stdin);
    freopen("B.out","w",stdout);
    int t,x,y;
    scanf("%d",&t);
    for (int cas=1;cas<=t;++cas)
    {
        scanf("%d%d%d",&n,&c,&m);
        fill(vec,vec+c+1,vector<int>());
        for (int i=1;i<=m;++i)
        {
            scanf("%d%d",&x,&y);
            vec[y].pb(x);
        }
        int l=1,r=m;
        for (int i=1;i<=c;++i) l=max(l,(int)vec[i].size());
        while (l<r)
        {
            int mid=(l+r)>>1;
            if (calc(mid)!=-1) r=mid;
            else l=mid+1;
        }
        printf("Case #%d: %d %d\n",cas,l,calc(l));
    }
    return 0;
}
