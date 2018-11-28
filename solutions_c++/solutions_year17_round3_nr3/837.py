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
int main()
{
    freopen("C-small-1-attempt2.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin>>t;
    int jj=1;

    while(t)
    {
        int n,k;
        cin>>n>>k;
        vector<double>p(n+1,1.0);
        //cout<<n<<"Ggg"<<endl;
        p[n]=1.0;
        double u;
        cin>>u;
        for(int i=0;i<n;i++)
        {
            cin>>p[i];
        }
        sort(p.begin(),p.end());
        long double res=0;
        while(u>0)
        {
            int nextI=0;
            while(nextI<n&&p[0]==p[nextI])nextI++;
            double pl=0.01;
            pl = u/nextI;
            if(pl>p[nextI]-p[0])pl=p[nextI]-p[0];
            //cout<<nextI<<' '<<pl<<endl;
            for(int i=0;i<nextI;i++)
            {
                p[i]+=pl;
                u-=pl;
            }
            if(nextI==n)break;
        }
        res=1.0;
        for(int i=0;i<n;i++)
        {
            res*=p[i];
        }
        printf("Case #%d: ",jj);
        cout<<fixed<<setprecision(7)<<res<<endl;
        jj++;
        t--;
    }
    return 0;
}
