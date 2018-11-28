#include<bits/stdc++.h>
using namespace std;
int main()
{
    ios_base::sync_with_stdio(0);
    freopen ("inp","r",stdin);
    freopen ("outp1","w",stdout);
    int t;
    cin>>t;
    for (int pp=1;pp<=t;pp++)
    {
        long long n,a,b,ans=0;
        long long mn[30],x[30],dp[20][20];
        //cin>>n;
        cin>>a;
        b=a;
        int k=0;
        while(a>0)
        {
            x[k]=a%10;
           // cout<<x[k]<<' ';
            a/=10;
            k++;
        }
       // long long m=x[k-1];
       // for ()
       for (int kk=1;kk<=20;kk++)
       {
      for (int i=k-2;i>=0;i--)
      {
          //cout<<x[i];
          if (x[i]<x[i+1])
          {
              //cout<<'!'<<i<<'!';
              x[i+1]--;
              for (int j=i;j>=0;j--)
                x[j]=9;
              break;
          }
      }
       }
      for (int i=k-1;i>=0;i--)
        ans=ans*10+x[i];
     cout<<"Case #"<<pp<<": "<<ans<<endl;


    }


}

