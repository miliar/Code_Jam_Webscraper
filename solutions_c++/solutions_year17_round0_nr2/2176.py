#include <fstream>
#include <string>
#include <vector>
using namespace std;

bool isTidy(const string& number)
{
	for (int i = 0; i < number.size() - 1; ++i)
	{
		if (number[i] > number[i + 1])
		{
			return false;
		}
	}

	return true;
}

void makeTidy(string& number)
{
	for (int i = number.size() - 1; i > 0; i--)
	{
		if (number[i - 1] > number[i])
		{
			number[i - 1]--;
			for (int j = i; j < number.size(); ++j)
			{
				number[j] = '9';
			}
		}
	}
}

int main()
{
	ifstream in("input.txt");
	ofstream out("output.txt");

	int T;
	in >> T;

	for (int t = 0; t < T; ++t)
	{
		string N;
		in >> N;

		out << "Case #" << t + 1 << ": ";

		makeTidy(N);

		bool startOutput = false;
		for (int i = 0; i < N.size(); ++i)
		{
			if (N[i] != '0')
			{
				startOutput = true;
			}
			if (startOutput)
			{
				out << N[i];
			}
		}
		out << endl;
	}

	return 0;
}