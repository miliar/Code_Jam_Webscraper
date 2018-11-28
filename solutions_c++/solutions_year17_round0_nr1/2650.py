#include<bits/stdc++.h>
using namespace std;
string laundiya;
int kutta,n;
int main()
{
//freopen("input.txt","r",stdin);
//freopen("output.txt","w",stdout);
long long tunda;
cin>>tunda;
for(int pyaaz=1;pyaaz<=tunda;pyaaz++)
{
cin>>laundiya>>kutta;
n=laundiya.size();
bool possible=true;
int jhandubaam=0;
for(int i=0;i<n;i++)
{

  if(laundiya[i]=='+')
  continue;
  else
  {
    if(i+kutta>n)
    { possible=false;break; }
   else
    {
      for(int j=i,l=0;l<kutta;j++,l++)
       (laundiya[j]=='+')?laundiya[j]='-':laundiya[j]='+';
      jhandubaam++;
    }
  }
}

cout<<"Case #"<<pyaaz<<": ";
(possible)?cout<<jhandubaam<<endl:cout<<"IMPOSSIBLE"<<endl;
}

  return 0;
}
