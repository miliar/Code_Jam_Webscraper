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

int ct;
void getAns(string s,int k){
  int sz=s.size();
  if(!s.size() || count(s.begin(),s.end(),'+')==sz){
    cout<<ct<<endl;
    return;
  }

  
  if(k>sz && count(s.begin(), s.end(), '+') !=sz){
    cout<<"IMPOSSIBLE"<<endl;
    return;
  }

  auto it=find(s.begin(), s.end(), '-');


  if((s.end()-it)<k){
    cout<<"IMPOSSIBLE"<<endl;
    return;
  }

  ct++;

  for(int i=0; i<k; i++){
    auto it2=it+i;
    if(*it2=='-')
      *it2='+';
    else
      *it2='-';
  }
  
  string s2(it,s.end());
  
  getAns(s2,k);
  
    
    
}


int main(){

  int T;
  cin>>T;

  

  

  for(int i=1; i<=T; i++){
    string s(1001,'a');
    int k;
    cin>>s>>k;
    ct=0;      
    
    cout<<"Case #"<<i<<": ";
    getAns(s,k);
    
    
  }

  
  

  return 0;

}
    
