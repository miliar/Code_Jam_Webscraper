#include <iostream>
using namespace std;  

int main() 
{
  long long int t;
  long long int n, temp;
  cin >> t; 
  
  for (long long int j = 1; j <= t; ++j) 
  {
  	cin >> n;
  	int flag = 0;
  	while(n > 0)
  	{
	  temp = n;
	  flag = 0;
	  while(temp >= 10)
	  {
	  	if(temp%10 < ((temp = temp / 10) % 10))
	  	{
	  		flag = 1;
			break;	  		
		}
	  }
	  if(flag == 0)
	  {
	  	cout << "Case #" << j << ": " << n << endl;
	  	break;
	  }
	  else
	  {
	  	n--;
	  }  		  		
	} 
  }
  return 0;
}
 

