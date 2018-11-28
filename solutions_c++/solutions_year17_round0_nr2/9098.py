#include <iostream>
#include <string>
#include <cstring>
#include <cstdlib>

using namespace std;

long long int processData(string inputNum) 
{
	char *newNum = new char[inputNum.length() + 1];
	strcpy(newNum, inputNum.c_str());
	
	//Find first non sorted number
	char *walk = newNum;
	while(walk < newNum + inputNum.length() - 1 && *walk <= *(walk+1))
		walk++;

	if(walk < newNum + inputNum.length() - 1)
	{
		while(walk > newNum && *(walk) == *(walk-1))
			walk--;

		*walk = *walk - 1;
		walk++;
		while(walk < newNum + inputNum.length())
			*walk++ = '9';
	}

	return atoll(newNum);
}

int main()
{
	int numOfCase;

	cin >> numOfCase;
	for(int i=1; i<=numOfCase; i++)
	{
		string inputNum;
		cin >> inputNum;
		cout << "Case #" << i << ": " << processData(inputNum) << endl;
	}

	return 0;
}


