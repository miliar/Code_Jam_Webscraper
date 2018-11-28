#include <iostream>

using namespace std;

int main()
{
   int r,r2,T,c,n,x,i=1;
   cin>>T;
   while(T!=0)
   {
       cin>>n;
       l: x=n;
       while(x!=0)
       {
         r=x%10;
         x=x/10;
         r2=x%10;
         if(r<r2)
         {
             c=0;
             n=n-1;
             goto l;
         }
         else
          c=1;
        
            
       }
       if(c==1)
        cout<<"Case #"<<i<<":"<<" "<<n<<endl;
       
       T--;
       i++;
       
   }
   
   
   return 0;
}

