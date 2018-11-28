#include <fstream>
#include <iostream>
#include <algorithm>
#include <vector>
#include <set>
#include <string>

using namespace std;

void flip(string& str, int begin, int end)
{
	for (auto i = begin; i < end; i++)
		str[i] = (str[i] == '+' ? '-' : '+');
}

int main()
{
	ifstream in("input.txt");
	ofstream out("output.txt");

	int t;
	in >> t;

	for (auto tcase = 1; tcase <= t; tcase++)
	{

		int k;
		string str;
		in >> str >> k;

		str += "+";

		auto incorrectBegin = -1;
		auto flips = 0;

		for (auto i = 0; i < str.size(); i++)
		{
			if (str[i] == '-' && incorrectBegin == -1)
			{
				incorrectBegin = i;
			}
			else if (incorrectBegin != -1 && incorrectBegin + k - 1 == i)
			{
				++flips;
				flip(str, incorrectBegin, i + 1);
				i = incorrectBegin;
				incorrectBegin = -1;
			}
		}

		auto hasSolution = true;
		for (auto i = str.size() - k; i < str.size(); i++)
		{
			if (str[i] == '-')
			{
				hasSolution = false;
				break;
			}
		}

		out << "Case #" << tcase << ": " << (hasSolution ? std::to_string(flips) : "IMPOSSIBLE") << endl;
	}
}