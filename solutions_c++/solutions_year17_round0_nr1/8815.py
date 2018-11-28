#include <iostream>
#include <vector>
#include <algorithm>
#include <string.h>
#define FOR(i,f,c) for(int i=f;i<c;i++)
using namespace std;
string S,sample;
int steps=0;
void Flip(int i , int K)
{
  FOR(j,i,i+K)
  {
    char g = S.at(j);
    switch(g)
    {
      case '+':
      S.at(j) = '-';
      break;
      case '-':
      S.at(j) = '+';
      break;
    }
  }
  ++steps;
}
string GEN(int len)
{
  string sm="";
  FOR(k,0,len)
  {
    sm+="+";
  }
  return sm;
}
int main()
{
  int K,len,y=-1,T;
  cin >> T;
  FOR(t,1,T+1)
  {
    steps=0;
    y=-1;
  cin >> S >> K;
  cout << "Case #" << t <<": ";
  len=S.length();
  sample=GEN(len);
  FOR(i,0,(len-K)+1)
  {
    char e = S.at(i);
    if(e=='-')
    {
      Flip(i,K);
    }
    if(S==sample)
    {
      cout << steps << endl;
      y=0;
      break;
    }
  }
  if(y == -1)
  cout << "IMPOSSIBLE" << endl;
}
  return 0;
}
