#include<bits/stdc++.h>
using namespace std;
FILE *fin = freopen("in.txt","r",stdin);
FILE *fout = freopen("out.txt","w",stdout);
int main()
{
    double t,n,d,k;
    cin>>t;
    for(k=1;k<=t;k++){

    priority_queue<pair<int,int> > pq;
        cin>>d>>n;
        for(int i=0;i<n;i++)
        {
            double g,h;
            cin>>g>>h;
            pq.push({g,h});
        }
        double ans=(d-pq.top().first)/pq.top().second;
        while(!pq.empty())
        {
            double temp=(d-pq.top().first)/pq.top().second;
            if(temp<ans);
            else ans=temp;
            pq.pop();
        }
        double f=(double)(d/ans);
        cout<<"Case #"<<k<<": "<<setprecision(15)<<f<<endl;
    }
}
