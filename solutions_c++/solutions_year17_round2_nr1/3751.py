#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int z=1;
    int t;
    scanf("%d",&t);
    while(t--)
     {
      double n,i,d,x,y,j,max=0.0;
        cin>>d>>n;
      for(i=1;i<=n;i++)
      {
          cin>>x>>y;
           j=(d-x)/y;

           if(j>max)
               max=j;
           
           
      }
      cout<<"Case #"<<z<<": ";
      printf("%.6lf\n",(d/max));
      
       z++; 
    }
    return 0;
}

