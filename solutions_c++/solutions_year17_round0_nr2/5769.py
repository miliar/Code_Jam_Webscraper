#include<iostream>
#include<stdio.h>
#include<cstring>
using namespace std;
int main()
{
  freopen("B-large.in","r",stdin);
  freopen("pb.txt","w",stdout);
  int cases,t,index,i;
  char input[30];
  cin>>t;
  for(cases=1;cases<=t;cases++)
  {
    cin>>input;
    for(index=1;input[index]!='\0';index++)
      if(input[index]<input[index-1])
        break;
    if(input[index]=='\0')
    {
      printf("Case #%d: %s\n",cases,input);
      continue;
    }
    input[index]='\0';
    for(i=index-1;i>0;i--)
    {
      if(input[i]!=input[i-1])
        break;
      input[i]='9';
    }
    input[i]--;
    for(i=0;input[i]=='0';i++)
      ;
    printf("Case #%d: %s",cases,input+i);
    cout<<"9";
    for(i=index+1;input[i]!='\0';i++)
      cout<<"9";
    cout<<endl;
  }
  return 0;
}