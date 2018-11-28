#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("B-large.in","r",stdin);
    
	freopen("output.txt","w",stdout);
    int t,j=1;
    scanf("%d",&t);
    
    while(t--)
    {
        long long int ans=0,flag=0,i=1,y,k,x,n;
     scanf("%lld",&n);
   
    while(flag!=1)
      {
          k=n;
          ans=45;
        while(k!=0)
          {
         y=k%10;
       k=k/10;
      if(y>ans)
      {
          flag=0;
          break;
      }
      else
      flag=1;
      
       ans=y; 
        
    }
        
        if(flag==1)
        break;
        
        x=pow(10,i);
        n=n-((n%x)+1);
     
        i++;
        
     }
     printf("Case #%d: %lld\n",j,n);
     j++;
    }
    return 0;
}
