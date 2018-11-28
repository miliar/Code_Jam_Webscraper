#include<iostream>
#include<stdio.h>
#include<string>
#include<set>
#include<queue>
#include<stack>
#include<algorithm>
#include<limits.h>
#include<cmath>
#include<vector>
#include<iomanip>
#include<unordered_map>
using namespace std;

int main()
{
    freopen("A-large (3).in","r",stdin);
    freopen("data.out","w",stdout);
    cout<<setprecision(9)<<fixed;
    int t,a=0;
    cin>>t;
    while(t--)
    {
        a++;
        vector<pair<long double,long double> >vec;
        int n;
        long double dest,u,v,time=0;
        cin>>dest>>n;
        for(int i=0;i<n;i++)
        {
            cin>>u>>v;
            long double ti=(dest-u)/v;
            if(ti>time)
                time=ti;
        }

        long double ans=dest/time;
        cout<<"Case #"<<a<<": ";
        cout<<ans<<endl;
    }

    return 0;
}
