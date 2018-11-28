#include<bits/stdc++.h>
using namespace std;
int main()
{
  int t,nt=1;
  cin>>t;
  while(nt <= t)
   {
    long long d,i,n,j;
    double t=0.0;
    cin>>d>>n;
    long long p[n],s[n];
    for(i=0LL;i<n;i++)
      {
        long long a,b;
        cin>>a>>b;
        p[i]=a; s[i]=b;
      }
      t= (double ) (d- p[n-1LL])/s[n-1LL] ;
    for(i=n-2LL;i>=0LL;i--)
       {
          long long t2;
          t2 =( double   ) ((d- p[i])/ s[i] );
          if( t2 > t )
              t= t2 ;

       }
      double v= (double)(d) ;
      double ans = v/t ;
      cout<<"Case #"<<nt<<": "<<ans<<endl;
      nt++;
   }

}