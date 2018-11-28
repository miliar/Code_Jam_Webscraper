#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;
main()
{
    int t;
    cin>>t;
    for(int ii=1;ii<=t;ii++)
    {
        int n;
        double d;
        cin>>d>>n;
        vector<pair<double,double> > p;
        for(int i=0;i<n;i++)
        {
            double di,s;
            cin>>di>>s;
            p.push_back(make_pair(di,s));
        }
        sort(p.begin(),p.end());
        double ti[n];
        ti[n-1] = (d-p[n-1].first)/p[n-1].second;
        for(int i = n-2; i>=0; i--)
        {
            ti[i] = (d-p[i].first)/p[i].second;
            if(ti[i]<ti[i+1])
                ti[i]=ti[i+1];
        }
        cout.precision(14);
        cout<<"Case #"<<ii<<": "<<d/ti[0]<<endl;
    }
}

