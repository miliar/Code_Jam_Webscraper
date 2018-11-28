#include<bits/stdc++.h>
using namespace std;
#define ll long long
pair<double,double> arr[1000000];
double dp1[1000000],dp2[1000000];
int main()
{
     //ios::sync_with_stdio(0);
     freopen("input.txt","r",stdin);
     freopen("output.txt","w",stdout);
     ll t,tt=0;
     cin>>t;
     while(t--)
     {
         tt++;
          ll d,n;
          cin>>d>>n;
          for(int i=0;i<n;i++)
          {
               cin>>arr[i].first;
               cin>>arr[i].second;
               dp1[i]=INT_MAX;
          }
          sort(arr,arr+n);
          for(int i=n-2;i>=0;i--)
          {
               for(int j=i+1;j<n;j++)
               {
                    if(arr[i].second>arr[j].second)
                    {
                         double t=(arr[j].first-arr[i].first)/(arr[i].second-arr[j].second);


                         if(arr[j].second*t>dp1[j])
                         {
                               t=(arr[j].first-arr[i].first-((arr[i].second-arr[j].second)*(dp1[j]/arr[j].second)))/(arr[i].second-dp2[j]);

                         }
                         if(arr[i].second*t+arr[i].first<=d)
                         {

                              if(arr[j].second*t<d)
                              {
                                   if(dp1[i]>arr[i].second*t)
                                   {
                                        dp1[i]=arr[i].second*t;
                                        dp2[i]=arr[j].second;
                                   }
                              }
                         }
                    }
               }
          }

          double t;
          if(dp1[0]==INT_MAX)
          {
               t=(d-arr[0].first)/arr[0].second;
          }
          else
          {
               t=dp1[0]/arr[0].second;
               t+=(d-arr[0].first-dp1[0])/dp2[0];
          }
          cout<<"Case #"<<tt<<": ";
          printf("%.6lf\n",d/t);
     }
}
