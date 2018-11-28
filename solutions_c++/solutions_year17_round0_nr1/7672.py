#include<iostream>
#include<string.h>
using namespace std;

char flip(char c)
{
  if(c=='+') return '-';
  else if(c=='-') return '+';
}

int flip_pancake(char str[],int k)
{
  int pos=0,len;
  for(len=0;str[len]!='\0';len++);
  int result=0;
  for(;pos<len;pos++)
  {
    if(str[pos]=='-')
    {
      if(pos+k<=len)
      {
        for(int i=pos;i<pos+k;i++)
        {
          str[i]=flip(str[i]);
        }
        result++;
        //cout<<str;
      }
      else 
        return -1;
    }
  }
  return result;
}


int main()
{
  int t,res[100],pos=0;
  cin>>t;
  while(t--)
  {
    char str[1000];
    int k;
    cin>>str>>k;
    
    res[pos]=flip_pancake(str,k);
    pos++;
    
  }
  for(int i=0;i<pos;i++)
  {
    if(res[i]!=-1)
      cout<<"Case #"<<i+1<<": "<<res[i]<<endl;
    else
     cout<<"Case #"<<i+1<<": IMPOSSIBLE"<<endl;
 }
}
