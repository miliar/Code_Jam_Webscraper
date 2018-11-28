#include<iostream>
#include<stdio.h>
#include<cstring>
using namespace std;
int main()
{
  freopen("A-large.in","r",stdin);
  freopen("pa.txt","w",stdout);
  int cases,t,K,i,j,answer,length;
  char str[1001];
  cin>>t;
  for(cases=1;cases<=t;cases++)
  {
    printf("Case #%d: ", cases);
    cin>>str>>K;
    answer=0;
    length=strlen(str);
    for(i=0;i<=length-K;i++)
    {
      if(str[i]=='-')
      {
        for(j=i+1;j-i<K;j++)
        {
          if(str[j]=='-')
            str[j]='+';
          else
            str[j]='-';
        }
        answer++;
      }
    }
    for(i=length-K+1;i<length;i++)
      if(str[i]!='+')
        break;
    if(i<length)
      cout<<"IMPOSSIBLE"<<endl;
    else
      cout<<answer<<endl;
  }
  return 0;
}