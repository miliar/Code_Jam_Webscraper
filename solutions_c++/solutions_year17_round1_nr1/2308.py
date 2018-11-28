#include <iostream>
#include <vector>

using namespace std;

int main() {

	int T;
	cin >> T;

	int R, C;
	for (int i = 0; i < T; i++)
	{
		cin >> R >> C;
		cout << "Case #" << i + 1 << ":" << endl;;


		char **rc = new char*[R];
		for (int j = 0; j < R; j++)
		{
			rc[j] = new char[C];
		}

		vector<pair<char, int>> *buffer = new vector<pair<char, int>>[R];

		for (int j1 = 0; j1 < R; j1++)
		{
			for (int j2 = 0; j2 < C; j2++)
			{
				cin >> rc[j1][j2];
				if (rc[j1][j2] != '?')
				{
					buffer[j1].push_back({ rc[j1][j2], j2 });
				}
			}
		}

		int bi = 0;
		int prev = -1;
		int bi2 = 0;

		for (int j1 = 0; j1 < R; j1++)
		{
			bi = j1;
			bi2 = 0;

			if (buffer[bi].size() < 1)
			{
				if (prev < 0)
				{
					while (buffer[bi].size() < 1)
					{
						bi++;
					}
				}
				else {
					bi = prev;
				}
			}
			prev = bi;

			for (int j2 = 0; j2 < C; j2++)
			{
				if (bi < j1)
				{
					cout << rc[bi][j2];
				}
				else {
					if (rc[j1][j2] == '?')
					{
						rc[j1][j2] = buffer[bi][bi2].first;
						cout << buffer[bi][bi2].first;
					}
					else {
						cout << rc[j1][j2];
					}
					if (bi2 < buffer[bi].size() - 1 && buffer[bi][bi2].second <= j2)
					{
						bi2++;
					}
				}
			}

			cout << endl;
		}
	}

}
