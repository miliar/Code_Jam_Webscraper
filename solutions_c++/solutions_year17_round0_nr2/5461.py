# include <bits/stdc++.h>

using namespace std;

int ntest;
string s,a;
bool check;

void process(int p,int last)
{
	if (p == s.size())
	{
		check = true;
		return;
	}
	if (s[p] < last) return;
	a[p] = s[p];
	process(p+1,s[p]);
	if (! check)
	{
		a[p] = s[p]-1;
		if (a[p] < last) return;
		for (int i = p+1; i<s.size(); i++) a[i] = '9';
		check = true;
	}
}

main()
{
	freopen("B-large.in","r",stdin);
	freopen("B.out","w",stdout);
	cin >> ntest;
	for (int test = 1; test <= ntest; test++)
	{
		check = false;
		cin >> s;
		cout << "Case #" << test << ": ";
		process(0,'0');
		for (int i=0; i<s.size(); i++)
		if (a[i] != '0')
		{
			for (int j=i; j<s.size(); j++) cout << a[j];
			break;
		}
		cout << "\n";
	}
}
