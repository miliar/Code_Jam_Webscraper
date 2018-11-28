#include <iostream>
#include <stdio.h>
using namespace std;
int main() 
{
    long long j,p,r,b,n,ans;
    int k,t,i;
    cin >> t;
   
    for (i=1; i<=t; i++)
    {   
        scanf("%lli",&n);
        int a[30];
        ans =0;
        b = n; 
        p= 0;

        while(b!=0)
        {   b = b/10 ;
            p= p+1; 
         }
         b= n ;

        for(j=0;j<= p-1; j++)
          {    
               a[p-1-j] = b%10 ;
               b= b/10;
          }
          k=0; 
          r=0; 
        if (p==1)
         printf("Case #%d: %lli\n",i,n);  

        else {
         for(j=0;j<= p-2 ; j++)
           {    
               if( a[j+1]> a[j] )
                  k= j+1; 
                else if ( a[j+1]< a[j])
                  {    r=-1;
                       break; }
                else;
             
            }


        if (r==-1)
        {     a[k] =a[k] -1;
              for(j=k+1; j<=p-1;j++)
                 a[j]= 9; 
              
               for (j=0; j<= p-1; j++)
             {     
                  ans= ans*10+ a[j];
                  
               }  
            printf("Case #%d: %lli\n",i,ans);
         }
        else
         {   
             printf("Case #%d: %lli\n",i,n);
           
          }
        }
      }

}
          




        
        
        
