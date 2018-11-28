#include <iostream>
#include <vector>
#include <string>

using namespace std;

string shim(string t)
{
	int g = t.find_first_not_of('?');
	for (int i = 0; i < t.size(); i++)
	{
		if (t[i] != '?')
			g = i;

		t[i] = t[g];
	}

	return t;
}

vector <string> solve(vector <string> T)
{
	int f = -1;
	for (int i = 0; i < T.size(); i++)
	{
		if (T[i].find_first_not_of('?') == string::npos)
		{
			if (f != -1)
				T[i] = T[i - 1];

			continue;
		}

		if (f == -1)
			f = i;

		T[i] = shim(T[i]);
	}

	for (int i = 0; i < f; i++)
		T[i] = T[f];

	return T;
}

int main()
{
	int n;
	cin >> n;
	for (int z = 1; z <= n; z++)
	{
		int r, c;
		cin >> r >> c;

		vector <string> T(r);
		for (auto &y : T)
			cin >> y;
		
		T = solve(T);

		printf("Case #%d:\n", z);
		for (auto &k : T)
			cout << k << endl;
	}
}
