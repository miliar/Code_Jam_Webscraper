#include<bits/stdc++.h>
using namespace std;
#define ll long long int
typedef vector<ll> vi;
typedef pair<ll,ll> ii;
typedef vector<ii> vii;
int main(){
  int T;
  cin>>T;
  for(int t_i=0;t_i<T;t_i++){
    int D,N;
    cin>>D>>N;
    vii v(N);
    for(int i=0;i<N;i++)
      cin>>v[i].first>>v[i].second;
    sort(v.rbegin(),v.rend());
    ll tmpdist=D-v[0].first;
    ll tmpspeed=v[0].second;
    for(int i=1;i<v.size();i++){
      if((D-v[i].first)*tmpspeed>tmpdist*v[i].second)
      {
        tmpdist=D-v[i].first;
        tmpspeed=v[i].second;
      }
  }
  //cout<<tmpdist<<tmpspeed<<endl;
    double ans=(D*tmpspeed*1.0)/tmpdist;
    printf("Case #%d: %lf\n",t_i+1,ans);
  }
  return 0;
}
