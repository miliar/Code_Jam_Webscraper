#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;


const bool OUTPUT_TO_FILE = true;


int main()
{
	cout.sync_with_stdio(false);
	stringstream output;

	int t;
	string n;
	int lastnine;

	cin >> t;
	for (int run = 1; run <= t; run++)
	{
		output << "Case #" << run << ": ";

		cin >> n;
		lastnine = n.size();

		for (int i = n.size() - 1; i > 0; i--)
		{
			if (n[i] < n[i - 1])
			{
				n[i - 1]--;
				for (int j = i; j < lastnine; j++)
				{
					n[j] = '9';
				}

				lastnine = i;
			}
		}

		if (n[0] != '0')
		{
			output << n[0];
		}
		for (int i = 1; i < n.size(); i++)
		{
			output << n[i];
		}

		output << "\n";
//		cout << run << "\n";
	}

	if (OUTPUT_TO_FILE)
	{
		ofstream output_file;
		output_file.open("out.txt");
		output_file << output.rdbuf();
		output_file.close();
	}
	else
	{
		cout << output.rdbuf();
	}
}
