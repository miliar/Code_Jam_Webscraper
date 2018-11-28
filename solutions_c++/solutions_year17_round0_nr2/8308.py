#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <iostream>
#include <sstream>
#include <fstream>
using namespace std;  // since cin and cout are both in namespace std, this saves some text

std::ifstream infile("B-small-attempt0.in");
std::ofstream outfile("B-small-attempt0.out");


int main() {
  int t, prev_dig; 
  long long m, temp;

  infile>>t;// read t. cin knows that t is an int, so it reads it as such.

  for (int i = 1; i <= t; ++i) {

  	infile>>m;// read n.
  	
  	while(true)
  	{
  		temp = m;
  		prev_dig = temp%10;
  		temp /= 10;


  		while(temp>0)
  		{
  			if((temp%10)>prev_dig)
  				break;
  			else
  			{
  				prev_dig = temp%10;
  				temp /= 10;
  			}
  		}

  		if(temp==0)
  			break;
  		else
  			m--;
  	}

  	outfile<<"Case #" << i << ": " << m << endl;
   
  }

  return 0;
}