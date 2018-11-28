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

string  getAns(string s){
  if(s.size()==1)
    return s;
  int n=s.size();
  reverse(s.begin(),s.end());
  for(int i=1; i<n; i++){
    if(s[i-1]<s[i]){
      for(int j=0;j<i; j++){
	s[j]='9';
      }
      s[i]--;
    }
  }
  reverse(s.begin(),s.end());
  if(s[0]=='0')
    return s.substr(1);
  return s;
}


int main(){

  int T;
  cin>>T;
  
  for(int i=1; i<=T; i++){
    string s(30,'a');
    cin>>s;
    cout<<"Case #"<<i<<": "<<getAns(s)<<endl;
  }

  
  

  return 0;

}
    
