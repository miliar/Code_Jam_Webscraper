#include<iostream>
#include<stdio.h>
#include<queue>
using namespace std;
void sol(int n,int k,int i)
{
   priority_queue<int> pq;
   pq.push(n);
   int a,b;
   while(k--)
   {
      int tmp=pq.top();
      a=tmp/2;
      b=tmp-1-a;
      pq.push(a);
      pq.push(b);
      pq.pop();
   }
   printf("Case #%d: %d %d",i,max(a,b),min(a,b));
   
}
int main()
{
  int T,i=1;
  scanf("%d",&T);
  
  while(T--)
  {
    int n,k;
    scanf("%d %d",&n,&k);
    sol(n,k,i);
    cout<<endl;
    i++;

    
  }
  return 0;
}