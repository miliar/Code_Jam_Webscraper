#include <fstream>
#include <iostream>
#include <string>

using namespace std;

int main()
{
	ifstream input("data.txt");
	ofstream output("output.txt");

	unsigned cases;
	unsigned long long n;

	input >> cases;

	for (int t = 1; t <= cases; t++)
	{
		input >> n;

		string s = to_string(n);
		int k = -1;

		for (int i = 0; i < s.length() - 1; i++) 
			if (s[i] > s[i + 1]) {
				if (k != -1)
					i = k;

				s[i] = s[i] - 1;
				for (int j = i + 1; j < s.length(); j++)
					s[j] = '9';
				break;
			}
			else {
				if (s[i] == s[i + 1])
					k = i;
				else
					k = -1;
			}

		for(int i = 0; i < s.length(); i++)
			if (s[i] == '0') {
				s = string(s.length() - 1, '9');
				break;
			}

		output << "Case #" << t << ": " << stoull(s) << endl;
	}

	input.close();
	output.close();

	return 0;
}