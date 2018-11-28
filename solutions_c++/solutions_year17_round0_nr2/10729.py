#include <cstdlib>
#include <iostream>
#include <fstream>
#define lint unsigned long long int
using namespace std;

bool isTidy(lint n){
  lint num=n%10;
  n/=10;
  while(n>0){
    //cout<<n<<endl;
    if(num<n%10)
      return false;
    num=n%10;
    n/=10;
  }
  return true;
}


int main(){
  ifstream in("input.txt");
  ofstream out("output.txt");
  int T;
  in>>T;
  lint N;
  for(int i=0;i<T;i++){
    out<<"Case #"<<i+1<<": ";
    in>>N;
    while(!isTidy(N))
      N--;
    out<<N<<endl;
  }
}
