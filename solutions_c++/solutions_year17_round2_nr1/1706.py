#include<bits/stdc++.h>
using namespace  std;

int main()
{
freopen("in.txt","r",stdin);
freopen("out.txt","w",stdout);
int curr=1;
    int t;
    cin>>t;
    while(t--)
    {
        //vector<pair<long long int ,long long int > > v;
        long long int d,n;
        cin>>d>>n;
        double mintime=-1;
        for(int i=0;i<n;i++)
        {
          long long int first,second;
          cin>>first>>second;
          double c=(((d-first)*1.0)/second);
          mintime=max(mintime,c);

        }

        cout<<"Case #"<<curr<<": "<<fixed<<setprecision(6)<<((d*1.0)/mintime)<<"\n";
curr++;
    }
}
