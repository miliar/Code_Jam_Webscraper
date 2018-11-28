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
const double pi=acos(-1);
struct cake
{
    double r,h;
};
int cmp(cake a,cake b)
{
    return a.r>b.r;
}
int cmp2(cake a,cake b)
{
    return a.r*a.h>b.r*b.h;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("a.out","w",stdout);
    int t,ca=0;
    scanf("%d",&t);
    while(t--)
    {

        int n,k;
        scanf("%d%d",&n,&k);
        vector<cake>vec(n);
        for(int i=0;i<n;++i)
        {
            scanf("%lf%lf",&vec[i].r,&vec[i].h);
        }
        sort(vec.begin(),vec.end(),cmp);
        double ans=0;
        for(int i=0;i<=n-k;++i)
        {
            double maxr=vec[i].r;

            vector<cake>vec1;
            for(int j=i+1;j<n;++j)
            {
                vec1.push_back(vec[j]);
            }
            sort(vec1.begin(),vec1.end(),cmp2);
            double sumarea=vec[i].r*vec[i].h;
            for(int j=0;j<k-1;++j)
                sumarea+=vec1[j].r*vec1[j].h;
            ans=max(ans,pi*(maxr*maxr+2*sumarea));
        }
        printf("Case #%d: %.10f\n",++ca,ans);
    }
}
