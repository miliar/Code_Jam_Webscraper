#include<stdio.h>
#include<iostream>
using namespace std;
int main()
{   
     long long n,b,r,k,s,a,p,ans1,ans2;
     int i,j,t;
     cin >> t;
     
     for(i=1; i<=t; i++)
     {    
         scanf("%lli",&n);
         scanf("%lli",&k);
         
         b=1;
         p=1;
         r=k;
         s=n;
         if(k==1)
           a= n;
         else{
           while(r>p)
           {
               r= r-p;
               p=p*2;
               b= b+p;
               
               s= s/2;
             
             
           }
           if(  p-r+1 >( p*s - (n-(b-p)) ) )
             a=s;
           else
             a=s-1;
          }
           
          if(a>1)
          {
          if( a%2==0)
           {  
                ans1= a/2;
                ans2= a/2-1;
            }
           else
            { ans1= a/2;
              ans2= a/2;
             }
           }
          else
             {  ans1=0;
                ans2=0;   }
         
          printf("Case #%d: %lli %lli\n",i,ans1,ans2);
         
       }
}





