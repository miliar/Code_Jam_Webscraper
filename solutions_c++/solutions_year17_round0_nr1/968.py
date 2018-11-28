
#include <iostream>
#include <string>
using namespace std;

int main() {

	int T;
	cin >> T;
	for (int i = 0; i < T; i++)
	{
		string input;
		cin >> input;
		int k;
		cin >> k;
		int flips = 0;
		bool success = true;
		for (int j = 0; j < input.length(); j++)
		{
			if (input[j] == '-')
			{
				if (j + k <= input.length())
				{
					flips++;
					for (int p = j; p < j + k; p++)
					{
						if (input[p] == '-')input[p] = '+';
						else input[p] = '-';
					}
				}
				else
				{
					success = false;
					break;
				}
			}
		}
		if (success) cout << "Case #" << i + 1 << ": " << flips << endl;
		else cout << "Case #" << i + 1 << ": " << "IMPOSSIBLE" << endl;
	}
	return 0;
}