#include <bits/stdc++.h>
#define endl '\n';
using namespace std;
typedef long long int LL;

int main()
{
  ios_base::sync_with_stdio(false);cin.tie(0);

  freopen("input.txt","r",stdin); freopen("output.txt","w",stdout);

  int tc;cin>>tc;for(int t=1;t<=tc;t++)
  {    
     cout<<"Case #"<<t<<": ";
     

     int d,n;
     cin>>d>>n;

     vector<long double>r;

     for(int i=0;i<n;i++)
     {
     	long double x,s;
     	cin>>x>>s;
     	r.push_back(((d-x)/s));
     }

    sort(r.begin(),r.end());
    reverse(r.begin(),r.end());
     
    long double speed = d/r[0];
    cout<<fixed<<setprecision(7)<<speed<<endl;
  }
          
  return 0;
}