#include<iostream>
#include<vector>



using namespace std;


void mktid(string &s){
  for (int i=1; i<s.size(); ++i){
    if (s[i]<s[i-1]){
      s[i-1]-=1;
      for (int j=i; j<s.size(); ++j)
	s[j]='9';
      mktid(s);
    }
  }
  return;
}



int main(){
  int T; cin>>T;
  for (int tc=1; tc<=T; ++tc){
    string s; cin>>s;
    mktid(s);
    

    cout<<"Case #"<<tc<<": ";
    int i=0;
    while(s[i]=='0')
      ++i;
    for (i=i; i<s.size(); ++i)
      cout<<s[i];
    cout<<endl;

  }
  return 0;
}
