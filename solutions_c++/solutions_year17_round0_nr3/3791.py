#define _CRT_SECURE_NO_DEPRECATE 1
#include <stdio.h>
#include <iostream>
#include <set>
using namespace std;

void solve(int tn)
{
	int n, k;
	multiset<int> s;
	cin >> n >> k;
	s.insert(n);
	for (int i = 0; i < k - 1; i++)
	{
		auto it = --s.end();
		s.insert((*it - 1) / 2);
		s.insert(*it / 2);
		s.erase(it);
	}
	int max = *(--s.end());
	cout << "Case #" << tn << ": " << max / 2 << " " << (max - 1) / 2 << endl;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf_s("%d", &t);
	for (int it = 0; it < t; it++)
		solve(it + 1);
	return 0;
}
