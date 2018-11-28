#include <bits/stdc++.h>
using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    int t;
    int caseno=0;
    cin>>t;
    while(t--){
        caseno++;
        double k;
        int d;
        cin>>k>>d;
        vector <pair <double,double> > dist;
        pair <double,double> p;
        for(int i=0;i<d;i++){
            cin>>p.first>>p.second;
            dist.push_back(p);
        }
        sort(dist.begin(),dist.end());
        double ans;
        //small case.
        if(d==1){
            double t1=(k-dist[0].first)/dist[0].second;
            // cout<<k<<" : "<<dist[0].first<<",";
            // cout<<(k-dist[0].first)<<" , "<<dist[0].second<<"@\n";
            // cout<<setprecision(15)<<t1<<"::\n";
            ans=k/t1;
        }
        else{
            double t1=(k-dist[1].first)/dist[1].second;
            double t2=(k-dist[0].first)/dist[0].second;
            if(t2<t1){
                //if intersects before completion
                t2=(dist[1].first-dist[0].first)/(abs(dist[1].second-dist[0].second));
                t2+=(k-dist[1].first-(t2*(dist[1].second)))/dist[1].second;
                t1=t2;
            }
            else{
                t1=t2;
            }
            ans=k/t1;
        }
        cout<<"Case #"<<caseno<<": ";
        cout<<fixed<<setprecision(8)<<ans<<"\n";
    }
    return 0;
}
