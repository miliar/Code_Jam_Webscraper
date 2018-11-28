#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
using namespace std;

bool isTiny(string number)
{
	string temp;
	temp = number;

	sort(temp.begin(), temp.end());
	return temp == number;
}

string process(string number)
{
	if (isTiny(number))
	{
		return number;
	}

	unsigned int len = number.length();
	string temp;

	for (register unsigned int i = 2; i <= len; ++i)
	{
		temp = number.substr(0, i);

		if (!isTiny(temp))
		{
			temp.replace(i-1, -1, len - i + 1, '0');
			return to_string(stoull(temp, nullptr) -1);
		}
	}

	return number;
}

int main() {

	unsigned __int64 cases;
	//string str, str2;
	string line;

	ofstream OUT("output.txt", ios::out);
	ifstream IN("input.txt", ios::in);

	IN >> cases;

	//cout << "There are " << cases;

	for (register unsigned __int64 T = 1; T <= cases; ++T)
	{
		IN >> line;

		while (!isTiny(line))
		{
			line = process(line);
		}

		OUT << "Case #" << T << ": " << line << endl;


		/*for (register unsigned __int64 i = n; i >= 0; --i)
		{
			//cout << "Processing " << i << endl;
			str = std::to_string(i);
			/str2 = str;

			//sort(str.begin(), str.end());

			//if (str == str2)
			if (isTiny(str))
			{
				OUT << "Case #" << T << ": " << str2 << endl;
				cout << "Case #" << T << ": " << str2 << endl;
				break;
			}
		}*/
	}
	
	return 0;
}