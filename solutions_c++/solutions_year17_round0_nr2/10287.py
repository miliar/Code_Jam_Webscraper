#include <bits/stdc++.h>
using namespace std;

bool ordenado(string s)
{
  for(int i=0;i<s.size()-1;++i)
  {
    if(s[i]>s[i+1])
    {
      return false;
    }
  }
  return true;
}

string numero(int n)
{
  while(true)
  {
    stringstream ss;
    ss<<n;
    if(ordenado(ss.str()))
    {
      return ss.str();
    }
    n--;
  }
}

int main()
{
  int casos=0, caso=1, N;
  cin>>casos;
  while(casos--)
  {
    cin>>N;
    printf("Case #%d: ",caso++);
    cout<<numero(N)<<endl;
  }
  return 0;
}
