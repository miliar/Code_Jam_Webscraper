#include <iostream>
#include <string>
#include <vector>

using namespace std;


int calc_flips(vector<bool> & v, int K)
{
	int flips = 0;
	for (int i=0; i<v.size(); i++)
	{
		if (!v[i])
		{
			if (i+K>v.size())
			{
				return -1;
			}
			for (int j=0; j<K; j++)
			{
				v[i+j] = !v[i+j];
			}
			flips++;
		}
	}
	return flips;
}

int main()
{
	int T;

	cin >> T;
	for (int i=0; i<T; i++)
	{
		string s;
		int K;
		vector<bool> v;
		cin >> s >> K;

		for (char c : s)
			v.push_back(c=='+');

		
		int flips = calc_flips(v, K);

		cout << "Case #" << i+1 << ": ";
		if (flips >= 0)
		{
			cout << flips << endl;
		}
		else
		{
			cout << "IMPOSSIBLE" << endl;
		}
	}
	return 0;
}