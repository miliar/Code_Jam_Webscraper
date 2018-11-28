#include<iostream>
#include<stdlib.h>
#include<string>
#include<stdio.h>
#include<vector>
#include<algorithm>

using namespace std; 

struct e {
  long double p;
  long double s;
  e(long double p_,long double s_){
    p = p_;s = s_;
  }
  e(){

  }
};

bool dcomp(e a,e b){
  return a.p < b.p;
}


int main(){
  int T;
  cin>>T;
  for(int t = 1 ; t <= T; ++t){
    long double D, N;
    cin>>D>>N;    
    long double s_min = 100001;
    long double p_min = -1;

    vector<e> v(N);
    for(int i = 0;i<N;++i){
      double s,p; 
      cin>>p>>s;
      v[i].p = p;
      v[i].s = s;
    }

    sort(v.begin(),v.end(),dcomp);       

    for(int j = N-1; j >0 ; --j){
      if(v[j].s > v[j-1].s || v[j].s == v[j-1].s  ){
        if( p_min  > -1 &&  ((D-v[j-1].p) / v[j-1].s) > ((D-p_min) / s_min) ){
          s_min = v[j-1].s; p_min = v[j-1].p; 
        } else if(p_min == -1 ){
          s_min = v[j-1].s; p_min = v[j-1].p;
        }
        continue;
      }

      if( ((D-v[j].p) / v[j].s) >= ((D-v[j-1].p) / v[j-1].s) ){
        //slower horse takes more time
        if( p_min == -1 || ((D-p_min) / s_min) <= ((D-v[j].p) / v[j].s) )
        {s_min = v[j].s; p_min = v[j].p;
        }
      }else{
        if( p_min == -1 || ((D-p_min) / s_min) <= ((D-v[j-1].p) / v[j-1].s) ){
          s_min = v[j-1].s;
          p_min = v[j-1].p;
        }
      }    
    }

    if( p_min == -1 ||  ((D-v[0].p) / v[0].s) >= ((D-p_min) / s_min)){
      s_min = v[0].s;
      p_min = v[0].p; 
    }    

    printf("Case #%d: %6Lf",t,D/((D - p_min)/s_min));
    if(t < T){
      cout<<endl;
    }
  }


}
