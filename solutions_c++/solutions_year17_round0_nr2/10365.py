#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <string>
using namespace std;

bool checkTidy(int NUM);

int main()
{
	freopen("B-small-attempt1.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int T; //testcase
	cin >> T;
	for (int t = 0; t < T; t++)
	{
		int input;
		cin >> input;
		//cout << checkTidy(input) << endl;
		while (!checkTidy(input))
		{
			input--;
		}
		cout << "Case #" << t + 1 << ": " << input << endl;
		
	}
	return 0;
}

bool checkTidy(int NUM)
{
	string num = to_string(NUM);
	int len = num.length();
	char temp = num.at(0);
	//cout << "string num: " << num << endl;
	//cout << "temp: " << temp << endl;
	for (int i = 1; i < len; i++)
	{
		if (num.at(i) >= temp) temp = num.at(i);
		else
			return false;
	}
	return true;
}