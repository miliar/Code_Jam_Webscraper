#include<bits/stdc++.h>
using namespace std;

int main()
{
  int n;
  scanf("%d",&n);
  for(int i = 1;i<=n;i++)
  {
    printf("Case #%d: ",i);
    char str[1005];
    int k;
    scanf("%s%d",str,&k);
    int len = strlen(str);
    int cnt = 0;
    for(int j = 0;j<len-k+1;j++)
    {
      if(str[j] == '-')
      {
        for(int l = j;l<j+k;l++)
        {
          str[l] = str[l]=='+'?'-':'+';
        }
        cnt++;
      }
    }
    if(count(str,str+len,'+') == len)
    {
      printf("%d\n",cnt);
    }
    else
    {
      printf("IMPOSSIBLE\n");
    }
  }
}
