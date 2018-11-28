#include <iostream>
using namespace std;

// Returns true if digits of n are sorted in decreasing
// order
bool areSorted(unsigned long long  int n)
{
	// Note that digits are traversed from last to first
  unsigned long long int next_digit = n%10;
	n = n/10;
	while (n)
	{
		unsigned long long int digit = n%10;
		if (digit > next_digit)
			return false;
		next_digit = digit;
		n = n/10;
	}

	return true;
}

int main(void)
{
	unsigned  long long int t,n ;
	cin>>t;
	for( unsigned long long int i =0;i<t;i++)
	{
	    cin>>n;
	    while (1)
	    {
	       if(areSorted(n)==true)
	       break;
	       else
	       n--;	        
	    }
	  cout<< "case #"<<i+1<<":"<<" "<<n<<endl;
	  
	} 
	return 0;
}