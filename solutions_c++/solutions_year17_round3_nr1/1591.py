#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#include<utility>
#include<set>
#include<queue>
#include<list>
#include<stack>
#include<iomanip>

const double PI=3.141592653593;

using namespace std;
class Pancake{
public:
  double r,h;
  Pancake(double _r, double _h):r(_r),h(_h){}
};

double getArea(vector<Pancake>& vp){
  double ans=0;
  for(auto& p:vp){
    ans+=2*PI*p.r*p.h;
  }
  ans+=vp[0].r*vp[0].r*PI;
}

  

void getAns(vector<Pancake> vp, int k, int N){
  sort(vp.begin(), vp.end(),[](auto p1, auto p2){return p1.r>p2.r;});
  double ans=0;
  
  for(int i=0; i<N; i++){
    vector<Pancake> vp2(vp.begin()+i+1,vp.end());
    if(vp2.size()<k-1) break;
    sort(vp2.begin(), vp2.end(),[](auto p1, auto p2)
	 {return p1.r*p1.h>p2.r*p2.h;});
    vector<Pancake> vp3;
    
    vp3.push_back(vp[i]);
    for(int j=0; j<k-1; j++){
      vp3.push_back(vp2[j]);
    }
    //cout<<getArea(vp3)<<endl;
    ans=max(ans,getArea(vp3));
  }
  cout<<setprecision(12)<<ans<<endl;
    
    
    
}


int main(){

  int T;
  cin>>T;  

  for(int i=1; i<=T; i++){
        
    int n,k;
    cin>>n>>k;
    vector<Pancake> vp;
    for(int i=0; i<n; i++){
      double r,h;
      cin>>r>>h;
      vp.push_back(Pancake(r,h));
    }
    
    cout<<"Case #"<<i<<": ";
    getAns(vp,k,n);
    
    
  }

  
  

  return 0;

}
    
