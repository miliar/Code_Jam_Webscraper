#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <utility>
#include <bitset>
#include <algorithm>
#include <set>
#include <iomanip>
#include <map>

using namespace std;

#define mp(a, b) make_pair(a,b)

long double EPS = 1e-9;

char getch(int i)
{
	char a[] = { 'R', 'O', 'Y', 'G', 'B', 'V' };
	return a[i];

}

vector< int> a(6);


void rec(vector<string> a, vector<string> b, vector<string> c)
{
	if (b.size() >= a.size() && b.size()>=c.size())
	{
		swap(a, b);
	}
	if (c.size() >= a.size() && c.size() >= b.size())
	{
		swap(a, c);
	}
	if (c.size() >= b.size() )
	{
		swap(b, c);
	}
	int n = a.size() + b.size() + c.size();
	
	
	vector<int> ans(n);

	int a1 = a.size();
	int b1 = b.size();
	int c1 = c.size();

	if (a1>b1 + c1)
	{
		cout << "IMPOSSIBLE";
		return;
	}

	for (int i = 0;i < n;i+=2)
	{
		if (a1) {
			ans[i] = 0;
			a1--;
		}
		else if (b1)
		{
			ans[i] = 1;
			b1--;
		}
		else
		{
			ans[i] = 2;
			c1--;
		}

	}

	for (int i = 1;i < n;i += 2)
	{
		if (a1) {
			ans[i] = 0;
			a1--;
		}
		else if (b1)
		{
			ans[i] = 1;
			b1--;
		}
		else
		{
			ans[i] = 2;
			c1--;
		}

	}
	

	string res = "";
	for (int i = 0;i < n;i++)
	{
		if (ans[i]==0)
		{
			res += a.back();
			a.pop_back();
		}
		else if (ans[i] == 1)
		{
			res += b.back();
			b.pop_back();
		}
		else 
		{
			res += c.back();
			c.pop_back();
		}
	}
	if (res[0]==res[res.size()-1])
	{
		cout << "IMPOSSIBLE";
	}
	cout << res;
}

bool f1()
{

	int n;
	cin >> n;
	a.clear();
	a.resize(6);
	for (int i = 0;i < 6;i++)
	{
		cin >> a[i];
	}

	if (a[1]==a[4] && a[1]+a[4]==n)
	{
		for (int i = 0;i < n;i++)
		{
			if (i%2)
			{
				cout << getch(1);
			}
			else
			{
				cout << getch(4);
			}
		}
	}

	if (a[1] == a[4] && a[1] + a[4] == n)
	{
		for (int i = 0;i < n;i++)
		{
			if (i % 2)
			{
				cout << getch(1);
			}
			else
			{
				cout << getch(4);
			}
		}
		return true;
	}

	if (a[3] == a[0] && a[3] + a[0] == n)
	{
		for (int i = 0;i < n;i++)
		{
			if (i % 2)
			{
				cout << getch(3);
			}
			else
			{
				cout << getch(0);
			}
		}
		return true;
	}

	if (a[2] == a[5] && a[2] + a[5] == n)
	{
		for (int i = 0;i < n;i++)
		{
			if (i % 2)
			{
				cout << getch(2);
			}
			else
			{
				cout << getch(5);
			}
		}
		return true;
	}


	if (a[1] > a[4] * 2) {
		return false;
	}
	else {
		a[4] -= a[1] * 2;
	}

	if (a[3] > a[0] * 2) {
		return false;
	}
	else {
		a[0] -= a[3] * 2;
	}

	if (a[5] > a[2] * 2) {
		return false;
	}
	else {
		a[2] -= a[5] * 2;
	}
	map<char, vector<string> > mapa;
	for (int i = 0;i < 6;i++)
	{
		mapa[i] = vector < string  >();
	}
	for (int i = 0;i < 6;i++)
	{
		for (int j = 0;j < a[i];j++)
		{
			switch (i)
			{
			case 0: 
				mapa[i].push_back("R");
				break;
			case 1:
				mapa[4].push_back("BOB");
				break;
			case 2:
				mapa[i].push_back("Y");
				break;
			case 3:
				mapa[0].push_back("RGR");
				break;
			case 4:
				mapa[i].push_back("B");
				break;
			case 5:
				mapa[2].push_back("YVY");
				break;
			}
		}
	}
	rec(mapa[0], mapa[2], mapa[4]);
}

void f()
{
	if (!f1())
	{
		cout << "IMPOSSIBLE";
	}
}

int main() {
	int n;
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	cin >> n;
	for (int i = 0;i < n;i++)
	{
		
		cout << "Case #" << i + 1 << ": ";
		f();
		cout << endl;
	}

	return 0;
}