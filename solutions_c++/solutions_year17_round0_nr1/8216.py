#include <bits/stdc++.h>

using namespace std;

bool check(const string & s)
{
    for (auto c : s)
	if (c == '-')
	    return false;
    return true;
}

char flip(char c)
{
    return c == '+' ? '-' : '+';
}

int main()
{
    int n; cin >> n;
    for (int i = 1; i <= n; ++i) {
	string s; int k;
	cin >> s >> k;
	int m = s.size(), c = 0;
	for (int j = 0; j + k -1 < m; ++j) {
	    if (s[j] == '-') {
		for (int r = 0; r < k; ++r)
		    s[j+r] = flip(s[j+r]);
		++c;
	    }
	}
	cout << "Case #" << i << ": ";
	if (check(s))
	    cout << c;
	else
	    cout << "IMPOSSIBLE";
	cout << endl;
    }
    return 0;
}
