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
}

void p3()
{
	
}

int main()
{
	cin >> cases;

	//TODO change problem number
	for (int i = 0; i < cases; ++i)p1();
}

//int** a = new int*[x];
//for (int i = 0; i < x; ++i)
//{
//	a[i] = new int[y];
//	for (int j = 0; j < y; ++j)
//	{
//		a[i][j] = val;
//	}
//}

//for (int i = 0; i < x; ++i)delete[] a[i];
//delete[] a;