#include <bits/stdc++.h>
#include <string>

using namespace std;

int main()
{
	ios_base::sync_with_stdio(false);
	int n;
	cin >> n;

	for(int j = 0; j < n; ++j)
	{
		long long int num;
		cin >> num;

		std::ostringstream ss;
		ss << num;
		string s = ss.str();
		reverse(s.begin(), s.end());

		for (int i = 0; i < s.length() - 1; ++i) {
			if (s[i] < s[i+1]) {
				s[i] = '9';
				--s[i+1];

				for (int k = 0; k < i; ++k) {
					s[k] = '9';
				}
			}
		}

		if (s[s.length() - 1] == '0')
			s = s.substr(0, s.length() - 1);

		reverse(s.begin(), s.end());

		cout << "Case #" << j+1 << ": " << s << endl;
	}

	return 0;
}