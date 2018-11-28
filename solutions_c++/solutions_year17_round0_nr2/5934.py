#include <iostream>  
#include <math.h> 
#include <string>
#include <iostream>
#include <algorithm>
#include <vector>
#include <fstream>
using namespace std;  
int main() {
  int t;
 // int n;
  cin >> t;  
  
  for (int i = 1; i <= t; ++i) {
  		
  	char num[20];
    int n;
    cin >> num ;  
    n=strlen(num);
    
    if(n!=1){
    	
    	
    int index=0;	
    	
    	
   	int k=0;
   	 for(int j=0;j<n-1;j++)
	{
 	 	if(num[j]>num[j+1])
		  	{
	 	 	num[j]--;
	 	 	k=j;
	 	 	index=1;
	         break;
	 	    }
	}
	  if(index==1)
	  	{
  		for(int j=k+1;j<n;j++)
		num[j]='9';	
		
	   while(k>0)
	   {
   		if(num[k-1]>num[k])
   		{
		   num[k-1]--;
		   	num[k]='9';
		   }
   k--;
   	}	
		
		
		
  	}
	  















 	 	
  }
 	 
 string s=num;
 if(num[0]=='0')
 s.erase(0,1); 
 
 
 cout << "Case #" << i << ": " << s << endl;
 
 	 
} 
   
    
   

  
    

   
  

return 0;


}