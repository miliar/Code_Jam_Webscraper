#include<iostream>
#include<string>

using namespace std;

string str;
int K;

void g(int n){
  for( int i=0;i<K;i++){

    if( str[i+n] == '-')str[i+n]='+';
    else      str[i+n]='-';
  }
}

int f(){
  int res = 0;
  for( int i = 0;i<str.size()-K+1;i++){
    if(str[i]=='-'){
      g(i);
      res++;
    }
  }
  for( int i = 0;i<str.size();i++){
    if( str[i]=='-')res=-1;
  }
  return res;
}

    

int main(void){
  int T;
  cin>>T;
  for( int cnt = 1;cnt<=T;cnt++){
    cin>>str>>K;
    cout<<"Case #"<<cnt<<": ";
    int tmp= f();
    if(tmp>=0) cout<<tmp<<endl;
    else cout<<"IMPOSSIBLE"<<endl;
  }
  return 0;
}
