#include<bits/stdc++.h>
using namespace std;
const int N=1e3+3;
char A[N];
int main()
{
  int t;
  scanf("%d",&t);
  for(int tc=1;tc<=t;tc++)
  {
    int n,k;
    scanf("%s %d",A+1,&k);
    n=strlen(A+1);
    int i;
    int cnt=0;
    for(i=1;i<=n;i++)
    {
      if(A[i]=='-' && (i+k-1)<=n)
      {
          cnt++;
         for(int j=i;j<=(i+k-1);j++)
         {

          if(A[j]=='-')
          {
            A[j]='+';
          }
          else
          {
            A[j]='-';
          }
         }
      }
    }
    printf("Case #%d: ",tc);
    int flag=0;
    for(i=1;i<=n;i++)
    {
      if(A[i]=='-')
      {
        printf("IMPOSSIBLE\n");
        flag=1;
        break;
      }
    }
    if(!flag)
    {
      printf("%d\n",cnt );
    }
  }
  return 0;
}