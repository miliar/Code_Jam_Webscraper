#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main(int argc, char** argv)
{
	string inFile(argv[1]);
	string outFile(inFile + ".out");
	ifstream in(inFile);
	ofstream out(outFile);

	int ts; in >> ts;
	for (int t = 1; t <= ts; ++t)
	{
		string num; in >> num;
		bool ok = true;
		while (ok)
		{
			ok = false;
			int i = 0;
			while (i < num.size() && num[i] == '0') i++;
			while (i + 1 < num.size() && num[i] <= num[i + 1]) i++;
			if (i + 1 < num.size() && num[i] > num[i + 1])
			{
				ok = true;
				num[i]--;
				i++;
				while (i < num.size())
				{
					num[i] = '9';
					i++;
				}
			}
		}
		out << "Case #" << t << ": ";
		int start = 0;
		while (start < num.size() && num[start] == '0') start++;
		if (start == num.size()) out << '0' << endl;
		else
		{
			while (start < num.size())
			{
				out << num[start];
				start++;
			}
			out << endl;
		}
	}
	return 0;
}
