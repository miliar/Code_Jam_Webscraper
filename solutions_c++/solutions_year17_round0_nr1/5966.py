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
 
 char s[1000];
 int k;
 int time=0;
 cin>>s>>k;
 
int n=strlen(s);
 
 for(int j=0;j<=n-k;j++)
 if(s[j]=='-')
  {
  	time++;
  	for(int y=j;y<j+k;y++)
  	{
		if(s[y]=='-')
  	s[y]='+';
  	else
  	s[y]='-';  	
  }
  
  	
  }		
  int index=1;
  for(int j=n-k;j<n;j++){
  if(s[j]=='-') 
  {
  	index=0;
  	break;
  }  	
  }

  if(index==1)
 cout << "Case #" << i << ": " << time << endl;  
 else
  cout << "Case #" << i << ": " << "IMPOSSIBLE" << endl;   
  
  
  
  }
  
    

   
  

return 0;


}