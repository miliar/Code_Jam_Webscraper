#include<bits/stdc++.h>
using namespace std;
#define rep(i,a,b) for(int (i)=(a);(i)<=(b);++i)
#define repd(i,a,b) for(int (i)=(a); (i)>=(b);--i)
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define ll long long int
#define mod 1000000007

long double pi=3.14159265359;

//double dp[1000][1000];
int main()
{freopen("abc.in","r",stdin);
freopen("output3.txt","w",stdout);

    int t=100,ti;
    cin>>t;
    rep(ti,1,t)
    {
     int n,k,i,j;
     cin>>n>>k;
  long   double r[1005],h[1005];
    vector<pair<long double,pair<int,long double>>> V;
     for(i=0;i<n;i++)
     {
         cin>>r[i]>>h[i];
         V.push_back({2.0*r[i]*pi*h[i],{i,r[i]}});
     }
     sort(V.begin(),V.end());
     reverse(V.begin(),V.end());
     long double ans,temp;
     ans=temp=0;
     int x;
    long double maxr=0;
     for(i=0;i<n;i++)
     {
         temp = 2.0*r[i]*pi*h[i] ;
      //cout<<temp<<endl;
         x=1;
         maxr =  r[i];
         for(j=0;j<n;j++)
         {
              if(x>=k)
                break;
                //cout<<i<<" "<<V[j].second.first<<endl;
             if(V[j].second.first != i)
             {
                 temp = temp + V[j].first;
               // cout<<V[j].first;
                 x++;
                 maxr = max(maxr,V[j].second.second);
             }

         }
        // cout<<pi*maxr*maxr<<endl;;
         ans = max(temp + pi*maxr*maxr,ans);
      //   cout<<ans<<endl<<endl;
     }






        cout<<setprecision(20)<<showpoint<<"Case #"<<ti<<": "<<ans<<endl;


    }
        return 0;
}
