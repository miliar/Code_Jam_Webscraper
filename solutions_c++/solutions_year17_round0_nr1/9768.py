#include<stdio.h>
#include<stdlib.h>
#include<iostream>
#include<string.h>
using namespace std;
int T;
char S[120][20];
int K[120];
int main()
{
freopen("A-small-attempt0.in","r+",stdin);
freopen("A-small-attempt0.out","w+",stdout);
cin>>T;
for(int i=0;i<T;i++)
{
cin>>S[i];
cin>>K[i];

bool has0;
bool output=false,back=false;
int counter=0;
while(!output)
{
//First Phase
has0=false;
for(int j=0;j<S[i][j];j++)
{
if(S[i][j]=='-')
{
    has0=true;
    break;
}
}
if(!has0)
{
    cout<<"Case #"<<i+1<<": "<<counter<<"\n";
    break;
}
//phase 2
int consk=0;
bool Swap=false;
int j;
for(j=0;j<S[i][j];j++)
{
 if(S[i][j]=='-')
  {
      consk++;
      if(consk==K[i])
        {
            Swap=true;
            counter++;
            break;
        }
  }
  else
    consk=0;
}
if(Swap)
{
for(int sw=j-K[i]+1;sw<=j;sw++)
{
    S[i][sw]='+';
}
}
else
{
int len=strlen(S[i]);
for(j=0;j<S[i][j];j++)
{
if(S[i][j]=='-')
{
if(j+K[i]<=len && !back)
{
for(int sw=j;sw<j+K[i];sw++)
{
    if(S[i][sw]=='+')
        S[i][sw]='-';
    else
        S[i][sw]='+';
}
counter++;
break;
}
else
{
back=true;
for(j=len-1;j>=0;j--)
{
if(S[i][j]=='-')
{
if(j-K[i]>=-1)
{
for(int sw=j;sw>j-K[i];sw--)
{
    if(S[i][sw]=='+')
        S[i][sw]='-';
    else
        S[i][sw]='+';
}
counter++;
break;
}
else
{
cout<<"Case #"<<i+1<<": "<<"IMPOSSIBLE"<<"\n";
output=true;
break;
}
}
}
}

}
//output=true;

}

}
}
}
//cout<<data[0];
return 0;
}

