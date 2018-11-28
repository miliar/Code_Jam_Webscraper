#include<bits/stdc++.h>
#include<string.h>
using namespace std;
char s[50];
int main()
{
  freopen("i.in","r",stdin);
    freopen("o.txt","w",stdout);
  int t;
  scanf("%d",&t);
  for(int x=1;x<=t;x++)
  {
      scanf("%s",s);
      int n=strlen(s);
      int i=0,j;
      while(i<n-1)
      {
          if(s[i]<s[i+1])
             i++;
          else if(s[i]>s[i+1])
          {
              if(s[i]=='1')
                  s[i]='9';
              else
                  s[i]=s[i]-'0'-1+'0';
              break;
          }
          else
          {   j=i+1;
              while(j<n && s[j]==s[i])
              {
                  j++;
              }
              if(j<n){
                 if(s[j]-'0'<s[i]-'0')
                 {
                  if(s[i]=='1')
                    s[i]='9';
                  else
                    {
                        s[i]=s[i]-'0'-1+'0';
                    }
                  break;
                 }
                 else
                    i=j;
              }
              else
              {
                  i=j;
              }
          }
      }
      if(i<n-1)
      {
        if(s[i]!='9')
         {   i++;
             while(i<n)
             {
              s[i]='9';
              i++;
             }
         }
         else
         {   i++;
             while(i<n-1)
             {
                 s[i]='9';
                 i++;
             }
             s[i]='\0';
         }
      }
      printf("Case #%d: %s\n",x,s);
  }
  return 0;
}
