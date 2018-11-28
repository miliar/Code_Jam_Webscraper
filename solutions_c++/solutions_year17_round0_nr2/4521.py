#include <iostream>  // includes cin to read from stdin and cout to write to stdout
#include <string>
using namespace std;  // since cin and cout are both in namespace std, this saves some text
__int64 solve(__int64 number);
void main() {
	int t;
	__int64 number;
	cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
	for (int i = 1; i <= t; ++i) {
		cin >> number;
		cout << "Case #" << i << ": " << solve(number) << endl;
		// cout knows that n + m and n * m are ints, and prints them accordingly.
		// It also knows "Case #", ": ", and " " are strings and that endl ends the line.
	}
}

__int64 solve(__int64 number) {

	std::string snumber = std::to_string(number);
	if (snumber.length() == 1)
	{
		return number;
	}
	__int64 n = (__int64)snumber.at(0) -48;
	
	for (__int64 i = 1; i < snumber.length(); i++)
	{
		__int64 test = (__int64)snumber.at(i) -48;
		if(n <= test)
		{
			n = test;
		}
		else 
		{
			number--;
			//cout << "test" << number << endl;
			return solve(number);

		}

	}

	return number;
}

/*
__int64 solve(__int64 number) {

std::string snumber = std::to_string(number);
if (snumber.length() == 1)
{
return number;
}
__int64 n = (__int64)snumber.at(0) -48;

for (__int64 i = 1; i < snumber.length(); i++)
{
__int64 test = (__int64)snumber.at(i) -48;
if(n <= test)
{
n = test;
}
else
{
number--;
return solve(number);

}

}

return number;
}*/