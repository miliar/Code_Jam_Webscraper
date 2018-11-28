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
		string s; in >> s;
		int k; in >> k;
		int cnt = 0;
		for (int i = 0; i < s.size(); i++)
		{
			if (s[i] == '-' && (i + k) <= s.size())
			{
				cnt++;
				for (int j = i; j < i + k; j++)
				{
					if (s[j] == '-') s[j] = '+';
					else s[j] = '-';
				}
			}
		}
		bool ok = true;
		for (int i = 0; ok && i < s.size(); i++) ok &= s[i] == '+';
		out << "Case #" << t << ": ";
		if (ok) out << cnt << endl;
		else out << "IMPOSSIBLE" << endl;
	}
	return 0;
}
