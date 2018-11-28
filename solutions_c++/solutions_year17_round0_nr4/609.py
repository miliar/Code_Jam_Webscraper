#include<iostream>
#include<algorithm>
#include<vector>
#include<string>

using namespace std;

int main()
{
	int t;
	cin >> t;
	for (int i = 0; i < t; ++i)
	{
		int n, m;
		cin >> n >> m;

		vector<vector<char> > mapa(n, vector<char>(n, '.'));

		int ox=-1, oy=-1;
		vector<pair<int, int> > newplus, newcross, cross, plus;
		int coolness = 0;
		vector<int> row(n, 0);
		vector<int> col(n, 0);
		vector<int> diag(2*n-1, 0);
		vector<int> revdiag(2 * n - 1, 0);
		for (int j = 0; j < m; ++j)
		{
			char c;
			int x, y;
			cin >> c >> x >> y;
			--x;
			--y;
			mapa[x][y] = c;
			++coolness;
			if (c == 'o')
			{
				ox = x;
				oy = y;
				row[x] = 1;
				col[y] = 1;
				diag[x + y] = 1;
				revdiag[n - 1 + x - y] = 1;
				++coolness;
			}
			else if (c == '+')
			{
				diag[x + y] = 1;
				revdiag[n - 1 + x - y] = 1;
				plus.push_back(make_pair(x, y));
			}
			else
			{
				row[x] = 1;
				col[y] = 1;
				cross.push_back(make_pair(x, y));
			}
		}

		for (int k = n-1; k >=0; --k)
		{
			if (row[k] == 0)
			{
				int j = n-1;
				if (col[k] == 0)
					j = k;
				while (true)
				{
					if (j == -1 || j >= 0 && col[j] == 0 && mapa[k][j] == '.')
						break;
					--j;
				}

				if (j == -1)
					continue;

				newcross.push_back(make_pair(k, j));
				row[k] = 1;
				col[j] = 1;
				mapa[k][j] = 'x';
				++coolness;
			}
		}

		for (int y = 0; y < n; ++y)
		{
			int x = 0;
			if (diag[x+y] == 0 && revdiag[n - 1 + x - y] == 0 && mapa[x][y] == '.')
			{
				newplus.push_back(make_pair(x,y));
				diag[x+y] = 1;
				revdiag[n - 1 + x - y] = 1;
				mapa[x][y] = '+';
				++coolness;
			}
		}

		for (int y = n-1; y > 0; --y)
		{
			int x = n - 1;
			if (diag[x+y] == 0 && revdiag[n - 1 + x-y] == 0 && mapa[x][y] == '.')
			{
				newplus.push_back(make_pair(x, y));
				diag[x + y] = 1;
				revdiag[n - 1 + x - y] = 1;
				mapa[x][y] = '+';
				++coolness;
			}
		}

		for (int k = 0; k < 2*n-1; ++k)
		{
			if (diag[k] == 0)
			{
				int j = 0;
				int x, y;
				while (true)
				{
					if (j == 2 * n - 1)
						break;
					x = (k + j - n + 1);
					y = (k - (j - n + 1));
					if (j < 2 * n - 1 && revdiag[j] == 0)
					{
						if (x >= 0 && x < 2*n && y >= 0 && y < 2*n)
						{
							if (x % 2 == 0 && y % 2 == 0 && mapa[x / 2][y / 2] == '.')
								break;
						}
					}
					
					++j;
				}

				if (j == 2*n-1)
					continue;
				
				newplus.push_back(make_pair(x/2, y/2));
				diag[k] = 1;
				revdiag[j] = 1;
				mapa[x/2][y/2] = '+';
				++coolness;
			}
		}

		bool newo = false;
		if (ox == -1 && oy == -1)
		{
			for (int x = 0; x < n; ++x)
			{
				for (int y = 0; y < n; ++y)
				{
					if (mapa[x][y] == '.')
					{
						if (row[x] == 0 && col[y] == 0 && diag[x + y] == 0 && revdiag[n - 1 + x - y] == 0)
						{
							ox = x;
							oy = y;
							newo = true;
							break;
						}						
					}
					else if (mapa[x][y] == 'x')
					{
						if (diag[x + y] == 0 && revdiag[n - 1 + x - y] == 0)
						{
							ox = x;
							oy = y;
							newo = true;
							for (auto it = newcross.begin(); it != newcross.end(); ++it)
							{
								if (it->first == x && it->second == y)
								{
									newcross.erase(it);
									break;
								}
							}
							break;
						}
					}
					else if (mapa[x][y] == '+')
					{
						if (row[x] == 0 && col[y] == 0)
						{
							ox = x;
							oy = y;
							newo = true;
							for (auto it = newplus.begin(); it != newplus.end(); ++it)
							{
								if (it->first == x && it->second == y)
								{
									newplus.erase(it);
									break;
								}
							}
							break;
						}
					}
				}
				if (newo)
					break;
			}
			++coolness;
		}

		int count = newplus.size() + newcross.size() + (newo ? 1 : 0);

		cout << "Case #" << i + 1 << ": " << coolness << ' ' << count << '\n';
		if (count > 0)
		{
			for (int j = 0; j < newplus.size(); ++j)
			{
				cout << "+ " << newplus[j].first + 1 << ' ' << newplus[j].second + 1 << '\n';
			}
			for (int j = 0; j < newcross.size(); ++j)
			{
				cout << "x " << newcross[j].first + 1 << ' ' << newcross[j].second + 1 << '\n';
			}
			if (newo)
			{
				cout << "o " << ox + 1 << ' ' << oy + 1 << '\n';
			}
		}
	}
	return 0;
}