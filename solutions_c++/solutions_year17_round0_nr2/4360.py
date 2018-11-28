#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <utility>
#include <bitset>
#include <algorithm>

using namespace std;

#define mp(a, b) make_pair(a,b)


void f()
{
	string s;
	cin >> s;
	int n = s.size();
	int p = 0;
	for (p=1;p < n;p++)
	{
		if (s[p]<s[p-1])
		{
			break;
		}
	}
	if (p==n)
	{
		cout << s;
		return;
	}
	while (p!=0 && s[p]<s[p - 1])
	{
		p--;
		s[p]--;
	}
	
	string s_add = string(n-1 - p, '9');
	s = s.substr(0, p+1) + s_add;
	if (s[0]=='0' && s.size()>1)
	{
		s = s.substr(1, s.size() - 1);
	}
	cout << s;
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