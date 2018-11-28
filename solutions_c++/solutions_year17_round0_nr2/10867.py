#include <iostream>
using namespace std;  
int main() 
{
  int t, n,a,b,c,d,e,f,k,flag=0;
  cin >> t; 
  for (int k = 1; k <= t; ++k)
   {
  	     cin>>n;
  	     
  		if(n>=1&&n<10)
  		{ 
  		cout << "Case #" << k << ": " <<n<< endl;
  	    }
  	   if(n>=10&&n<100)
  	    {
  
        for(int i=n;i>=1;i--)
        {
         f=i%10;
  	      e=i/10;
        	if(e<=f)
        	break;
	     }
	     cout << "Case #" << k << ": " <<e<<f<< endl;
        } 
   
      if(n>=100 && n<1000)
      {
       for(int i=n;i>=1;i--)
       {
       c=i%10;
  	   d=i/10;
       b=d%10;
       a=d/10;
      if(a<=b&&b<=c)
       {
	   cout << "Case #" << k << ": " <<a<<b<<c<< endl;   
	   break;
       }
    
      }
      }
   
    if(n==1000)
   {
    cout << "Case #" << k << ": " <<"999"<< endl;
   }
    
  }
  return 0;
}
