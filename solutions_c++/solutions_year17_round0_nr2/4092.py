#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>

using namespace std;
string s, ans;
int n, k;

string make9(int nn)
{
	string ss = "";
	for (int i = 0; i < nn; i++)
	{
		ss += '9';
	}
	return ss;
}

int main()
{
	ios::sync_with_stdio(false);
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	cin >> n;

	for (int i = 0; i < n; i++)
	{
		cin >> s;
		for (int j = s.size() - 2; j >= 0; j--)
		{
			if (s[j] > s[j + 1])
			{
				int temp = stoi(s.substr(j, 1));
				temp--;
				ans = to_string(temp);
				ans += make9(s.size() - j - 1);
				s = s.substr(0, j) + ans;
			}
		}

		if (s[0] == '0')
			s = s.substr(1);

		cout << "Case #" << i + 1 << ": ";
		cout << s << endl;

	}
}