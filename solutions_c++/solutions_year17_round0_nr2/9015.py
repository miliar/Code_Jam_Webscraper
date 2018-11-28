#include <iostream>  
#include <string>
#include <sstream> 

// cause I'm lazy
using namespace std;

unsigned long long lastTidyNumber(string number)
{
	int index = -1;
	string newNumber = number;
	for (int i = 0; i < number.length() - 1; ++i)
	{
		if (number[i] < number [i+1])
		{
			continue;
		}
		else if (number[i] == number[i+1])
		{
			if (index == -1)
			{
				index = i;
			}
		}
		else if (number[i] > number[i+1])
		{
			newNumber = "";
			if (index == -1)
			{
				for (int j = 0; j < i; ++j)
				{
					newNumber += number[j];
				}
				newNumber += number[i] -1;
				for (int j = i+1; j < number.length(); ++j)
				{
					newNumber += "9";
				}
			}
			else
			{
				for (int j = 0; j < index; ++j)
				{
					newNumber += number[j];
				}
				newNumber += number[index] -1;
				for (int j = index+1; j < number.length(); ++j)
				{
					newNumber += "9";
				}
			}
			break;
		} 
	}
	istringstream istr(newNumber);
	unsigned long long toReturn;
	istr >> toReturn;
	return toReturn;
}

int main() 
{
  int tests;
	string number;
  cin >> tests; 
  for (int i = 1; i <= tests; ++i) 
	{
    cin >> number;
		unsigned long long tidyNumber = lastTidyNumber(number);	
    cout << "Case #" << i << ": " << (tidyNumber) << endl;
  }
  return 0;
}
