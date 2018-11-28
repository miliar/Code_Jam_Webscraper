#include <bits/stdc++.h>
using namespace std;

int main(){
  long long int t,n;
  string num;
  stringstream mystream;
  bool nao = false;
  scanf("%lld",&t);
  long long int cont = 1, aux;
  long long int j = 1;
  while(cont<=t){
    scanf("%lld",&n);
    aux = n;
    while(1){
      mystream.str("");
      mystream << aux;
      num = mystream.str();
      for(long long int i = 0 ; i < num.length()-1 ; i++){
        if(!(num[i]-'0'<=num[i+1]-'0')){
          nao=true;
          break;
        }
      }
      if(!nao)
        break;
      nao=false;
      aux--;
    }
    cout << "Case #" <<cont<< ": " << num <<endl;
    nao=false;
    cont++;
  }
  return 0;
}
