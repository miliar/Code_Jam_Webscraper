#include<iostream>


using namespace std;

bool istidy(int x);
int main()
{
	int testcase;
	cin >> testcase;
	int number;
	for (int i = 1; i <= testcase; i++)
	{
		cin >> number;
		while(!istidy(number))
		{
			number--;
		}
		cout << "Case #" << i << ": " << number << endl;
	}
	return 0;
}

bool istidy(int x)
{
	int newnum = x;	// the new number formed after removing the last digit
	int prevlastnum = newnum % 10; // the last digit found after getting the modulus 
	int newlastnum;
	while (newnum != 0) {
		newlastnum = newnum % 10;
		if (newlastnum > prevlastnum)// if the new last number found is not either equal or smaller
		{
			return false; // stop the operation and return false 
		}
		else
		{
			newnum /= 10;
			prevlastnum = newlastnum;	// saving the tested current digit for next test 
		}
	}
	return true;
}