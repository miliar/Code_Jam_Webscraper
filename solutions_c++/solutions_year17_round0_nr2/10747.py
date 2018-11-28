#include <iostream>  
using namespace std;  
int main() {
 long long int t, n,a,j;
  cin >> t; 
  
  
  
  for(j=0;j<t;j++)
  {
  	cin>>n;
  	a=n;
  	long long int m[20],result;
  	int i=0;int ok=0;
  	while(n)
  	{	  
  		m[i]=n%10;
  		
  		if(i==0)
  		{ok=1;
		  result=n;}
  		else
  		{
  			if(m[i-1]>=m[i])
  			{
  				ok=1;
  				
			  }
			  else
			  {
			  	ok=0;
			  	n=a-1;
			  	a=n;
			  	i=-1;
			  	result=n;
			  }
		  }
		  ++i;
		  if(i>0){
		  
		  n=n/10;
	}
  		
	} 	
  	
   
    
    cout << "Case #" << j+1 << ": "  << " " << result << endl;
  }
  return 0;
}
 
