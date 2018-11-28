#include<bits/stdc++.h>
using namespace std;
int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
   freopen("a.in","r",stdin);
   freopen("output.txt","w",stdout);
   int t,i;
   cin>>t;
   i=1;
   while(i<=t){
      long d;
      int n;
      double max_t=0,t;
      cin>>d>>n;
      long k,s;
      while(n--){
        cin>>k>>s;
        t=(double)((double)d-(double)k)/(double)s;
        max_t=max(max_t,t);
;      }
      cout<<fixed<<"Case #"<<i<<": "<<(double)d/max_t<<"\n";
      i++;
   }
   return 0;
}
