#include<iostream>
#include<map>
#include<algorithm>
#include<vector>
using namespace std;
#define pres(d,e)((d).find(e)!=(d).end())
int main(){
  int t;
  cin>>t;
  for(int i=1;i<=t;i++){
    long long  n,k;
    cin>>n>>k;
    map<long long,int> a;
    a[n]=1;
    for(int j=0;j<=k-2;j++){
      typeof(a.rbegin()) x = a.rbegin();
      long long max = x->first;
      long long rs = (max)/2;
        long long ls = (max-1)/2;
      if(pres(a,ls)) {
         a[ls]++;
      }
      else {
         a[ls] = 1;
      }

      if(pres(a,rs)) {
         a[rs]++;
      }
      else {
         a[rs] = 1;
      }
      if(a[max]==1) {
         a.erase(max);
      }
      else {
         a[max]-=1;
      }
    }
    typeof(a.rbegin()) x = a.rbegin();
      long long max = x->first;
      long long maxin = (max-1)/2;
      long long minin = (max)/2;
      cout<<"Case #"<<i<<": "<<minin<<" "<<maxin<<"\n";
  }
}
