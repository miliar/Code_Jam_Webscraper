#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <utility>
#include <bitset>
#include <algorithm>
#include <set>

using namespace std;

#define mp(a, b) make_pair(a,b)

int e(int n, int k)
{
	if (k == 1)
		return n;
	int st = 0;
	int k0 = k;
	int mod = k % 2;
	while (k>1)
	{
		mod += k % 2;
		k /= 2;
		st++;

	}
	if (mod>0)
	{
		mod = 1;
	}
	k = k0;

	for (int i = 0;i < st-1;i++)
	{
		n--;
		n /= 2;
	}
	
	n /= 2;
	return n;
}

void f()
{
	int n, m;
	cin >> n >> m;
	vector<string> a(n);
	for (int i = 0;i < n;i++)
	{
		cin >> a[i];
	}
	for (int i = 0;i < n;i++)
	{
		int check = false;
		for (int j = 0;j < m;j++)
		{
			if (a[i][j]!='?')
			{
				int k = j + 1;
				while (k < m && a[i][k]=='?')
				{
					a[i][k] = a[i][k - 1];
					k++;
				}
			}
		}
		for (int j = m-1;j >=0;j--)
		{
			if (a[i][j] != '?')
			{
				int k = j - 1;
				while (k>=0 && a[i][k]=='?')
				{
					a[i][k] = a[i][k + 1];
					k--;
				}
			}
		}
	}

	for (int i = 1;i < n;i++)
	{
		int check = false;
		for (int j = 0;j < m;j++)
		{
			if (a[i][j] != '?')
			{
				check = true;
			}
		}
		if (!check)
		{
			a[i] = a[i - 1];
		}
		
	}

	for (int i = n-2;i >=0;i--)
	{
		int check = false;
		for (int j = 0;j < m;j++)
		{
			if (a[i][j] != '?')
			{
				check = true;
			}
		}
		if (!check)
		{
			a[i] = a[i + 1];
		}
	}
	cout << endl;
	for (int i = 0;i < n;i++)
	{
		cout << a[i] << endl;
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
		//cout << endl;
	}

	return 0;
}