#include <iostream>
#include <sstream>
using namespace std;

int tidy(int x);
bool ascending(string s);

int main()
{
	int N, T, x, y; //N: the integer, T: the number of test case

	cin >> T; // read T
	for (x = 1; x <= T; x++)
	{
		cin >> N;
		y = tidy(N);
		cout << "Case #" << x << ": " << y << endl;
	}
	return 0;
}

int tidy(int x)
{
	for (int i = x; i >= 0; i--)
	{
		string number;
		ostringstream convert;
		convert << i;
		number = convert.str();
		if (ascending(number) == true)return i;
	}
}

bool ascending(string s)
{
	int len = s.length();
	bool status = true;
	if (len == 1)return true;
	for (int i = 0; i < len - 1; i++)
	{
		if (s[i] > s[i + 1])return false;
	}
	return status;
}
