#include <iostream>
using namespace std;
int ans(string s,int k){
  int i=0;
  while(s[i]=='+'){
    i++;
    if(i==s.length()) break;
  }
  if(i==s.length()) {return 0;}
  else if(i>s.length()-k) {return -1;}
  for(int j=i;j<i+k;j++){
    if(s[j]=='+'){
      s[j]='-';
    }
    else{
      s[j]='+';
    }
  }
  for(int kl=0;kl<=i;kl++) s[kl]='+';
  int answ=ans(s,k);
  if(answ==-1) return -1;
  else return answ+1;
}

int main(){
  int t;
  cin>>t;
  int count[t];
  for(int i=0;i<t;i++){
    string s;
    cin>>s;
    int k;
    cin>>k;
    count[i]=ans(s,k);
  }
  for(int i=0;i<t;i++){
    if(count[i]==-1) cout<<"Case #"<<i+1<<": IMPOSSIBLE"<<endl;
    else cout<<"Case #"<<i+1<<": "<<count[i]<<endl;
  }
}
