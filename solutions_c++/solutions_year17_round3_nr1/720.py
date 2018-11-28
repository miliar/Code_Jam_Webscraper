#include <bits/stdc++.h>
using namespace std;
const int maxn=1e3+10;
pair<int,int> ca[maxn],fir[maxn];
const double pi=acos(-1);
double calc(double ri,double hi)
{
    return 2*pi*ri*hi;
}
typedef pair<int,int> pii;
bool cmp(pii a,pii b)
{
    return calc(a.first,a.second)>calc(b.first,b.second);
}
double solve()
{
    int n,k;
    scanf("%d%d",&n,&k);
    for(int i=1;i<=n;i++)
        scanf("%d%d",&ca[i].first,&ca[i].second);
    sort(ca+1,ca+1+n);
    double ans=0;
    for(int i=k;i<=n;i++)
    {
        for(int j=1;j<i;j++)    fir[j]=ca[j];
        sort(fir+1,fir+i,cmp);
        double tmp=0;
        for(int j=1;j<k;j++)
            tmp+=calc(fir[j].first,fir[j].second);
        tmp+=calc(ca[i].first,ca[i].second)+pi*ca[i].first*ca[i].first;
        ans=max(ans,tmp);
    }
    return ans;
}
int main()
{
    int T,cas=1;
    scanf("%d",&T);
    while(T--)
    {
        printf("Case #%d: %.10f\n",cas++,solve());
    }
    return 0;
}
