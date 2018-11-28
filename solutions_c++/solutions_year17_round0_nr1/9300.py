#include <iostream>
#include <queue>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main(int argc, char const *argv[])
{
	int T;
	cin >> T;
	for (int i = 0; i < T; ++i)
	{
		/* code */
		int impossible = 0;
		int flips = 0;
		string input;
		int K;
		cin >> input;
		cin >> K;
		int n = input.size();
		for (int j = 0; j < n; ++j)
		{
			if (input[j] == '-')
			{
				flips++;
				if (j + K > n)
				{
					impossible = 1;
					break;
				} else {
					// possible flip next k
					input[j] = '+';
					for (int k = 1; k < K; ++k)
					{
						// j++;
						if(input[j + k] == '-')
							input[j + k] = '+';
						else
							input[j + k] = '-';
					}
				}
			}
		}
		if(impossible == 1) {
			cout << "Case #" << i + 1<< ": IMPOSSIBLE" << endl;
		} else {
			cout << "Case #" << i + 1 << ": " << flips << endl;
		}
	}
	return 0;
}