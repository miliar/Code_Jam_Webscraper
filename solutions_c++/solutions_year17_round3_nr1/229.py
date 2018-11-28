#include <bits/stdc++.h>
using namespace std;
int main()
{
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    int t;
    cin>>t;
    for(int tt=1;tt<=t;tt++)
    {
        //printf("Case #%d: ",i);
        int n,k;
        cin>>n>>k;
        vector<pair<double,double> > x;
        for(int i=1;i<=n;i++)
        {
            double h,r;
            cin>>r>>h;
            x.push_back(make_pair(r,h));
        }
        sort(x.begin(),x.end());
        vector<double> heap;
        double ca=0;
        double an=0;
        double pi=acos(-1);
        for(int i=0;i<x.size();i++)
        {
            //cout<<ca<<" "<<pi*x[i].first*x[i].first<<" "<<2.0*pi*x[i].second*x[i].first<<endl;
            an=max(an,ca+pi*x[i].first*x[i].first+2.0*pi*x[i].second*x[i].first);
            heap.push_back(-2.0*pi*x[i].second*x[i].first);
            ca+=2.0*pi*x[i].second*x[i].first;
            push_heap(heap.begin(),heap.end());
            while(heap.size()!=0&&heap.size()>k-1)
            {
                ca+=heap[0];
                pop_heap(heap.begin(),heap.end());
                heap.pop_back();

            }
        }
        printf("Case #%d: %.9f\n",tt,an);
    }
}
