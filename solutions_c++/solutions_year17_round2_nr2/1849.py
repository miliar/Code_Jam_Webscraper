#include <iostream>
#include <vector>
#include <string>
#define ll long long int
using namespace std;

vector<char> fd(6);

int mv(vector<int> &v){
	int m=0;
	int w;
	for (int i = 0; i < v.size(); i++)
	{
		if (v[i] > m) {
			m = v[i];
			w = i;
		}
	}
	return w;
}

int main()
{
	iostream::sync_with_stdio(false);
	cin.tie(0);
	int t;
	cin >> t;
	fd = { 'R','B','Y','O','G','V' };
	for (int q = 0; q < t; q++)
	{
		int n, r, o, y, g, b, v;
		cin >> n >> r >> o >> y >> g >> b >> v;
		vector<int>  tos(3);
		tos[0] = r;
		tos[1] = b;
		tos[2] = y;
		string out = "";
		out.push_back(fd[mv(tos)]);
		char last = fd[mv(tos)];
		char first = last;
		if (mv(tos)==0)
		{
			r--;
		}
		if (mv(tos) == 1)
		{
			b--;
		}
		if (mv(tos) == 2)
		{
			y--;
		}
		bool inp = false;
		for (int i = 0; i < n-1; i++)
		{
			if (last == 'R') {
				if (g > 0) {
					g--;
					last = 'G';
					out.push_back(last);
					continue;
				}
				if (b == 0 && y == 0)
				{
					inp = true;
					break;
				}
				if (first == 'B')
				{
					if (b >= y)
					{
						b--;
						last = 'B';
						out.push_back(last);
					}
					else
					{
						y--;
						last = 'Y';
						out.push_back(last);
					}
				}
				else
				{
					if (b > y)
					{
						b--;
						last = 'B';
						out.push_back(last);
					}
					else
					{
						y--;
						last = 'Y';
						out.push_back(last);
					}
				}
				
				continue;
			}
			if (last == 'B') {
				if (o > 0) {
					o--;
					last = 'O';
					out.push_back(last);
					continue;
				}
				if (r == 0 && y == 0)
				{
					inp = true;
					break;
				}
				if (first == 'R')
				{
					if (r >= y)
					{
						r--;
						last = 'R';
						out.push_back(last);
					}
					else
					{
						y--;
						last = 'Y';
						out.push_back(last);
					}
				}
				else
				{
					if (r > y)
					{
						r--;
						last = 'R';
						out.push_back(last);
					}
					else
					{
						y--;
						last = 'Y';
						out.push_back(last);
					}
				}
				
				continue;
			}
			if (last == 'Y') {
				if (v > 0) {
					v--;
					last = 'V';
					out.push_back(last);
					continue;
				}
				if (b == 0 && r == 0)
				{
					inp = true;
					break;
				}
				if (first == 'B')
				{
					if (b >= r)
					{
						b--;
						last = 'B';
						out.push_back(last);
					}
					else
					{
						r--;
						last = 'R';
						out.push_back(last);
					}
				}
				else
				{
					if (b > r)
					{
						b--;
						last = 'B';
						out.push_back(last);
					}
					else
					{
						r--;
						last = 'R';
						out.push_back(last);
					}
				}
				
				continue;
			}
			if (last == 'G')
			{
				if (r > 0) {
					r--;
					last = 'R';
					out.push_back(last);
				}
				else
				{
					inp = true;
					break;
				}
				continue;
			}
			if (last == 'V')
			{
				if (y > 0) {
					y--;
					last = 'Y';
					out.push_back(last);
				}
				else
				{
					inp = true;
					break;
				}
				continue;
			}
			if (last == 'O')
			{
				if (b > 0) {
					b--;
					last = 'B';
					out.push_back(last);
				}
				else
				{
					inp = true;
					break;
				}
				continue;
			}
		}
		//sprawdzanie ostatniej
		if (last == 'R')
		{
			if ( out[0]=='R' || out[0]=='V' || out[0]=='O' )
			{
				inp = true;
			}
		}
		if (last == 'Y')
		{
			if (out[0] == 'Y' || out[0] == 'G' || out[0] == 'O')
			{
				inp = true;
			}
		}
		if (last == 'B')
		{
			if (out[0] == 'B' || out[0] == 'G' || out[0] == 'V')
			{
				inp = true;
			}
		}
		if (last == 'O')
		{
			if (! (out[0]=='B'))
			{
				inp = true;
			}
		}
		if (last == 'V')
		{
			if (!(out[0] == 'Y'))
			{
				inp = true;
			}
		}
		if (last == 'G')
		{
			if (!(out[0] == 'R'))
			{
				inp = true;
			}
		}
		if (!inp)
		{
			for (int i = 0; i < n; i++)
			{
				if (last == 'R')
				{
					if (out[0] == 'R' || out[0] == 'V' || out[0] == 'O')
					{
						inp = true; cout << "hi";
					}
				}
				if (last == 'Y')
				{
					if (out[0] == 'Y' || out[0] == 'G' || out[0] == 'O')
					{
						inp = true; cout << "hi";
					}
				}
				if (last == 'B')
				{
					if (out[0] == 'B' || out[0] == 'G' || out[0] == 'V')
					{
						inp = true; cout << "hi";
					}
				}
				if (last == 'O')
				{
					if (!(out[0] == 'B'))
					{
						inp = true; cout << "hi";
					}
				}
				if (last == 'V')
				{
					if (!(out[0] == 'Y'))
					{
						inp = true; cout << "hi";
					}
				}
				if (last == 'G')
				{
					if (!(out[0] == 'R'))
					{
						inp = true; cout << "hi";
					}
				}
			}
		}


		if (inp)
		{
			cout << "Case #" << q + 1 << ": " << "IMPOSSIBLE\n";
		}
		else
		{
			cout << "Case #" << q + 1 << ": " << out << "\n";
		}
	}
	return 0;
}

