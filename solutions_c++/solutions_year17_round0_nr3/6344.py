#include<iostream>
#include<stdlib.h>
#include<string> 
#include<stdint.h>
#include<queue>
#include<vector>
#include<algorithm>
using namespace std; 

struct elem{
  int64_t pos;   
  int64_t val; 

  elem(){
    pos = -1; 
    val = -1; 
  }
  elem(int64_t p, int64_t v){
    pos = p;
    val = v; 
  }

}; 


struct comparator{

  bool operator()(struct elem &e1 , struct elem  &e2){
    if(e1.val < e2.val)
      return true; 
    else if ( e1.val > e2.val){
      return false;
    } else {
      return e1.pos > e2.pos ; 
    }
  }

};

bool compare (pair<int64_t,int64_t> &l,pair<int64_t,int64_t> &r){
  return l.first > r.first;
}

int main(){

  int64_t T; 
  cin>>T; 

  for(int64_t i = 0 ; i < T ; ++i){  
    int64_t N,K;
    cin>>N>>K;
    vector<pair<int64_t,int64_t> > v; 
    int64_t s = 0; 
    int64_t l=0; 
    while(K > (s+ (1<<l)) ){
      s = s+(1<<l);
      l++;     
    }

   // cerr<<"level "<<l<<endl; 
    int64_t c = 0 ; 
    v.push_back(pair<int64_t,int64_t>(N,1)); 
    for(int64_t i = 0 ; i < l;++i){
      vector< pair<int64_t,int64_t> > v1; 
      for(int64_t j = 0 ; j < v.size();++j){
        pair<int64_t,int64_t> l(v[j].first/2,v[j].second*2);
        pair<int64_t,int64_t> r(v[j].first/2,v[j].second*2); 
        if(v[j].first % 2 == 0){
          l.first-=1;   
        }
        v1.push_back(l);
        v1.push_back(r); 
      }
      v = v1; 
    }
   // cerr<<"c: "<<c<<endl;
   // cerr<<" v.size(): "<<v.size()<<endl; 
    sort(v.begin(),v.end(),compare);
    c= v.size() -1; 
    K -= c;    
   // cerr<<"new K:"<<K<<endl;
    int64_t la,ra; 
    la = v[K-1].first/2;
    ra =la; 
    if(v[K-1].first%2 == 0 ){
      la= la-1; 
    }

    cout<<"Case #"<<i+1<<": "<< ra<<" "<<la<<endl;      
  }

}
