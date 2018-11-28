#include <iostream>
#include <vector>
#include <cstring>
#include <map>
#include <algorithm>
#include <math.h>
#include <CMATH>
#include <iostream>     // std::cout, std::fixed
#include <iomanip>
using namespace std;
typedef long long ll;
const double PI  =3.141592653589793238463;

int main()  {
    ios_base::sync_with_stdio(false);
    int T;
    cin>>T;
    for(int t=0;t<T;t++)
    {
    int n,k;
    cin>>n>>k;
    vector<pair<double,pair<double, double>>> hr(n);
    for(int i=0;i<n;i++)
    {
        double r,h;
        cin>>r>>h;
        hr[i].first=r*h;
        hr[i].second.first=r;
        hr[i].second.second=h;

    }
    sort(hr.begin(),hr.end(),greater<pair<double, pair<double, double>>>());
    double maxsol=0;
    for(int i=0;i<n;i++)
    {
        pair<double, pair<double, double>> cur=hr[i];
        int num=k-1;
        double sol=PI*cur.second.first*cur.second.first;
        sol+=2*PI*cur.first;
        for(int j=0;j<n && num>0;j++)
        {
            if(i==j)continue;
            if(hr[j].second.first<=cur.second.first)
            {
                sol+=2*PI*hr[j].first;
                num--;
            }
        }
        if(num!=0)continue;
        maxsol=max(maxsol,sol);
    }
        cout<<"Case #"<<t+1<<": ";
        cout<<fixed<<setprecision(10)<<maxsol;
        cout<<endl;
    }

    return 0;
}
