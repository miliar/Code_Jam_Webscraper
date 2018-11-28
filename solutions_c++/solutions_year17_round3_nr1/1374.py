#include<bits/stdc++.h>
using namespace std;
#define ll long long
double n,k,dp[1003][1003],r[10000],h[10000];
pair<double,double> arr[10000];
double rec(ll i,ll kk)
{
     if(kk==k)
     {
          return 0;
     }
     if(i==-1)
     {
          return INT_MIN;
     }
     if(dp[i][kk]!=0)
     return dp[i][kk];
     double ans=rec(i-1,kk);
     double temp2=rec(i-1,kk+1);
     double temp=2*3.141592653589793238462*r[i]*h[i]+temp2;
     if(kk==0)
          temp+=3.141592653589793238462*r[i]*r[i];
    if(temp2==INT_MIN)
        temp=INT_MIN;
     dp[i][kk]=max(temp,ans);
     return max(temp,ans);
}
vector<pair<double,double> >vec;
int main()
{

     freopen("input.txt","r",stdin);
     freopen("output.txt","w",stdout);
     ll t,tt=0;
     cin>>t;
     while(t--)
     {
          tt++;
          //ll n,k;
          cin>>n>>k;
          vec.clear();
          for(int i=0;i<n;i++)
          {
               cin>>arr[i].first>>arr[i].second;
               vec.push_back(arr[i]);
          }
          sort(vec.begin(),vec.end());
          for(int i=0;i<n;i++)
          {
               r[i]=vec[i].first;
               h[i]=vec[i].second;
          }
          memset(dp,0,sizeof(dp));
          cout<<"Case #"<<tt<<": ";
          printf("%.9lf\n",rec(n-1,0));
     }
}
