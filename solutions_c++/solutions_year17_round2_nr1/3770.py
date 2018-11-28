#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("A-large (1).in","r",stdin);
    
	freopen("output.txt","w",stdout);
    
    int t;
    scanf("%d",&t);
    int h=1;
    while(t--)
    {
      double n,i,d,x,y;
      double j,min=0.0;
      scanf("%lf",&d);
      scanf("%lf",&n);
      for(i=1;i<=n;i++)
      {
          scanf("%lf %lf",&x,&y);
           j=(d-x)/y;
           if(j>min)
           {
               min=j;
           }
           
      }
      printf("Case #%d: %.6lf\n",h,(d/min));
      
        h++;
    }
    return 0;
}

