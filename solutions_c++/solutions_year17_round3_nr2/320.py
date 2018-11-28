#include <iostream>
#include <cstdio>
using namespace std;

int Ac,Aj;
int C[200],D[200],J[200],K[200];

void read()
{
  cin >> Ac >> Aj;
  for(int i=0;i<Ac;i++)
    cin >> C[i] >> D[i];
  for(int i=0;i<Aj;i++)
    cin >> J[i] >> K[i];
}

int mod(int a,int n)
{
  return (((a%n)+n)%n);
}

bool good(int s1,int e1,int s2,int e2)
{
  if(s1+720<=1440)
    return s2>=s1 && e2<=s1+720;
  int e = mod(s1+720,1440);
  if(s2>=s1)
    return true;
  return e2<=e;
}

int solve()
{
  if(Ac==1 || Aj==1)
    return 2;
  int S[2],E[2];
  if(Ac==2)
    {
      S[0]=C[0];
      S[1]=C[1];
      E[0]=D[0];
      E[1]=D[1];
    }
  if(Aj==2)
    {
      S[0]=J[0];
      S[1]=J[1];
      E[0]=K[0];
      E[1]=K[1];
    }
  if(good(S[0],E[0],S[1],E[1]))
    return 2;
  if(good(S[1],E[1],S[0],E[0]))
    return 2;
  return 4;
}

int main()
{
  int T;
  cin >> T;
  for(int t=1;t<=T;t++)
    {
      read();
      cout << "Case #" << t << ": " <<solve()<<endl;
    }
  return 0;
}
