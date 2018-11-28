#include<bits/stdc++.h>
using namespace std;
void flip(int strindx,char s[1000],int k)
{
    for(int i=strindx;i<(strindx+k);i++)
    {
        if(s[i]=='+')
        s[i]='-';
        else
        s[i]='+';
    }
}
int main()
{
  freopen("input.txt","r",stdin);
  freopen("output.txt","w",stdout);
  int t=1,test;
  cin>>t;
  for(test=1;test<=t;test++)
  {
      char s[1000];
      int len,k,i,j,cont=0,flag=0;
      scanf("%s%d",s,&k);
      //cin>>k;
      len=strlen(s);
      //puts(s);
      //cout<<k<<" ";
      for(i=0;i<=len-k;i++)
      {
         if(s[i]=='-')
         {
             flip(i,s,k);
             cont++;
         }

      }
      for(i=len-k;i<len;i++)
      {
          if(((s[i]=='-')&&(s[i+1]=='+'))||((s[i]=='-')&&(s[i-1]=='+')))
          {
              cout<<"Case #"<<test<<": IMPOSSIBLE";
              //puts(s);
              goto abc;
          }
      }
      cout<<"Case #"<<test<<": "<<cont;
      //puts(s);
      abc:
      cout<<"\n";
   }
  return 0;
}
