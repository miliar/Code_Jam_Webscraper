#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

int tidyCheck(int x);
bool ascCheck(int x);

int main()
{
	int T;
	cin >> T;

	ofstream myFile;
	myFile.open("output.txt");

	for (int i = 0; i < T; i++)
	{
		int input, tidy;
		cin >> input;
		tidy = tidyCheck(input);

		myFile << "Case #" << i + 1 << ": " << tidy << endl;
	}
	system("PAUSE");
	return 0;
}

int tidyCheck(int x)
{
	if (x < 10)
		return x;
	else if ((x % 10 == 0) || (ascCheck(x) == false))
		tidyCheck(x - 1);
	else
		return x;
}
bool ascCheck(int x)
{
	int length = 0;
	int temp = x;

	while (temp != 0)
	{
		length++;
		temp /= 10;
	}
	temp = x;

	vector<int> v(length);
	for (int i = length - 1; i >= 0; i--)
	{
		v[i] = temp % 10;
		temp /= 10;
	}

	for (int i = 0; i < length - 1; i++)
	{
		if (v[i] > v[i + 1])
			return false;
	}
	return true;
}