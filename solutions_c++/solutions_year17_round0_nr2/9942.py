#include <string>
#include <iostream>
#include <boost/lexical_cast.hpp>

using namespace std;

uint64_t lastTidy(uint64_t num);

int main(){
	int cases;
	cin >> cases;
	for(int i=1; i<=cases; i++)
	{
	  uint64_t num = 0;
	  cin >> num;
	  uint64_t solution = lastTidy(num);
	  cout << "Case #" << i << ": " << solution << endl;   
	}
		
	return 0;
}

uint64_t lastTidy(uint64_t num)
{
  string number = to_string(num);
  for(int i=0; i< number.size()-1; i++)
  {
	  int leftDigit = (int)number[i] - '0';
	  int rightDigit = (int)number[i+1] - '0';
	  if(leftDigit > rightDigit)
	  {
				if(i > 0 && number[i] == number[i-1])
				{
					number[i-1] = '0' + (leftDigit - 1);
					for(int j = i; j< number.size(); j++)
						number[j] = '9';
				}
				else
				{
				  number[i] = '0' + (leftDigit - 1);
				  for(int j = i+1; j< number.size(); j++)
					number[j] = '9';
				}
	  }
  }
  return boost::lexical_cast<uint64_t>(number);
}