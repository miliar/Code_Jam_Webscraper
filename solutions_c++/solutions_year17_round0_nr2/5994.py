#include <iostream>
#include <sstream>
#include <string>
using namespace std;
string num;
void g(long long int n){
  for(long long int i =n+1;i<num.size();i++){
    num[i]='0';
  }
}

long long int f(){
  long long int i=0;
  for(i=0;i<num.size()-1;i++){
    if(num[i]>num[i+1]){
      break;
    }
  }
  if( i==num.size()-1){
    stringstream ss(num);
    long long int ret;
    ss>>ret;
    return ret;
  }
  char max = num[i];
  while( i && num[i-1] == max )i--;
  g(i);
  stringstream ss(num);
  long long int ret;
  ss>>ret;
  return ret-1;
}


int main(void){
  long long int cnt;
  cin>>cnt;
  for( long long int i = 1;i<=cnt;i++){
    cin>>num;

    cout<<"Case #"<<i<<": "<<f()<<endl;
  }
  return 0;
}
