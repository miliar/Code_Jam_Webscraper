#include <bits/stdc++.h>
using namespace std;
bool compare(pair<long long,long long>& a,pair<long long,long long>& b)
{
    return a.first>b.first;
}
int main()
{
    int t;
    cin>>t;
    for(int t1=0;t1<t;t1++)
    {
        long long n,k;
        cin>>n>>k;
        vector<pair<long long,long long>> a;
        a.push_back(make_pair(n,1));
        
        while(k>0)
        {
            if(k-a[0].second>0)
            {
                long long x,y,f1=0,f2=0;
                if(a[0].first%2==0)
                {
                    
                    x=a[0].first/2;
                    y=x-1;
                    
                }
                else
                {
                  x=a[0].first/2;
                  y=x;
                }
                 for(int j=0;j<a.size();j++)
                {
                    if(a[j].first==x)
                    {a[j].second+=a[0].second;f1=1;}
                    if(a[j].first==y)
                    {a[j].second+=a[0].second;f2=1;}
                }
                if(f1==0)
                {
                    if(y==x)
                    {a.push_back(make_pair(x,a[0].second*2));f2=1;}
                    else
                    a.push_back(make_pair(x,a[0].second));
                }
                if(f2==0)
                a.push_back(make_pair(y,a[0].second));
                k-=a[0].second;
               //cout<<a[0].first<<" "<<a[0].second<<" "<<x<<" "<<y<<"    " <<k<<endl;
                a.erase(a.begin());
                sort(a.begin(),a.end());
                reverse(a.begin(),a.end());
            }
            else
            k=0;
            
        }
        cout<<"Case #"<<t1+1<<": ";
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

