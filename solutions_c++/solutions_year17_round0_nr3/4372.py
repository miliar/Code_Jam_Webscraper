#include <iostream>
#include <fstream>
#include <queue>
#include <vector>
using namespace std;
ifstream in("C-small-2-attempt0.in");
ofstream out("C-small-2-attempt0.out");
struct bath{
  int range;
  int ls, rs;
  bath(int range){
    (this->range)=range;
    if(range%2==1){
      (this->ls)=(this->rs)=range/2;
    }
    else{
      (this->ls)=(range-1)/2;
      (this->rs)=(range-1)/2+1;
    }
  }
  bool operator < (bath x){
    return min(ls, rs)<min(x.ls, x.rs) || min(ls, rs)==min(x.ls, x.rs) && max(ls, rs)<max(x.ls, x.rs);
  }
};

struct compare{
  bool operator()(bath const & p1, bath const & p2){
    return min(p1.ls, p1.rs)<min(p2.ls, p2.rs) || min(p1.ls, p1.rs)==min(p2.ls, p2.rs) && max(p1.ls, p1.rs)<max(p2.ls, p2.rs);
  }
};

priority_queue<bath, vector<bath>, compare> vapo;

int main()
{
  int t=0;
  in>>t;
  for(int c=1; c<=t; c++)
  {
    vapo=priority_queue<bath, vector<bath>, compare>();
    int n, p;
    in>>n>>p;
    bath *y=(new bath(n));
    vapo.push(*y);
    bath k=vapo.top();
    for(int i=1; i<p; i++)
    {
      //cout<<(k.range)<<": "<<k.ls<<" "<<k.rs<<endl;
      vapo.pop();
      if(k.range>1){
        bath* l=(new bath(k.ls));
        bath* r=(new bath(k.rs));
        if(l->range!=0)
        vapo.push(*l);
        if(r->range!=0)
        vapo.push(*r);
      }
      k=vapo.top();
    }
    out<<"Case #"<<c<<": "<<(k.rs)<<" "<<(k.ls)<<endl;
  }
}
