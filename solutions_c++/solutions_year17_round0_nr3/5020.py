#include <bits/stdc++.h> 
using namespace std;
#define ll long long int
#define gearchange() cin.tie(0),cerr.tie(0),ios_base::sync_with_stdio(0)
#define MOD 1000000007LL

int main()
{
  gearchange();
   int t;
   cin>>t;
   int y=0;
   while(t--){
        y++;
        ll n,k;
        cin>>n>>k;
        ll x= log2(k);
        ll slot=(1LL<<x);
        x= (1LL<<x)-1;
        n=n-x;
        k= k-x;
        ll fia;
        ll rem= n%slot;
        ll per= n/slot;
        if(rem>=k){ fia=per+1; }
        else{ fia= per;}
        ll a,b;
        if(fia&1){
          a= (fia-1)/2;
          b=a;
        }
        else{
          a= fia/2;
          b=a-1;
        }

       cout<<"Case #"<<y<<": ";
       cout<<a<<" "<<b<<endl;
   }
  return 0;
}