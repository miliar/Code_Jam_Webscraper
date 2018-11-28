#include <iostream>
#include<cstring>

using namespace std;
char buffer[1005];//use bit operation
int k;
int len;
int cnt_op;

int main()
{
  freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
  int T;
  scanf("%d",&T);
  for(int t= 1; t <= T;t++)
  {

    cnt_op = 0;
    printf("Case #%d: ",t);
    scanf("%s %d",buffer,&k);
    //printf("aaaaa: %s,%d\n",buffer,k);
  len  = strlen(buffer);


  /*  for(int i = 0; i< len;i++)
      if(buffer[i] == '+')
      buffer[i] = 1;
      else buffer[i] = 0;*/

    for(int i = 0; i<= len-k;i++)
    {
      if(buffer[i] == '-')
      {
        cnt_op++;
        for(int j = i; j<i+k;j++)
          buffer[j] = (buffer[j]=='+') ? '-':'+';
    //    printf("rua: %s\n",buffer);
      }
    }
    for(int i = len -k; i < len;i++)
    {
      if(buffer[i] == '-')
      {
        cnt_op = -1;
        break;
      }
    }
    if(cnt_op == -1)
    {
      printf("IMPOSSIBLE\n");
    }
    else printf("%d\n",cnt_op);
  }

return 0;


}
