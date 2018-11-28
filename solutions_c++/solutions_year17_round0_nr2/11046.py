#include <iostream>
#include <cstdint>
#define ULL unsigned long long int

using namespace std;

int convert(int *ar,ULL ba)
{  int i=0;
  while(ba>0) {
    ar[i++] = ba% 10;
    ba /= 10;
     }
    return --i;  
}
 int check(int *ar,int ch)
{
    for(int j=0;j<ch;j++)
    {
        if(ar[j+1]<=ar[j])
        continue;
        else
        return 0;
        
    }
    return 1;
}



int main() {
    ULL a=0,b=0;
    
    
   int T;
   cin>>T;
   for(int i=1;i<=T;i++)
   {  int ar[25]={0},c;
       cin>>a;
       b=a;
     while(1)
     {
    c= convert(ar,b);
     
     if(check(ar,c))
     {
        cout<<"Case #"<<i<<": "<<b<<endl;
         break;  
     }
     else
      { b--;
       continue;
      }
   }
     
       
       
      

       
       
       
  }  
	
	return 0;
}
