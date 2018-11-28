#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <iomanip>

using namespace std;

bool comp(pair<long long,int> l, pair<long long ,int> r)
{
    if(l.first==r.first)
    {
        return l.second>r.second;
    }
    return l.first>r.first;
}
const long double pi = 3.141592653589793238462643383279502884L;
int main()
{
    freopen("A-large (1).in","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin>>t;
    int j=1;
    while(t)
    {
        int n,k;
        cin>>n>>k;
        vector<pair<int,int> >c(n);
        vector<pair<long long,int> >prh(n);
        long long maxR=0,maxRes=0;
        for(int i=0;i<n;i++)
        {
            cin>>c[i].first>>c[i].second;
        }
        sort(c.begin(),c.end(),comp);
        for(int i=0;i<n;i++)
        {
            prh[i].first=2LL*c[i].first*c[i].second;
            prh[i].second=i;
        }
        for(int j=0;j<=n-k;j++)
        {
            sort(prh.begin(),prh.end(),comp);
            long long res=0;
            for(int i=0;i<k-1;i++)
            {
                if(prh[i].second==j)
                {
                    res+=prh[k-1].first;
                    continue;
                }
                res+=prh[i].first;
                //maxR=max(maxR,c[prh[i].second].first);
            }
            //cout<<maxR<<endl;
            res+=1LL*c[j].first*c[j].first+2LL*c[j].first*c[j].second;
            //cout<<res<<endl;
            maxRes=max(maxRes,res);
        }
        printf("Case #%d: ",j);
        cout<<fixed<<setprecision(12)<<pi*maxRes<<endl;
        j++;
        t--;
    }
    return 0;
}
