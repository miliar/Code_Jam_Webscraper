#include <bits/stdc++.h>
#define mp make_pair
#define op(a) "Case #"<<a<<": "
#define ll long long
using namespace std;
struct comp{
   bool operator()(ll a,ll b){
          return a>b;
   }
};
ll min(ll a,ll b){return a<b?a:b;}
ll max(ll a,ll b){
  return a<b?b:a;
}
pair<ll ,ll> fn1(ll n,ll k){
ll r,y;
 // if(k==n/2) return mp(1,0);
  if(k==n )  return mp(0,0);
 multiset<ll,comp>ms;
 multiset<ll,comp>:: iterator ii;
 ms.insert(n);
while(k--){
  ii=ms.begin();
  if(*ii==1) return mp(0,0);
  ll x= *ii;
  //cout<<x<<endl;
   ms.erase(ii);
    r=(x-1)/2;
    y =x-1-r;
   ms.insert(r);
   ms.insert(y);
}
ii =ms.begin();
ll s=max(r,y);
ll z=min(r,y);
 return mp(s,z);
}
int main(int argc, char const *argv[])
{
	ifstream fin("C-small-2-attempt0.in");
    ofstream fout("C-small-2-attempt0.out");
     int No_testCase; fin>>No_testCase;
  
    for(int test_id=1;test_id<=No_testCase;test_id++){    
       ll n,k; 
       fin>>n>>k;
      pair<ll,ll> w=fn1(n,k);
       fout<<"Case #"<<test_id<<": "<<w.first<<" "<<w.second<<endl;
    }
	return 0;
}