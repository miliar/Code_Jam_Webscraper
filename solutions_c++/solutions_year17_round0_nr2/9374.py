#include<iostream>
#include<math.h>
using namespace std;
int main()
{
   int t,j;
    unsigned long long int n,m,i,k,l,x,y;
	cin>>t;
	j=0;
	while(t--)
	{ i=1;
	  x=0;
	 
	  cin>>n;
	  m=n;
	 
	    
	  while(m!=0)
	  {
	
	      k=m%10;
	      m=m/10;
	      l=m%10;
          if(k<l)
	      {
	        x=i;
	      }
	      if(x>0)
	      {
	          if(k==l)
	            x=i;
	      }
	      i++;
	  }
	  if(i>=9)
	  {
	      
	  }
	  if(x>0)
	  {
	  
	  y=pow(10,x);
	  n=(n-y)-(n%y)+(y-1);
	  }
	  
	  
	  j++;
	     cout<<"Case #"<<j<<": "<<n<<"\n";
	    
	  
	}
	
	return 0;
}


