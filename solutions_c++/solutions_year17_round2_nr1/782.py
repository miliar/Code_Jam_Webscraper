#include<iostream>
#include<fstream>
#include<iomanip>
#include<vector>
#include<algorithm>
#include<string>
#define cin ifile
#define cout ofile

using namespace std;

int main()
{
    ifstream ifile("A-large (1).in");
    ofstream ofile("out1.txt");
    int t;
    cin>>t;

    for(int fff=1;fff<=t;fff++)
    {
        int d,n;
        cin>>d>>n;

        vector<pair<long double,long double> > arr;
        for(int i=0;i<n;i++)
        {
            int x,s;
            cin>>x>>s;
            arr.push_back(make_pair(x,s));
        }
        sort(arr.begin(),arr.end());


        long double ans=1e18;
        for(int i=0;i<n;i++)
        {
            long double s= d*arr[i].second/(d-arr[i].first);
            ans=min(ans,s);
        }

        cout<<"Case #"<<fff<<": "<<fixed<<setprecision(8)<<ans<<"\n";
    }
    return 0;
}
