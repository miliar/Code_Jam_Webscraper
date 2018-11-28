#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
	ifstream input("C:/Users/dal4s/Downloads/B-small-attempt1.in");
	ofstream output("C:/Users/dal4s/Downloads/B-small-attempt1.out");

	int T(0);
	input >> T;
	for (int CASE = 1; CASE <= T; ++CASE)
	{
		long long N(0), result(0);
		input >> N;
		output << "CASE #" << CASE << ": ";
		string S(to_string(N));
		int len(S.length());

		if (len == 1)
		{
			output << S << '\n';
		}
		else if (S[0] == '1' && (S.find('0') != string::npos))
		{
			string result(len - 1, '9');
			output << result << '\n';
		}
		else
		{
			bool OK(false);
			string result(S);
			for (int pos = 0; pos < len - 1; ++pos)
			{
				string copyS(S.begin() + pos, S.end()), targetS(len - pos, S[pos]);
				long long copy(stoll(copyS)), target(stoll(targetS));
				if (copy == target)
				{
					output << result << '\n';
					OK = true;
					break;
				}
				else if (copy < target)
				{
					if (copyS[0] > copyS[1])
					{
						while (pos != 0 && result[pos] <= result[pos - 1])
							--pos;
						--result[pos];
						for (int modpos = pos + 1; modpos < len; ++modpos)
							result[modpos] = '9';
						output << result << '\n';
						OK = true;
						break;
					}
				}
			}
			if (!OK)
				output << result << '\n';
		}
	}
	input.close();
	output.close();
	return 0;
}