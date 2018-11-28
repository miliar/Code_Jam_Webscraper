#include<bits/stdc++.h>
using namespace std;
int main()
{
  int n;
  scanf("%d",&n);
  for(int i = 1;i<=n;i++)
  {
    printf("Case #%d: ",i);
    char str[20];
    scanf("%s",str);
    int len = strlen(str);
    if(is_sorted(str,str+len))
    {
      printf("%s\n",str);
    }
    else
    {
      while(!is_sorted(str,str+len))
      {
        for(char* not_sorted = is_sorted_until(str, str+len);not_sorted!=str+len;++not_sorted)
        {
          *not_sorted = '0';
        }
        long long int a;
        sscanf(str,"%lld",&a);
        sprintf(str,"%lld",--a);
        len = strlen(str);
      }
      printf("%s\n",str);
    }
  }
}
