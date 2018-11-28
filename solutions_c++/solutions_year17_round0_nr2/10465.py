
#include <iostream>
using namespace std;

int main() {
    
   
	int T,N[1000],i,f,s,a,b,j=1;
	
	cin>>T;
	for(i=0;i<T;i++)
	std::cin >>N[i] ;


for(i=0;i<T;i++)	
	{
	   b=N[i];
	   
	   
	   AAA: a=b;
	    f=a%10;
	    a=a/10;
	    while(a)
	    {
	        s=a%10;
	        if(s>f)
	      { --b;
	        goto AAA;
	          
	      }
	      
	        
	        f=s;
	        a=a/10;
	        
	    }
std::cout << "Case #"<<j<<": "<<b<<endl;
	    j++;
	}
	
}