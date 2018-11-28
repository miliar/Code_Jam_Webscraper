#include <iostream>
#include <algorithm>
#include <string>
#include <set>

using namespace std;

int currCase = 1;
int cases;

void print(const string &solution)
{
	cout << "Case #" << currCase << ": " << solution << '\n';
	++currCase;
}

void p1()
{
	double dist;
	int h;

	cin >> dist >> h;

	double speed;
	double bgn;

	double time = 0;

	for (int i = 0; i < h; ++i)
	{
		cin >> bgn >> speed;

		double t = (dist - bgn) / speed;

		if (t > time) time = t;
	}

	print(to_string(dist / time));
}

void p2()
{
	int n, r, o, y, g, b, v;
	cin >> n;
	cin >> r >> o >> y >> g >> b >> v;

	string stalls;
	stalls.resize(n);

	int next = 0;

	for (int i = 0; i < g; ++i)
	{
		stalls[next++] = 'R';
		stalls[next++] = 'G';
	}
	r -= g;
	if (next < n && g > 0)
	{
		stalls[next++] = 'R';
		--r;
	}

	for (int i = 0; i < o; ++i)
	{
		stalls[next++] = 'B';
		stalls[next++] = 'O';
	}
	b -= o;
	if (next < n && o > 0)
	{
		stalls[next++] = 'B';
		--b;
	}

	for (int i = 0; i < v; ++i)
	{
		stalls[next++] = 'Y';
		stalls[next++] = 'V';
	}
	y -= v;
	if (next < n && v > 0)
	{
		stalls[next++] = 'Y';
		--y;
	}

	if (next == 0)
	{
		if (r >= y && r >= b)
		{
			stalls[next++] = 'R';
			--r;
		}
		else if (b >= r && b >= y)
		{
			stalls[next++] = 'B';
			--b;
		}
		else
		{
			stalls[next++] = 'Y';
			--y;
		}
	}

	while (next < n)
	{
		if (stalls[next - 1] == 'R')
		{
			if (b > 0 && b > y)
			{
				stalls[next++] = 'B';
				--b;
				continue;
			}
			else if(y > 0)
			{
				stalls[next++] = 'Y';
				--y;
				continue;
			}
			else
			{
				print("IMPOSSIBLE");
				return;
			}
		}
		else if (stalls[next - 1] == 'B')
		{
			if (y > 0 && y > r)
			{
				stalls[next++] = 'Y';
				--y;
				continue;
			}
			else if (r > 0)
			{
				stalls[next++] = 'R';
				--r;
				continue;
			}
			else
			{
				print("IMPOSSIBLE");
				return;
			}
		}
		else if (stalls[next - 1] == 'Y')
		{
			if (r > 0 && r > b)
			{
				stalls[next++] = 'R';
				--r;
				continue;
			}
			else if (b > 0)
			{
				stalls[next++] = 'B';
				--b;
				continue;
			}
			else
			{
				print("IMPOSSIBLE");
				return;
			}
		}
	}

	if (r < 0 || y < 0 || b < 0)
	{
		print("IMPOSSIBLE");
		return;
	}

	if (stalls[n - 1] == stalls[0])
	{
		if (stalls[n - 2] == 'G' || stalls[n - 2] == 'O' || stalls[n - 2] == 'V')
		{
			print("IMPOSSIBLE");
			return;
		}

		char tmp = stalls[n - 1];
		stalls[n - 1] = stalls[n - 2];
		stalls[n - 2] = tmp;

		if (stalls[n - 3] == stalls[n - 2] || stalls[n - 2] == stalls[n - 1] || stalls[n - 1] == stalls[0])
		{
			print("IMPOSSIBLE");
			return;
		}
	}

	print(stalls);
}

void p3()
{
	
}

int main()
{
	cin >> cases;

	//TODO change problem number
	for (int i = 0; i < cases; ++i)p2();
}