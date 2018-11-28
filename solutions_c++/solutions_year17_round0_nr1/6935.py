#include <string>
#include <iostream>

using namespace std;

int main(){
  int T;
  cin>>T;
  for(int ix=0;ix<T;ix++){
    cout<<"Case #"<<ix+1<<": ";
    string s;
    cin>>s;
    int k;
    cin>>k;
    int n = 0,i;
    for(i=0;i<s.length();i++){
      if(s[i] == '-'){
        if(i + k > s.length()){
          cout<<"IMPOSSIBLE"<<endl;
          break;
        }
        else{
          for(int j=0;j<k;j++)
            s[i+j] = s[i+j] == '-'?'+':'-';
          n++;
        }
      }
    }
    if(i == s.length()){
      cout<<n<<endl;
    }
  }
  return 0;
}
