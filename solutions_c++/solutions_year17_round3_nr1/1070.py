#include <bits/stdc++.h>
using namespace std;

vector<pair<long long,long long> >v;
vector<long long> v2;

bool comp(long long i,long long j)
{
    return i>j;
}

int main() 
{
    int t,n,k,c=1,i,j,r,h;
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    cin>>t;
    long double pi=3.141592653589793238;
    while(t>0)
    {
        v.clear();
        cout<<"Case #"<<c<<": ";
        ++c;
        cin>>n>>k;
        for(i=0;i<n;++i)
        {
            cin>>r>>h;
            v.push_back({r,h});
        }
        long double ans=0.0;
        long long x;
        for(i=0;i<n;++i)
        {
            v2.clear();
            for(j=0;j<n;++j)
            {
                if(i!=j && v[j].first<=v[i].first)
                {
                    v2.push_back(v[j].first*v[j].second);
                }
            }
            x=v[i].first*v[i].second;
            
            
            if(v2.size()>0 && v2.size()>=k-1)
            {
                sort(v2.begin(),v2.end(),comp);
                
                for(j=0;j<k-1;++j)
                {
                    x=x+v2[j];
                }
                
            }
            
                ans=max(ans,(long double)((long double)(2*pi*x)+(long double)pi*v[i].first*v[i].first));
        }
        printf("%.9Lf\n",ans);
        --t;
    }
	return 0;
}

