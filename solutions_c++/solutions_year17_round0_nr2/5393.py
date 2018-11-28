#include <iostream>
#include <string>

using namespace std;

int main() {
	int T;
	cin >> T;

	string N;
	for (int i = 0; i < T; i++)
	{
		cin >> N;

		cout << "Case #" << i + 1 << ": ";

		int a, b, g;
		g = -1;
		string Z;
		int m = 0;
		for (int j = N.size() - 1; j > 0; j--)
		{
			a = N[j] - '0' - (m * 1);
			b = N[j - 1] - '0';

			if (a < b)
			{
				Z = '9' + Z;
				g = j;
				m = 1;
			}
			else {
				Z = (char)(a + '0') + Z;
				m = 0;
			}
		}

		a = N[0] - '0' - (m * 1);

		if (a > 0)
		{
			Z = (char)(a + '0') + Z;
		}

		if (g > 0)
		{
			for (int j = g; j < Z.size(); j++)
			{
				Z[j] = '9';
			}
		}


		cout << Z << endl;

	}

}
