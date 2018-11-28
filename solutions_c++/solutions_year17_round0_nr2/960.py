
#include <iostream>
#include <string>
#include <cmath>
using namespace std;

int main() {

	int T;
	cin >> T;
	for (int i = 0; i < T; i++)
	{
		long long input;
		cin >> input;
		string sinput = to_string(input);
		int first = 0;
		bool valid = true;
		for (int j = 1; j < sinput.length(); j++)
		{
			if (sinput[j] > sinput[j - 1]) first = j;
			if (sinput[j] < sinput[j - 1])
			{
				valid = false;
				break;
			}
		}
		if (input == 1||valid)
		{

		}
		else if (first == 0 && sinput[0] == '1')
		{
			string temp = "";
			for (int k = 1; k < sinput.length(); k++)
			{
				temp += '9';
			}
			input = atoll(temp.c_str());
		}
		else if (first != sinput.length() - 1)
		{
			string temp = "";
			for (int k = 0; k < sinput.length(); k++)
			{
				if (k < first)
				{
					temp += sinput[k];
				}
				else if (k == first)
				{
					temp += sinput[k] - 1;
				}
				else
				{
					temp += '9';
				}
			}
			input = atoll(temp.c_str());
		}
		cout << "Case #" << i + 1 << ": " << input << endl;
	}
	return 0;
}