#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int R, C;
vector<vector<char>> field;

void fill(int r1, int r2, int c1, int c2)
{
	//cerr << r1 << " " << r2 << " " << c1 << " " << c2 << endl;
	tuple<int, int, char> first, second;
	bool foundfirst = false, foundsecond = false;
	for(int r = r1; r <= r2; ++r)
	for(int c = c1; c <= c2; ++c)
	{
		if(field[r][c] != '?')
		{
			if(!foundfirst)
			{
				first = make_tuple(r, c, field[r][c]);	
				foundfirst = true;
			}
			else if(!foundsecond)
			{
				second = make_tuple(r, c, field[r][c]);	
				foundsecond = true;
			}
		}
	}

	if(!foundsecond)
	{
		char ch = get<2>(first);
		for(int r = r1; r <= r2; ++r)
		for(int c = c1; c <= c2; ++c)
		{
			field[r][c] = ch;
		}
	}
	else
	{
		if(get<0>(first) == get<0>(second))
		{
			//cerr << "case 1" << endl;
			fill(r1, r2, c1, get<1>(first));
			fill(r1, r2, get<1>(first) + 1, c2);
		}
		else
		{
			//cerr << "case 2" << endl;
			fill(r1, get<0>(first), c1, c2);
			fill(get<0>(first) + 1, r2, c1, c2);
		}
	}
}

void solve()
{
	cin >> R >> C;
	field = vector<vector<char>>(R, vector<char>(C));

	for(auto &r : field) for(auto &c : r) cin >> c;

	fill(0, R - 1, 0, C - 1);

	cout << "\n";
	for(auto &r : field) 
	{
		for(auto &c : r) cout << c;
		cout << "\n";
	}
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);

	int T;
	cin >> T;
	for(int t = 1; t <= T; ++t)
	{
		cout << "Case #" << t << ": ";
		solve();
	}
}
