#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

inline bool comp(double a,double b){
  return a>b;
}

int main(){
  int t,n,d,i,j,k,s;
  cin>>t;
  vector<double> inp;
  double ans;
  for(int zz=1;zz<=t;zz++){
    cin>>d;
    cin>>n;
    for(i=0;i<n;i++){
      cin>>k;
      cin>>s;
      inp.push_back((double)(d-k)/s);
    }
    sort(inp.begin(),inp.end(),comp);
    ans=(double)d/inp[0];
    printf("Case #%d: %.6f\n",zz,ans);
    inp.clear();
  }
}
