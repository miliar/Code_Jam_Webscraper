#include<iostream>
#include<fstream>
#include<vector>
#include<string>
#include<iterator>
#include<sstream>

using namespace std;

bool CheckFlipsComplete(string& s)
{
	bool complete = true;

	for (int i = 0; i < s.length(); i++)
	{
		if (s.at(i) == '-')
		{
			complete = false;
			break;
		}
	}

	return complete;
}

void FlipPancakes(string& s, int k)
{
	int flips = 0;
	int countIndex = -1;
	vector<int> counts(k);

	for (int i = 0; i < s.length(); ++i)
	{
		if (s.at(i) == '-')
		{
			s.at(i) = '+';
		}
		else if (s.at(i) == '+')
		{

		}
	}
}

int FlipPancakes_Naive(string& s, int k)
{
	int flips = 0;
	bool end = false;
	int count = -1;

	while (!end)
	{
		for (size_t i = 0; i < s.length(); i++)
		{
			if (count >= (k - 1))
			{
				count = -1;
				flips++;
				break;
			}

			if (s.at(i) == '-')
			{
				// first check to flip pancakes, maybe doesn't have free space to do it
				if (count == -1)
				{
					if (i + (k - 1) >= s.length())
					{
						end = true;
						break;
					}
					
				}

				s.at(i) = '+';
				count++;
			}
			else if (s.at(i) == '+')
			{
				if (count != -1)
				{
					s.at(i) = '-';
					count++;
				}
			}

			if (i == (s.length() - 1))
			{
				if (count >= (k - 1))
					flips++;

				end = true;
			}
		}
	}

	return flips;
}

template<typename Out>
void split(const string &s, char delim, Out result) {
	stringstream ss;
	ss.str(s);
	string item;
	while (getline(ss, item, delim)) {
		*(result++) = item;
	}
}

vector<string> split(const string &s, char delim) {
	std::vector<std::string> elems;
	split(s, delim, back_inserter(elems));
	return elems;
}

int main()
{
	int T;
	cin >> T;

	vector<string> S(T);
	vector<int> K(T);

	for (size_t i = 0; i < T; i++)
	{
		cin >> S[i] >> K[i];
	}

	for (size_t i = 0; i < T; i++)
	{
		int flips = FlipPancakes_Naive(S[i], K[i]);
		bool flipsComplete = CheckFlipsComplete(S[i]);

		if (flipsComplete)
			cout << "Case #" << (i + 1) << ": " << flips << '\n';
		else
			cout << "Case #" << (i + 1) << ": IMPOSSIBLE" << '\n';
	}
	

	/*string line;
	fstream myFile("A-large.in");

	if (myFile.is_open())
	{
		int count = 0;
		while (getline(myFile, line))
		{
			count++;
			if (count > 1)
			{
				vector<string> values = split(line, ' ');
				int flips = FlipPancakes_Naive(values[0], stoi(values[1]));
				bool flipsComplete = CheckFlipsComplete(values[0]);

				if (flipsComplete)
					cout << "Case #" << count - 1 << ": " << flips << '\n';
				else
					cout << "Case #" << count - 1 << ": IMPOSSIBLE" << '\n';
			}
		}

		myFile.close();
	}
	else
		cout << "Unable to open file.\n";*/
		
	return 0;
}