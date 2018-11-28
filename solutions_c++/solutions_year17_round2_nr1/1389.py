#include<bits/stdc++.h>
using namespace std;

#define eps 1e-9
#define MAX 1010

typedef pair<double, double> pdd;

vector<pdd> v;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,n,i,j,k,ti;
    double d,tm,ki,si,maxi;
    scanf("%d",&t);
    for(ti=1; ti<=t; ++ti)
    {
        maxi=0;
        v.clear();
        scanf("%lf %d",&d, &n);
        for(i=1; i<=n; ++i)
        {
            scanf("%lf %lf",&ki,&si);
            v.push_back({ki,si});
        }
        sort(v.begin(),v.end());
        for(i=v.size()-1; i>=0; --i)
        {
            tm=(d-v[i].first)/v[i].second;
            maxi=max(maxi,tm);
        }
        printf("Case #%d: %.8lf\n",ti,d/maxi);
    }
    return 0;
}
