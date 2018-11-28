#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string>
#include <fstream>
using namespace std;

bool isTidy(int n)
{
  int k = n, last = 9;
  if( k == 0)
  	return true;
  while( k != 0)
  {
  	int temp = k % 10;
  	k = k / 10;
  	if( temp > last)
  		return false;
  	else 
  	{
  		last = temp;
  	}
  	
  }
  return true;
}


int main() 
{
  int t,i = 0, n, m;
  string alpha;
  cin >> t;
  while(t != 0)
  {
  	i++;
  	t--;
  	cin >> n;
   	cout << "case #" << i << ": ";
  	while(n >= 0)
  	{
  		if(isTidy(n))
  		{
  			cout << n << endl;
  			break;
  		}
  		n--;
  	}
  }
  return 1;
}