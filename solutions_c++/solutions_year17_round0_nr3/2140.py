#include <bits/stdc++.h>
using namespace std;
//#define long long ll
long long mod=1000000007;

int main()
{
    int test;
    cin>>test;
    for(int kk=0;kk<test;kk++)
    {
        cout<<"Case #"<<kk+1<<": ";
        
        long long n,k;
        cin>>n>>k;
        
        vector<pair<long long,long long>> a;
        
        a.push_back(make_pair(n,1));
        
        while(k>0)
        {
            if(k-a[0].second>0)
            {
                long long u,v;
                int f1=0,f2=0;
                if(a[0].first%2==0)
                {
                    u=a[0].first/2;
                    v=u-1;
                }
                else
                {
                  u=a[0].first/2;
                  v=u;
                }
                for(int j=0;j<a.size();j++)
                {
                    if(a[j].first==u)
                    {
                        a[j].second+=a[0].second;
                        f1=1;
                    }
                    if(a[j].first==v)
                    {
                        a[j].second+=a[0].second;
                        f2=1;
                    }
                }
                if(f1==0)
                {
                    if(v==u)
                    {
                        a.push_back(make_pair(u,a[0].second*2));
                        f2=1;
                    }
                    else
                    a.push_back(make_pair(u,a[0].second));
                }
                if(f2==0)
                a.push_back(make_pair(v,a[0].second));
                k-=a[0].second;
                a.erase(a.begin());
                sort(a.rbegin(),a.rend());
            }
            else
            k=0;
            
        }
        if(a[0].first%2==0)
        {
            long long x=a[0].first/2;
            long long y;
            if(x==0)
            y=x;
            else
            y=x-1;
            cout<<x<<" "<<y<<endl;
        }
        else
        {
            long long x=a[0].first/2;
            cout<<x<<" "<<x<<endl;
        }
        
    }
    return 0;
}
