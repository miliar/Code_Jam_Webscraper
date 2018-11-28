#include <iostream>

using namespace std;

bool validar(int n);

int main()
{
  long long T, N,i,j;
  bool numero;
  cin>>T;
  for(i=0;i<T;i++)
  {
    cin>>N;
    for(j=N;j>0;j--)
    {
      numero=validar(j);
      if(numero)
      {
        cout<<"Case #"<<i+1<<": "<<j<<endl;
        break;
      }
    }
  }
}
bool validar(int n)
{
  int digito, digito1;
  digito1=n%10;
  n/=10;
  while(n>0)
  {
    digito=n%10;
    n/=10;
    if(digito1<digito)
    {
      return false;
    }
    digito1=digito;
  }
  return true;
}
