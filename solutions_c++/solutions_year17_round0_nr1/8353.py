#include <fstream>
#include <string>

using namespace std;

int main()
{
	ifstream input("data.txt");
	ofstream output("output.txt");

	unsigned cases, k;
	string s;

	input >> cases;

	for (int t = 1; t <= cases; t++)
	{
		input >> s;
		input >> k;

		unsigned n = 0;
		for (int i = 0; i <= s.length() - k; i++)
			if (s[i] == '-') {
				n++;
				for (int j = i; j < i + k; j++)
					s[j] = (s[j] == '-') ? '+' : '-';
			}

		bool flag = true;
		for (int i = s.length() - k + 1; i < s.length(); i++)
			if (s[i] != '+')
				flag = false;

		if(flag)
			output << "Case #" << t << ": " << n  << endl;
		else
			output << "Case #" << t << ": IMPOSSIBLE" << endl;
	}

	input.close();
	output.close();

	return 0;
}