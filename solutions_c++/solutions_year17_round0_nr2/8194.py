#include <bits/stdc++.h>

using namespace std;

int main(){
  int t;
  long long n;
  cin>>t;
  int caso = 1;
  long long bizu;
  long long aux;
  int last;
  int aux2;
  long long base;
  while(t--){
    cin>>n;
    cout<<"Case #"<<caso++<<": ";
    bizu = 0;
    aux = 0;
    last = 9;
    base = 1;
    while(n!=0){
      aux2 = n%10;
      if(aux2>last){
        aux2--;
        bizu = aux;
      }
      bizu += base*aux2;
      last = aux2;
      aux+=base*9;
      base*=10;
      n/=10;
    }
    cout<<bizu<<endl;
  }
  return 0;
}