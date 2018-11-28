#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#include<utility>
#include<set>
#include<queue>
#include<list>
#include<stack>

using namespace std;

class Interval{
public:
  int l,r, size;
  
  Interval(int _l, int _r):l(_l),r(_r){
    size=r-l;
  }
  int getPos() const {
    return l+size/2;
  }
};

bool operator<(const Interval& int1,const Interval& int2){
  int int1p=int1.getPos();
  int int2p=int2.getPos();
  int dli1=int1p-int1.l, dri1=int1.r-int1p;
  int dli2=int2p-int2.l, dri2=int2.r-int2p;

  if(min(dli1,dri1)<min(dli2,dri2))
    return true;
  else if(min(dli1,dri1)>min(dli2,dri2))
    return false;
  else{
    if(max(dli1,dri1)<max(dli2,dri2))
      return true;
    else if(max(dli1,dri1)>max(dli2,dri2))
      return false;
    else if(int1.l>int2.l)
      return true;
    return false;
  }
}
      
priority_queue<Interval> pq;
  
void getAns(int n, int k){
  pair<int,int> ans;
  pq.push(Interval(0,n));
  for(int i=1; i<k; i++){
    auto cur=pq.top();
    pq.pop();
    int pos=cur.getPos();
    Interval int1(cur.l,pos),int2(pos+1,cur.r);
    if(int1.size>0)
      pq.push(int1);
    if(int2.size)
      pq.push(int2);
  }
  auto cur=pq.top();
  cout<<cur.getPos()-cur.l<<" "<<cur.r-1-cur.getPos()<<endl;
}
    
    

int main(){

  int T;
  cin>>T;

  

  for(int i=1; i<=T; i++){
    priority_queue<Interval> pq2;
    pq=pq2;
    int n,k;
    cin>>n>>k;
    
    
    cout<<"Case #"<<i<<": ";
    getAns(n,k);
  }

  
  

  return 0;

}
    
