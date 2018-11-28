#include<bits/stdc++.h>
using namespace std;
int A[20];
int long long num;
int main()
{
    int t;
    scanf("%d",&t);
    for(int tc=1;tc<=t;tc++){
      scanf("%lld",&num);
      int c=0;
      int i;
      int long long x=num;
      while(x)
      {
        A[c+1]=x%10;
        x/=10;
        c++;
      }
      int n=c;
      int todo=0;
      for(i=1;i<=n;i++)
      {
        
        if(todo && A[i]!=0)
        {
         A[i]--;
         todo=0;
        }
        if(A[i]==0 && i<n)
        {
          int pos=i;
          int number=A[i];
           while(pos>0)
           {
            A[pos]=9;
            pos--;
           }
            todo=1;
            continue;
        }
        if(A[i]<A[i+1] && i<n)
        {
          int pos=i;
          int number=A[i];
           while(pos>0)
           {
            A[pos]=9;
            pos--;
           }
           todo=1;
           continue;
        }
      }
      printf("Case #%d: ",tc);
      if(A[n]!=0)
      {
        printf("%d",A[n] );
      }
      for(i=(n-1);i>=1;i--)
      {
        printf("%d",A[i]);
      }
      printf("\n");
    }
    return 0;
}