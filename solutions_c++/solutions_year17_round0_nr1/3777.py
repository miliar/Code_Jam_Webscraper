#include<iostream>
#include<fstream>
#include<string>
#include<vector>
#include<algorithm>
#include<string>
using namespace std;
int main()
{
	int t;

	cin >> t;
	ofstream outfile;
	outfile.open("AAA.txt");
	for (int i = 0; i < t; i++)
	{
		outfile << "Case #" << i + 1 << ": ";
		string word;
		int value;
		int cntr = 0;
		cin >> word >> value;
		bool answer = true;
		for (int l = 0; l < word.size(); l++)
		{
			if (word[l] == '-') {
				if (((word.size()-value)) >= l) {
					for (int j = l; j < l + value; j++)
					{
						if (word[j] == '-') { word[j] = '+'; }
						else if (word[j] == '+') { word[j] = '-'; }
					}
					cntr++;
				}
				else { answer = false; }
				
				}
			
		}
		if (answer == false) { outfile << "IMPOSSIBLE" << endl; }
		else {
			outfile << cntr << endl;
		}
	}

	outfile.close();
	
	return 0;
}
