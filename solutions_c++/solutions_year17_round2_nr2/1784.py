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

string comb(string s1, string s2){
  if(s1.size()<s2.size())
    return comb(s2,s1);

  list<char> ls(s1.begin(), s1.end());
  int ct=0;
  for(auto it=ls.begin(); it!=ls.end(); it++){
    if(it!=ls.begin()){
      auto it2=it;
      it2--;
      if(*it2==*it && ct<s2.size()){
	ct++;
	ls.insert(it,s2[0]);
      }
    }
  }
  if(ct!=s2.size()){
    ls.push_back(s2[0]);
    ct++;
    for(auto it=ls.begin(); it!=ls.end() && ct<s2.size(); it++){
      if(it!=ls.begin()){
	auto it2=it;
	it2--;
	if(*it2!=s2[0] && *it!=s2[0]){
	  ls.insert(it,s2[0]);
	  ct++;
	}
      }
    }

  }
  string s(ls.begin(), ls.end());
  return s;

  
  
}
void getAns(int r, int b, int y, int tot){
  if(r>tot/2 || b>tot/2 || y>tot/2){
    cout<<"IMPOSSIBLE"<<endl;
    return;
  }
  
  string rs(r,'R'), bs(b,'B'), ys(y,'Y');
  string ans=comb(rs,bs);
  ans=comb(ans,ys);
  cout<<ans<<endl;  
  

  
      
  
    
    
}


int main(){

  int T;
  cin>>T;  

  for(int i=1; i<=T; i++){
    int n,r,b,y,x;
    cin>>n>>r>>x>>y>>x>>b>>x;
       
    
    cout<<"Case #"<<i<<": ";
    
    getAns(r,b,y,n);
    
    
  }

  
  

  return 0;

}
    
