#include <cstdio>
#include <cstring>
#include <map>
#include <algorithm>
typedef long long int ll;
#define MAXN 22

char V[MAXN];

void check(char *V,char *vend,char *x)
{
  if(x==V)return;
  if(*x<x[-1])
  {
    std::fill(x,vend,'9');
    x[-1]--;
  }
  return check(V,vend,x-1);
}

void solve()
{
  scanf("%s\n",V);
  check(V,V+strlen(V),V+strlen(V)-1);
  char *x=V;
  while(*x=='0')x++;
  while(*x){putchar(*x);x++;}
  putchar(10);
}

int main()
{
  int T;
  scanf("%d\n",&T);
  for(int i=1;i<=T;i++){printf("Case #%d: ",i);solve();}
}
