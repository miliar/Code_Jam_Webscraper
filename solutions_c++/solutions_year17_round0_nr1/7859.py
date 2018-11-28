#include<bits/stdc++.h>
#include<string.h>
using namespace std;
int main()
{
    int t,e;
//ofstream outFile;

//outFile.open("output.txt");
    scanf("%d",&t);
    for(e=1;e<=t;e++)
    {
      char s[1005];
      int k;
      scanf("%s",s);
      scanf("%d",&k);
      int j=0,c=0,i;
      int l=strlen(s);
      int d=0;
      while(j<=strlen(s)-k)
      {
          if(s[j]=='+')
          {
              d++;
              j++;
              continue;
          }
          else
          {
              c++;
              for(i=j;i<j+k;i++)
              {
                  if(s[i]=='-')
                    s[i]='+';
                  else
                    s[i]='-';
              }
              d++;
              j++;
              continue;
          }
      }
      for(i=j;i<strlen(s);i++)
      {
          if(s[i]=='+')
            d++;
      }
      if(d==strlen(s))
      {
          //outFile<<"Case #"<<e<<": "<<c<<"\n";
          printf("Case #%d: %d\n",e,c);
      }
        else
        {
           //outFile<<"Case #"<<e<<": "<<"IMPOSSIBLE"<<"\n";
           printf("Case #%d: IMPOSSIBLE\n",e);
        }
    }
    return(0);
}
