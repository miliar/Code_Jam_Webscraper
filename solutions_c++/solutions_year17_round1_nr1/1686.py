#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

typedef long long ll;


ll f1(ll n, ll k)
{
	int exponent = log2(k) + 1;
	ll numRepeats = 1;
	for (int i = 0; i < exponent; ++i)
		numRepeats *= 2;

	return (n - (k - numRepeats / 2)) / numRepeats;
}

ll f2(ll n, ll k)
{
	int exponent = log2(k) + 1;
	ll numRepeats = 1;
	for (int i = 0; i < exponent; ++i)
		numRepeats *= 2;

	return (n - k) / numRepeats;
}

int main()
{
	ofstream output;
	ifstream input;
	input.open("input.txt");
	output.open("output.txt");

	//	FILE * input;
	//	input = fopen("input.txt","r");

	int T;

	//	fread(&n, sizeof(int), 1, input);cout<<n<<endl; char cc=getchar();

	input >> T;// cout<<n<<endl;
	//cin >> T;

	//string s;
	int r, c;

	//string s[] = { "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""};
	string s[25];

	for (int t = 0; t < T; ++t)
	{
		input >> r >> c;

		for (int i = 0; i < r; ++i)
		{
			input >> s[i];
		}

		int lastNonEmpty = -1;
		for (int i = 0; i < r; ++i)
		{
			bool isEmpty = 1;
			for (int j = 0; j < c; ++j)
			{
				if (s[i][j] != '?')
				{
					isEmpty = 0;
					break;
				}
			}
			if (!isEmpty)
			{
				int lc = -1;
				for (int j = 0; j < c; ++j)
				{
					if (s[i][j] != '?')
					{
						lc = j;
						for (int x = lastNonEmpty + 1; x <= i; ++x)
						{
							for (int y = 0; y <= j; ++y)
							{
								if (s[x][y] == '?')
								{
									s[x][y] = s[i][j];
								}
							}
						}
					}
				}

				for (int j = lc + 1; j < c; ++j)
				{
					for (int x = lastNonEmpty + 1; x <= i; ++x)
					{
						if (s[x][j] == '?')
						{
							s[x][j] = s[i][lc];
						}
					}
				}

				lastNonEmpty = i;
			}
		}

		for (int x = lastNonEmpty + 1; x < r; ++x)
		{
			for (int y = 0; y < c; ++y)
			{
				s[x][y] = s[lastNonEmpty][y];
			}
		}
	


			output << "Case #" << t + 1 << ":"<< endl;
			for (int i = 0; i < r; ++i)
			{
				output << s[i] << endl;
			}
		

	}
	//	fclose(input);
	input.close();
	output.close();
	//	system("pause");
	return 0;
}
