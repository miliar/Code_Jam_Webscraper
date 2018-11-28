#include<iostream>
#include<stdio.h>
using namespace std;

int main()
{
   int t,k,n,n1,p,q,flag,i,j,arr[10000];  
   
   cin>>t;
   
   for(i=1;i<=t;i++)
   {
       cin>>n;
       
       if(n>=0 && n<=9)
          arr[i]=n;
         //cout<<"Case #"<<i<<": "<<n<<endl;
       
       else
       {
         while(n>0)
         {
            n1=n;
            flag=0;
       //   cout<<"This is n "<<n<<endl;
            while(n1>9)
            {  
                p = n1%10;
                q = n1%100; q=q/10;
                if(q>p)
                {
                   flag=1;
                   break;
                }
                else
                  n1 = n1/10;
            }
           
            if(flag==0)
            {
               arr[i]=n;
           //     cout<<"Case #"<<i<<": "<<n<<endl;
                break;
            }  
            else
              n--;
          }
                 
        }
    }
    
    for(i=1;i<=t;i++)
       cout<<"Case #"<<i<<": "<<arr[i]<<endl;
      

   return 0;
   
}
