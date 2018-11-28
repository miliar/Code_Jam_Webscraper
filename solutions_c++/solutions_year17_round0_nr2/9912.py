#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <list>
#include <map>

using namespace std;



bool is_tidy (int n)
{
	vector <int> digits;
	int copy = n;
	while (copy != 0)
	{
		digits.push_back (copy % 10);
		copy /= 10;
	}
	
	sort(digits.begin(), digits.end());
	
	for (int j = digits.size()-1; j >= 0; j--)
	{
		if (digits [j] != n % 10) return false;
        n/=10;		
	}
	
	return true;
}


int main (int argc, char* argv[])
{
   unsigned int n; 
   cin >> n;
   for (unsigned int i=0;i<n;i++)  
   { 
      int number;
      cin >> number;
      
	  for (int j = number; j >= 1; j--)
	  {
		if (is_tidy (j))
		{
			cout << "Case #"<< i+1 <<":" << " " << j << endl;	
		    break;
		}
	  }
	  	
	}
}
