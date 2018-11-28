#include <string>
#include <iostream>
#include <cstdlib>
#include <vector>
#include <fstream>
using namespace std;

int main() {
	ifstream cin;
	ofstream outStream;

	cin.open("A-large.in");
	outStream.open("output.txt");

	int numcases;
	cin >> numcases;

	int count = 1;
	for (int i = 0; i < numcases; i++)
	{
		string ans = "IMPOSSIBLE";
		int flips = 0;
		string s;
		cin >> s;
		int k;
		cin >> k;
		for (int j = 0; j < (int)s.length()-k+1; j++)
		{
			if (s[j] == '-')
			{
				for (int n = j; n < j+k; n++)
				{
					if (s[n] == '-')
					{
						s[n] = '+';
					}
					else
						s[n] = '-';
				}
				flips++;
			}
		}
		bool b = true;
		for (int j = 0; j < s.size(); j++)
		{
			if (s[j] == '-')
			{
				b = false;
				break;
			}
		}
		if (b)
		{
			cout << "Case #" << count << ": " << flips << endl;
			outStream << "Case #" << count << ": " << flips << endl;
		}
		else
		{
			outStream << "Case #" << count << ": " << "IMPOSSIBLE" << endl;
			cout << "Case #" << count << ": " << "IMPOSSIBLE" << endl;
		}
		count++;
	}


	cin.close();
	outStream.close();

	return(0);
}