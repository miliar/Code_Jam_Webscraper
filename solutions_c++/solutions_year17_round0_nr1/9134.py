#include <iostream>
#include <string>

using namespace std;

int main()
{
  string S;
  int T,K,i,j,n;
  bool cambio;
  cin>>T;
  for(i=0;i<T;i++)
  {
    cin>>S>>K;
    int conta=0;
    cambio=true;
    while(cambio)
    {
      cambio=false;
      for(j=0;j<S.size();j++)
      {
        if(S[j]=='-' && j+K<=S.size())
        {
          ++conta;
          cambio=true;
          for(n=j;n<j+K;n++)
          {
            if(S[n]=='-')
            {
              S[n]='+';
            }
            else
            {
              S[n]='-';
            }
          }
          break;
        }
      }
    }
    cambio=true;
    for(n=0;n<S.size();n++)
    {
      if(S[n]=='-')
      {
        cambio=false;
        cout<<"Case #"<<i+1<<": IMPOSSIBLE"<<endl;
        break;
      }
    }
    if(cambio)
    {
      cout<<"Case #"<<i+1<<": "<<conta<<endl;

    }
  }
}
