#include <bits/stdc++.h>

using namespace std;

string max_tidy(char t, string s)
{
    if (s.size() == 1)
	return (s[0] >= t) ? s : "!";
    string r("!"), x("!");
    if (s[0]-1 >= t) {
	r.assign(1, s[0]-1);
	r += string(s.size()-1, '9');
    }
    if (s[0] >= t) {
	string y = max_tidy(s[0], s.substr(1));
	if (y != "!") {
	    x.assign(1, s[0]);
	    x += y;
	}
    }
    return max(r, x);
}

string trim(string s)
{
    reverse(s.begin(), s.end());
    while (s.size() > 1 && s.back() == '0')
	s.pop_back();
    reverse(s.begin(), s.end());
    return s;
}

int main()
{
    int n; cin >> n;
    for (int i = 1; i <= n; ++i) {
	string s; cin >> s;
	cout << "Case #" << i << ": " << trim(max_tidy(0, s)) << endl;
    }
    return 0;
}
