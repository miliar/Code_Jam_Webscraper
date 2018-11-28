#include <iostream>
#include <cmath>

using namespace std;
int main(){
  /* a = digit  
  *  y = amount to subtract
  */
  unsigned long long n,a,x,aux,y;
  int t,cont;

  cin >> t;
  for(int i = 1; i <= t;++i){
    cin >> n;
    x = n;
    cont = 0;
    do{
      a = x % 10;
      x /= 10;
      if(a < x % 10){
        aux = pow(10,cont);
        y = n - ((n/aux)* aux);
        y++;
        n -= y;
        //PRINT ATTEMPTS
        //cout << n << '\n';
        x = n;
        cont = 0;
        continue;
      }
      cont++;
    }while(x);

    cout << "Case #"<< i << ": " << n << '\n';
  }
}
