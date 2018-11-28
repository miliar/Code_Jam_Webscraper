#include<iostream>
using namespace std;
int minflipping,flag=0;
void sol(int K,string S,int i,int count)
{
  if(i>S.length()-K)
  {
    for(int z=0;z<S.length();z++)
    {
      if(S[z]=='-')
        return ;
    }
    flag=1;
    minflipping=min(minflipping,count);
    return;  

  }
  sol(K,S,i+1,count);
  for(int j=i;j<K+i;j++)
  {
      if(S[j]=='+') S[j]='-';
      else          S[j]='+';
  }
  sol(K,S,i+1,count+1);
  for(int j=i;j<K+i;j++)
  {
      if(S[j]=='+') S[j]='-';
      else          S[j]='+';
  }

  
}
int main()
{
  int T,i=1;
  cin>>T;
  while(T--)
  {
    string S;
    cin>>S;
    int K; 
    cin>>K;
    flag=0;
    minflipping=100000000;
    sol(K,S,0,0);
    if(flag==1)
    cout<<"Case #"<<i<<": "<<minflipping<<endl;
    else 
      cout<<"Case #"<<i<<": "<<"IMPOSSIBLE"<<endl;
    i++;
  }
  return 0;
}