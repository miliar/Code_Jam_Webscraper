#include <iostream>
#include <fstream>
#include <stdio.h>
#include <math.h>
#include <algorithm>
#include <iomanip>
#include <bits/stdc++.h>
#define PI 3.14159265
#define MOD 1000000007
using namespace std ;


int main()
{

    #ifndef ONLINE_JUDGE
    freopen("input.txt", "rt", stdin);
    freopen("output.txt", "wt", stdout);
    #else
     online submission
    #endif

    int t;
    cin>>t;
    int m=1;
    while(m<=t)
    {

        int k1,k2, n,i,d,d1;
        cin>>d>>n;
        double mtime=0,dist=0;
        vector < pair < double , double > > p;
        for (i=0;i<n;i++)
        {
            double x;
            double y;
            cin>>x>>y;
            p.push_back(make_pair(x,y));
        }
        int index;
        sort(p.begin(),p.end());
        for (i=0;i<n;i++)
        {
            double x=p[i].first;
            double y=p[i].second;

            double time = (d-x)/y;
            if(time>mtime)
            {
                mtime=time;
                index=i;

            }
        }
         double ans = d/mtime;
         //vector <double> v;
        for (i=0;i<index;i++)
        {
             double tmp = (abs(p[index].first-p[i].first)/abs(p[index].second-p[i].second));
            // cout<<tmp;
             tmp =    (tmp*p[i].second+p[i].first)/tmp;
           //  cout<<tmp;
             if (tmp<ans)
                ans=tmp;
        }
        cout<<fixed;
        cout<<"Case #"<<m<<": "<<setprecision(6)<<ans<<"\n";
        m++;
    }




   return 0;
}
