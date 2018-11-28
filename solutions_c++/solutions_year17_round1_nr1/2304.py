#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main()
{
	int T;
	cin >> T;

	for (int t = 1; t <= T; ++t)
	{
		int R, C;
		cin >> R >> C;

		vector<string> v(R);
		for (int i = 0; i < R; cin >> v[i++]);

		int first_empty = 0;
		while (v[first_empty] == string(C, '?')) ++first_empty;

		int last_empty = 0;
		while (v[R - last_empty - 1] == string(C, '?')) ++last_empty;

		for (int i = first_empty; i < R - last_empty; ++i)
		{
			// look for sth other than ?
			int pos = -1;
			for (int j = 0; j < C; ++j)
			{
				if (v[i][j] != '?')
				{
					pos = j;
					break;
				}
			}

			// if there are only ?, copy preceding line
			if (pos == -1)
			{
				v[i] = v[i-1];
			} else
			{
				for (int j = 0; j < pos; v[i][j++] = v[i][pos]);

				char x = v[i][pos];
				for (int j = pos + 1; j < C; ++j)
				{
					if (v[i][j] != '?' and v[i][j] != x) x = v[i][j];
					v[i][j] = x;
				}
			}

		}

		for (int i = 0; i < first_empty; ++i)
			v[i] = v[first_empty];

		for (int i = R - last_empty - 1; i < R; ++i)
			v[i] = v[R - last_empty - 1];

		cout << "Case #" << t << ":\n";
		for (int i = 0; i < R; ++i)
			cout << v[i] << '\n';;
	}
	return 0;
}
