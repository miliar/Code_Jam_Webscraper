#include <iostream>
#include<cstring>
#define ll long long
using namespace std;


int num[25]; // from lowest to highest
int changed[25];
int main()
{
  freopen("in.txt","r",stdin);
  freopen("out.txt","w",stdout);
  int T;
  ll n;
  scanf("%d",&T);
  for(int t= 1; t <= T;t++)
  {
    memset(changed,0,sizeof(changed));
    printf("Case #%d: ",t);
    scanf("%lld",&n);
     num[0] = 0;
    //ll tmp;
    while(n)
    {
      num[++num[0]] = n%10;
      n/=10;
    }
    if(num[0] == 1)
    {
      printf("%d\n",num[1]);
      continue;
    }
    int new_num[25];
    for(int i = 1; i<= num[0];i++)
    {
      new_num[i] = num[num[0]+1-i];
    }
    new_num[0]= num[0];
    for(int i = new_num[0]; i >= 2;i--)
    {
      if(new_num[i] < new_num[i-1])
      {
        if(new_num[i-1] >= 1)
        {
          new_num[i-1] -=1;
          for(int x = i; x <= new_num[0];x++)
          new_num[x] = 9;
        }
        else
        {
          //bool find = false;
          for(i = i-2; i >= 1; i--)
          {
            if(new_num[i] >=1)
            {
              new_num[i]-=1;
              for(int j = i+1; j <= new_num[0];j++)
                new_num[j] = 9;
              break;
            }
          }

        }
      }
    }
    int l = 1;
    for(; l<= new_num[0];l++)
    {
      if(new_num[l]!=0)
      break;
    }
    for(; l<= new_num[0];l++)
    printf("%d",new_num[l]);
    printf("\n");


  }
return 0;


}
