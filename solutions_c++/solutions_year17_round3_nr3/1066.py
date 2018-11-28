#include <bits/stdc++.h>
using namespace std;
#define lli long long int
#define lD long double
#define fio ios_base::sync_with_stdio(0)
#define mp(x,y) make_pair(x,y)
#define pb(x) push_back(x)
#define ii pair<int,int>
#define vB vector<bool>
#define vC vector<char>
#define vlD vector<lD>a
#define vvC vector<vC>
#define vi vector<int>
#define vvi vector<vi >
#define vii vector<ii >
#define vvii vector<vii >
#define ll pair<lli,lli>
#define vl vector<lli>
#define vvl vector<vl >
#define vll vector<ll >
#define vvll vector<vll >
#define M_PI 3.14159265358979323846
#define MOD 1000000007
#define MAX 200005
#define EPS 1e-4
#define NINF LONG_MIN
#define INF LONG_MAX
//cout<<"Case #"<<tc<<": ";

int main(){
  lli t,tc=1;
  cin>>t;
  while(t--){
    cout<<"Case #"<<tc<<": ";
    lli n,k;
    cin>>n>>k;
    lD u;
    cin>>u;
    vector<lD> A(n);
    map<lD,lD> mp;
    for(int i=0;i<n;i++){
      cin>>A[i];
      mp[A[i]]++;
    }
    if(n==1){
      cout<<fixed<<setprecision(10)<<min((lD)1,A[0]+u)<<"\n";
      tc++;
      continue;
    }
    while(u){
      
      if(mp.size()==1) break;
      pair<lD,lD> tmp=*mp.begin();
      auto it=mp.find(tmp.first);
      mp.erase(it);
      pair<lD,lD> tmp2=*mp.begin();
      if((tmp2.first-tmp.first)!=0) {
        lD del=min(u,(tmp2.first-tmp.first)*tmp.second);
        u=u-del;
        //cout<<tmp.first<<" ";
        tmp.first=tmp.first+del/tmp.second;
        //cout<<tmp.first<<" ";
        mp[tmp.first]+=tmp.second;
        //cout<<del<<" "<<tmp.first<<" "<<tmp.second<<"\n";
      }
      else break;
      //cout<<u<<"\n";
    }
    if(u){
      lD ans=1;
      lD pp=(*mp.begin()).first+u*1.0/n;
      //cout<<pp<<"\n";
      for(int i=0;i<n;i++){
        ans=ans*pp;
      }
      cout<<fixed<<setprecision(10)<<ans<<"\n";
    }else{
      lD ans=1;
      while(!mp.empty()){
        for(int i=1;i<=(*mp.begin()).second;i++){
          ans=ans*((*mp.begin()).first);
        }
        mp.erase(mp.begin());
      }
      cout<<fixed<<setprecision(10)<<ans<<"\n";
    }
    tc++;
  }
  return 0;
}