#include<iostream>
#include<fstream>

using namespace std;

#define N 1001

static bool panc[N];

void flip(int index, int k)
{
	for (int i = index; i < index + k; i++)
	{
		panc[i] ^= true;
	}
}

int main()
{
	ifstream cin("in.txt");
	ofstream cout("out.txt");

	int T;
	cin >> T;

	for (int test_case = 0; test_case < T; test_case++)
	{
		int k, result = 0, n = -1, i;
		char temp = '-';
		bool possible = true;

		i = 0;
		while (temp == '-' || temp == '+')
		{			
			cin >> temp;
			panc[i] = temp == '+';
			n++;
			i++;
		}
		cin.putback(temp);
		cin >> k;

		for (i = 0; i <= n - k; i++)
		{
			if (!panc[i])
			{
				flip(i, k);
				result++;
			}
		}

		for (i = n - k; i < n; i++)
		{
			possible &= panc[i];
		}
		if (possible)
		{
			cout << "Case #" << test_case + 1 << ": " << result << endl;
		}
		else
		{
			cout << "Case #" << test_case + 1 << ": IMPOSSIBLE" << endl;
		}
	}
#ifdef _DEBUG
	system("pause");
#endif
	cin.close();
	cout.close();
	return 0;
}