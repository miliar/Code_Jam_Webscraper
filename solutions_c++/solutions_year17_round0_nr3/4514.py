#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <utility>
#include <bitset>
#include <algorithm>
#include <set>

using namespace std;

#define mp(a, b) make_pair(a,b)


void f()
{
	int n, k;
	cin >> n >> k;
	multiset<int> s;
	s.insert(n);
	for (int i = 0;i < k-1;i++)
	{
		int x = *s.rbegin();
		
		s.erase(s.find(x));
		x--;
		s.insert(x / 2);
		s.insert((x+1) / 2);
	}
	int x = *s.rbegin();
	cout << (x) / 2 << ' ' << (x-1) / 2;
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